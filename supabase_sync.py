"""
Separate script to sync data from SQLite to Supabase.
This script reads data from the SQLite database, performs analysis,
and pushes results to Supabase without modifying the original scraper.
"""
import os
import sys
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from supabase import create_client, Client
import json
import warnings

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, will use system environment variables
    pass

# Fix Unicode encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'replace')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'replace')

# Suppress SQLAlchemy deprecation warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Supabase credentials (load from environment variables for security)
# Create a .env file with these variables (see .env.example)
# Or set them as GitHub Secrets for CI/CD
SUPABASE_URL = os.getenv('SUPABASE_URL', '')
SUPABASE_SERVICE_ROLE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY', '')
SUPABASE_DB_PASSWORD = os.getenv('SUPABASE_DB_PASSWORD', '')

# Validate required credentials
if not SUPABASE_URL:
    print("[ERROR] SUPABASE_URL not found in environment variables!")
    print("[INFO] Please set SUPABASE_URL in .env file or GitHub Secrets")
    sys.exit(1)

if not SUPABASE_SERVICE_ROLE_KEY:
    print("[ERROR] SUPABASE_SERVICE_ROLE_KEY not found in environment variables!")
    print("[INFO] Please set SUPABASE_SERVICE_ROLE_KEY in .env file or GitHub Secrets")
    print("[INFO] See .env.example for template")
    sys.exit(1)

# SQLite database path (same as scraper uses)
cwd = os.getcwd()
Database_Name = 'PriceSmart_Products_Database.db'
Location = r'Database'
WorkingDir = os.path.join(cwd, Location)
Database = os.path.join(WorkingDir, Database_Name)

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

# SQLAlchemy setup for reading SQLite
Base = declarative_base()

class PriceHistory(Base):
    __tablename__ = 'price_history'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_pid = Column(String)
    old_price = Column(Float)
    new_price = Column(Float)
    price_change = Column(Float)
    price_change_percentage = Column(Float)
    change_type = Column(String)
    timestamp = Column(DateTime)

class PriceSmart_Product(Base):
    __tablename__ = 'pricesmart_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pid = Column(String)
    title = Column(String)
    price = Column(Float)
    thumb_image = Column(String)
    brand = Column(String)
    slug = Column(String)
    skuid = Column(String)
    currency = Column(String)
    fractionDigits = Column(Integer)
    master_sku = Column(String)
    sold_by_weight_TT = Column(String)
    weight_TT = Column(Float)
    weight_uom_description_TT = Column(String)
    sign_price_TT = Column(String)
    price_per_uom_TT = Column(Float)
    uom_description_TT = Column(String)
    availability_TT = Column(String)
    price_TT = Column(Float)
    inventory_TT = Column(String)
    promoid_TT = Column(String)
    category = Column(String)
    uniqueId = Column(String)
    last_updated = Column(DateTime)
    date_created = Column(DateTime)
    is_active = Column(String)

def safe_str(value, max_len=50):
    """Safely convert value to string for display, handling Unicode"""
    if value is None:
        return 'N/A'
    try:
        s = str(value)
        if len(s) > max_len:
            s = s[:max_len] + '...'
        return s.encode('utf-8', errors='replace').decode('utf-8', errors='replace')
    except:
        return 'N/A'

# Define all possible keys to ensure consistency across batches
ALL_PRODUCT_KEYS = [
    'id', 'pid', 'title', 'price', 'thumb_image', 'brand', 'slug', 'skuid',
    'currency', 'fractiondigits', 'master_sku', 'sold_by_weight_tt', 'weight_tt',
    'weight_uom_description_tt', 'sign_price_tt', 'price_per_uom_tt', 'uom_description_tt',
    'availability_tt', 'price_tt', 'inventory_tt', 'promoid_tt', 'category',
    'uniqueid', 'is_active', 'last_updated', 'date_created'
]

def convert_to_supabase_format(product):
    """Convert SQLAlchemy product object to Supabase format (lowercase column names)
    Returns dict with ALL keys to ensure batch consistency"""
    try:
        # Build data dict with all possible keys
        data = {
            'id': product.id,
            'pid': product.pid if product.pid else None,
            'title': product.title if product.title else None,
            'price': float(product.price) if product.price is not None else None,
            'thumb_image': product.thumb_image if product.thumb_image else None,
            'brand': product.brand if product.brand else None,
            'slug': product.slug if product.slug else None,
            'skuid': product.skuid if product.skuid else None,
            'currency': product.currency if product.currency else None,
            'fractiondigits': int(product.fractionDigits) if product.fractionDigits is not None else None,
            'master_sku': product.master_sku if product.master_sku else None,
            'sold_by_weight_tt': product.sold_by_weight_TT if product.sold_by_weight_TT else None,
            'weight_tt': float(product.weight_TT) if product.weight_TT is not None else None,
            'weight_uom_description_tt': product.weight_uom_description_TT if product.weight_uom_description_TT else None,
            'sign_price_tt': product.sign_price_TT if product.sign_price_TT else None,
            'price_per_uom_tt': float(product.price_per_uom_TT) if product.price_per_uom_TT is not None else None,
            'uom_description_tt': product.uom_description_TT if product.uom_description_TT else None,
            'availability_tt': product.availability_TT if product.availability_TT else None,
            'price_tt': str(product.price_TT) if product.price_TT is not None else None,
            'inventory_tt': product.inventory_TT if product.inventory_TT else None,
            'promoid_tt': product.promoid_TT if product.promoid_TT else None,
            'category': product.category if product.category else None,
            'uniqueid': product.uniqueId if product.uniqueId else None,
            'is_active': product.is_active if product.is_active else None,
            'last_updated': product.last_updated.isoformat() if product.last_updated else None,
            'date_created': product.date_created.isoformat() if product.date_created else None
        }
        
        # Ensure all keys are present (for batch consistency)
        result = {}
        for key in ALL_PRODUCT_KEYS:
            result[key] = data.get(key)
        
        return result
    except Exception as e:
        print(f"[LOG] Error in convert_to_supabase_format for product {getattr(product, 'pid', 'unknown')}: {e}")
        raise

def convert_price_history_to_supabase(price_history):
    """Convert price history object to Supabase format
    Returns dict with ALL keys to ensure batch consistency"""
    data = {
        'id': price_history.id,
        'product_pid': price_history.product_pid if price_history.product_pid else None,
        'old_price': str(price_history.old_price) if price_history.old_price is not None else None,
        'new_price': str(price_history.new_price) if price_history.new_price is not None else None,
        'price_change': str(price_history.price_change) if price_history.price_change is not None else None,
        'price_change_percentage': str(price_history.price_change_percentage) if price_history.price_change_percentage is not None else None,
        'change_type': price_history.change_type if price_history.change_type else None,
        'timestamp': price_history.timestamp.isoformat() if price_history.timestamp else None
    }
    
    return data

def sync_products_to_supabase(db_session):
    """Sync all products from SQLite to Supabase"""
    print("\n" + "=" * 80)
    print("[STEP 1] Reading products from SQLite database...")
    print("=" * 80)
    
    # Get all products from SQLite
    print("[LOG] Querying SQLite for all products...")
    products = db_session.query(PriceSmart_Product).all()
    print(f"[LOG] Query completed. Found {len(products)} products in SQLite database")
    
    if len(products) == 0:
        print("[!] No products to sync. Make sure the scraper has run first.")
        return
    
    # Process products in batches
    batch_size = 100
    total_synced = 0
    total_errors = 0
    total_batches = (len(products) + batch_size - 1) // batch_size
    
    print(f"[LOG] Processing {len(products)} products in {total_batches} batches of {batch_size}")
    print("-" * 80)
    
    for i in range(0, len(products), batch_size):
        batch_num = i//batch_size + 1
        batch = products[i:i+batch_size]
        print(f"\n[LOG] Processing batch {batch_num}/{total_batches} (products {i+1} to {min(i+batch_size, len(products))})")
        batch_data = []
        
        for idx, product in enumerate(batch):
            try:
                # Only log every 10th product or on errors to reduce output
                if idx == 0 or (idx + 1) % 10 == 0 or idx == len(batch) - 1:
                    title_preview = safe_str(product.title, 50) if product.title else 'N/A'
                    print(f"[LOG]   Converting product {idx+1}/{len(batch)}: PID={product.pid}, Title={title_preview}")
                product_dict = convert_to_supabase_format(product)
                # Keep all keys for batch consistency (Supabase requires matching keys)
                batch_data.append(product_dict)
                if idx == 0 or (idx + 1) % 10 == 0 or idx == len(batch) - 1:
                    non_null_count = sum(1 for v in product_dict.values() if v is not None)
                    print(f"[LOG]   [OK] Converted successfully. Columns: {len(product_dict)} (non-null: {non_null_count})")
            except Exception as e:
                pid = getattr(product, 'pid', 'unknown')
                print(f"[!]   [ERROR] Error converting product {pid}: {e}")
                import traceback
                traceback.print_exc()
                total_errors += 1
                continue
        
        if batch_data:
            print(f"[LOG] Attempting to upsert {len(batch_data)} products to Supabase...")
            try:
                # Verify all items have same keys
                if len(batch_data) > 1:
                    first_keys = set(batch_data[0].keys())
                    for i, item in enumerate(batch_data[1:], 1):
                        item_keys = set(item.keys())
                        if first_keys != item_keys:
                            missing = first_keys - item_keys
                            extra = item_keys - first_keys
                            print(f"[!] [WARNING] Item {i} has mismatched keys. Missing: {missing}, Extra: {extra}")
                            # Fix by ensuring all items have all keys
                            for key in first_keys:
                                if key not in item:
                                    item[key] = None
                            for key in item_keys - first_keys:
                                if key not in batch_data[0]:
                                    batch_data[0][key] = None
                                    first_keys.add(key)
                
                # Upsert to Supabase (insert or update based on pid)
                print(f"[LOG] Calling Supabase API: table('pricesmart_products').upsert()...")
                response = supabase.table('pricesmart_products').upsert(
                    batch_data,
                    on_conflict='pid'
                ).execute()
                
                total_synced += len(batch_data)
                print(f"[OK] [SUCCESS] Batch {batch_num} synced successfully: {len(batch_data)} products")
                if hasattr(response, 'data'):
                    print(f"[LOG] Supabase response: {len(response.data) if response.data else 0} records returned")
                
            except Exception as e:
                error_msg = str(e)
                print(f"[!] [ERROR] Error syncing batch {batch_num}: {error_msg}")
                print(f"[LOG] Error type: {type(e).__name__}")
                import traceback
                traceback.print_exc()
                total_errors += len(batch_data)
                print(f"[LOG] Attempting individual inserts for failed batch...")
                # Try individual inserts for this batch
                individual_success = 0
                for product_dict in batch_data:
                    try:
                        supabase.table('pricesmart_products').upsert(
                            product_dict,
                            on_conflict='pid'
                        ).execute()
                        individual_success += 1
                        total_synced += 1
                    except Exception as e2:
                        pid = product_dict.get('pid', 'unknown')
                        print(f"[!]   [ERROR] Error syncing individual product {pid}: {e2}")
                        total_errors += 1
                if individual_success > 0:
                    print(f"[LOG] Individual inserts: {individual_success}/{len(batch_data)} succeeded")
        else:
            print(f"[!] Batch {batch_num} had no valid data to sync")
    
    print("\n" + "=" * 80)
    print("[STEP 1 SUMMARY] Products Sync Complete")
    print("=" * 80)
    print(f"    [OK] Total products synced: {total_synced}")
    print(f"    [ERROR] Errors: {total_errors}")
    print(f"    [STATS] Success rate: {(total_synced/(total_synced+total_errors)*100) if (total_synced+total_errors) > 0 else 0:.1f}%")

def ensure_product_exists_for_price_history(db_session, product_pid):
    """Ensure a product exists for a given PID. If not, create a minimal product record."""
    # Check if product exists in SQLite
    product = db_session.query(PriceSmart_Product).filter_by(pid=product_pid).first()
    
    if product:
        # Product exists in SQLite, sync it to Supabase
        try:
            product_dict = convert_to_supabase_format(product)
            supabase.table('pricesmart_products').upsert(
                product_dict,
                on_conflict='pid'
            ).execute()
            return True
        except Exception as e:
            print(f"[!] [WARNING] Could not sync product {product_pid} to Supabase: {e}")
            return False
    
    # Product doesn't exist - check if it exists in Supabase
    try:
        response = supabase.table('pricesmart_products').select('pid').eq('pid', product_pid).limit(1).execute()
        if response.data and len(response.data) > 0:
            return True  # Product exists in Supabase
    except Exception as e:
        print(f"[!] [WARNING] Could not check Supabase for product {product_pid}: {e}")
    
    # Product doesn't exist anywhere - create minimal product record
    # (Logging handled by caller)
    try:
        minimal_product = {
            'pid': product_pid,
            'title': f'Product {product_pid} (Historical)',
            'is_active': 'false',  # Mark as inactive since we don't have full data
            'date_created': datetime.datetime.now().isoformat(),
            'last_updated': datetime.datetime.now().isoformat()
        }
        
        # Ensure all keys are present
        result = {}
        for key in ALL_PRODUCT_KEYS:
            result[key] = minimal_product.get(key)
        
        supabase.table('pricesmart_products').upsert(
            result,
            on_conflict='pid'
        ).execute()
        return True
    except Exception as e:
        print(f"[!] [ERROR] Could not create minimal product for PID {product_pid}: {e}")
        return False

def sync_price_history_to_supabase(db_session):
    """Sync price history from SQLite to Supabase, ensuring all referenced products exist"""
    print("\n" + "=" * 80)
    print("[STEP 2] Reading price history from SQLite database...")
    print("=" * 80)
    
    # Get all price history records
    print("[LOG] Querying SQLite for all price history records...")
    price_history_records = db_session.query(PriceHistory).all()
    print(f"[LOG] Query completed. Found {len(price_history_records)} price history records")
    
    if len(price_history_records) == 0:
        print("[!] No price history to sync.")
        return
    
    # Ensure all products referenced in price history exist
    print("\n[LOG] Checking for orphaned price history records (missing products)...")
    unique_pids = set(ph.product_pid for ph in price_history_records if ph.product_pid)
    print(f"[LOG] Found {len(unique_pids)} unique product PIDs in price history")
    
    # Check which products exist in Supabase (batch check for performance)
    print(f"[LOG] Checking product existence in Supabase (batch query)...")
    missing_products = []
    
    # Batch check: get all existing PIDs from Supabase efficiently
    try:
        # Get all PIDs from Supabase in batches (Supabase supports 'in' filter)
        existing_pids = set()
        batch_check_size = 1000
        pid_list = list(unique_pids)
        
        print(f"[LOG] Checking {len(pid_list)} unique PIDs in batches of {batch_check_size}...")
        for i in range(0, len(pid_list), batch_check_size):
            batch_pids = pid_list[i:i+batch_check_size]
            try:
                # Use 'in' filter to check multiple PIDs at once (Supabase syntax)
                response = supabase.table('pricesmart_products').select('pid').in_('pid', batch_pids).execute()
                if response.data:
                    existing_pids.update(p['pid'] for p in response.data if 'pid' in p)
            except Exception as batch_error:
                # If batch query fails, try individual queries for this batch
                print(f"[!] [WARNING] Batch query failed for batch {i//batch_check_size + 1}, checking individually...")
                for pid in batch_pids:
                    try:
                        response = supabase.table('pricesmart_products').select('pid').eq('pid', pid).limit(1).execute()
                        if response.data and len(response.data) > 0:
                            existing_pids.add(pid)
                    except:
                        pass
        
        # Find missing products
        missing_products = list(unique_pids - existing_pids)
        print(f"[LOG] Found {len(existing_pids)} existing products, {len(missing_products)} missing")
        
    except Exception as e:
        print(f"[!] [WARNING] Batch check failed, falling back to individual checks: {e}")
        # Fallback to individual checks if batch fails
        missing_products = []
        for pid in unique_pids:
            try:
                response = supabase.table('pricesmart_products').select('pid').eq('pid', pid).limit(1).execute()
                if not response.data or len(response.data) == 0:
                    missing_products.append(pid)
            except Exception as e2:
                print(f"[!] [WARNING] Could not check product {pid}: {e2}")
                missing_products.append(pid)
    
    if missing_products:
        print(f"[LOG] Found {len(missing_products)} products missing from Supabase. Creating them...")
        created_count = 0
        for idx, pid in enumerate(missing_products):
            # Only log every 10th product creation
            if idx == 0 or (idx + 1) % 10 == 0 or idx == len(missing_products) - 1:
                print(f"[LOG] Creating product {idx+1}/{len(missing_products)}: PID={pid}")
            if ensure_product_exists_for_price_history(db_session, pid):
                created_count += 1
        print(f"[OK] Created {created_count}/{len(missing_products)} missing products")
    else:
        print("[OK] All products referenced in price history exist in Supabase")
    
    # Process in batches
    batch_size = 100
    total_synced = 0
    total_errors = 0
    total_batches = (len(price_history_records) + batch_size - 1) // batch_size
    
    print(f"[LOG] Processing {len(price_history_records)} records in {total_batches} batches of {batch_size}")
    print("-" * 80)
    
    for i in range(0, len(price_history_records), batch_size):
        batch_num = i//batch_size + 1
        batch = price_history_records[i:i+batch_size]
        print(f"\n[LOG] Processing batch {batch_num}/{total_batches} (records {i+1} to {min(i+batch_size, len(price_history_records))})")
        batch_data = []
        
        # Define all price history keys for consistency
        ALL_PRICE_HISTORY_KEYS = ['id', 'product_pid', 'old_price', 'new_price', 
                                   'price_change', 'price_change_percentage', 'change_type', 'timestamp']
        
        for idx, record in enumerate(batch):
            try:
                # Only log every 10th record or on errors to reduce output
                if idx == 0 or (idx + 1) % 10 == 0 or idx == len(batch) - 1:
                    print(f"[LOG]   Converting record {idx+1}/{len(batch)}: ID={record.id}, PID={record.product_pid}, Change={record.change_type}")
                record_dict = convert_price_history_to_supabase(record)
                # Ensure all keys are present for batch consistency
                result = {}
                for key in ALL_PRICE_HISTORY_KEYS:
                    result[key] = record_dict.get(key)
                batch_data.append(result)
                if idx == 0 or (idx + 1) % 10 == 0 or idx == len(batch) - 1:
                    print(f"[LOG]   [OK] Converted successfully")
            except Exception as e:
                print(f"[!]   [ERROR] Error converting price history record {record.id}: {e}")
                import traceback
                traceback.print_exc()
                total_errors += 1
                continue
        
        if batch_data:
            print(f"[LOG] Attempting to upsert {len(batch_data)} price history records to Supabase...")
            try:
                # Verify all items have same keys
                if len(batch_data) > 1:
                    first_keys = set(batch_data[0].keys())
                    for i, item in enumerate(batch_data[1:], 1):
                        item_keys = set(item.keys())
                        if first_keys != item_keys:
                            missing = first_keys - item_keys
                            extra = item_keys - first_keys
                            print(f"[!] [WARNING] Price history item {i} has mismatched keys. Missing: {missing}, Extra: {extra}")
                            # Fix by ensuring all items have all keys
                            for key in first_keys:
                                if key not in item:
                                    item[key] = None
                            for key in item_keys - first_keys:
                                if key not in batch_data[0]:
                                    batch_data[0][key] = None
                                    first_keys.add(key)
                
                # Insert price history (no upsert needed, these are historical records)
                print(f"[LOG] Calling Supabase API: table('price_history').upsert()...")
                response = supabase.table('price_history').upsert(
                    batch_data,
                    on_conflict='id'
                ).execute()
                
                total_synced += len(batch_data)
                print(f"[OK] [SUCCESS] Batch {batch_num} synced successfully: {len(batch_data)} records")
                if hasattr(response, 'data'):
                    print(f"[LOG] Supabase response: {len(response.data) if response.data else 0} records returned")
                
            except Exception as e:
                error_msg = str(e)
                print(f"[!] [ERROR] Error syncing price history batch {batch_num}: {error_msg}")
                print(f"[LOG] Error type: {type(e).__name__}")
                import traceback
                traceback.print_exc()
                total_errors += len(batch_data)
                # Try individual inserts for failed batch
                print(f"[LOG] Attempting individual inserts for failed batch...")
                individual_success = 0
                for record_dict in batch_data:
                    try:
                        supabase.table('price_history').upsert(
                            record_dict,
                            on_conflict='id'
                        ).execute()
                        individual_success += 1
                        total_synced += 1
                    except Exception as e2:
                        record_id = record_dict.get('id', 'unknown')
                        print(f"[!]   [ERROR] Error syncing individual price history record {record_id}: {e2}")
                        total_errors += 1
                if individual_success > 0:
                    print(f"[LOG] Individual inserts: {individual_success}/{len(batch_data)} succeeded")
    
    print("\n" + "=" * 80)
    print("[STEP 2 SUMMARY] Price History Sync Complete")
    print("=" * 80)
    print(f"    [OK] Total records synced: {total_synced}")
    print(f"    [ERROR] Errors: {total_errors}")
    print(f"    [STATS] Success rate: {(total_synced/(total_synced+total_errors)*100) if (total_synced+total_errors) > 0 else 0:.1f}%")

def calculate_and_sync_analytics(db_session):
    """Calculate analytics and sync to Supabase analytics tables"""
    print("\n" + "=" * 80)
    print("[STEP 3] Calculating and syncing analytics...")
    print("=" * 80)
    
    try:
        # Get current date for analytics
        today = datetime.datetime.now().date()
        thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
        
        # Calculate product statistics
        total_products = db_session.query(PriceSmart_Product).count()
        active_products = db_session.query(PriceSmart_Product).filter_by(is_active='true').count()
        discontinued_products = db_session.query(PriceSmart_Product).filter_by(is_active='false').count()
        
        # Calculate price statistics
        products_with_price = db_session.query(PriceSmart_Product).filter(
            PriceSmart_Product.price_TT.isnot(None),
            PriceSmart_Product.is_active == 'true'
        ).all()
        
        total_value = sum(float(p.price_TT) for p in products_with_price if p.price_TT)
        avg_price = total_value / len(products_with_price) if products_with_price else 0
        
        # Calculate price change statistics
        recent_changes = db_session.query(PriceHistory).filter(
            PriceHistory.timestamp >= thirty_days_ago
        ).all()
        
        total_price_changes = len(recent_changes)
        price_increases = len([c for c in recent_changes if c.change_type == 'increase'])
        price_decreases = len([c for c in recent_changes if c.change_type == 'decrease'])
        
        avg_increase = sum([c.price_change_percentage for c in recent_changes if c.change_type == 'increase']) / max(price_increases, 1) if price_increases > 0 else 0
        avg_decrease = sum([c.price_change_percentage for c in recent_changes if c.change_type == 'decrease']) / max(price_decreases, 1) if price_decreases > 0 else 0
        
        # Get new products today
        new_products_today = db_session.query(PriceSmart_Product).filter(
            PriceSmart_Product.date_created >= today
        ).count()
        
        # Calculate brand statistics (Top 5 brands - matches README)
        brand_counts = {}
        all_products = db_session.query(PriceSmart_Product).filter_by(is_active='true').all()
        for product in all_products:
            brand = product.brand if product.brand else ''
            brand_counts[brand] = brand_counts.get(brand, 0) + 1
        
        top_brands = sorted(brand_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        top_brands_json = json.dumps([{"brand": brand, "count": count} for brand, count in top_brands])
        
        # Get database change statistics from recent sync (if available)
        # Note: These would need to be passed from the sync process or calculated from price_history
        # For now, we'll calculate from price_history
        recent_price_changes_count = db_session.query(PriceHistory).filter(
            PriceHistory.timestamp >= today
        ).count()
        
        # Estimate new/updated products from price history
        new_products_from_history = db_session.query(PriceHistory).filter(
            PriceHistory.change_type == 'new',
            PriceHistory.timestamp >= today
        ).count()
        
        # Prepare analytics data (matches README structure)
        analytics_data = {
            'snapshot_date': today.isoformat(),
            
            # Basic Analysis (matches README)
            'total_products': total_products,
            'total_value': str(total_value),
            'average_price': str(avg_price),
            
            # Product Status
            'active_products': active_products,
            'discontinued_products': discontinued_products,
            
            # Database Changes (matches README) - estimated from price history
            'new_products_added': new_products_from_history,
            'existing_products_updated': total_products - new_products_from_history,  # Approximate
            'price_changes_detected': recent_price_changes_count,
            'stock_availability_changes': 0,  # Would need to track separately
            'discontinued_products_count': discontinued_products,
            
            # Price Change Statistics (30 days - matches README)
            'total_price_changes_30d': total_price_changes,
            'price_increases_30d': price_increases,
            'price_decreases_30d': price_decreases,
            'average_increase_percentage': str(avg_increase),
            'average_decrease_percentage': str(avg_decrease),
            
            # Daily Stats
            'new_products_today': new_products_today,
            
            # Top Brands (matches README)
            'top_brands_json': top_brands_json,
            
            'last_updated': datetime.datetime.now().isoformat()
        }
        
        print(f"[LOG] Calculated analytics (matching README structure):")
        print(f"  - Total products: {total_products}")
        print(f"  - Active products: {active_products}")
        print(f"  - Total value: ${total_value:,.2f}")
        print(f"  - Average price: ${avg_price:,.2f}")
        print(f"  - Price changes (30d): {total_price_changes}")
        print(f"  - Top brands: {', '.join([f'{b[0]} ({b[1]})' for b in top_brands[:3]])}")
        
        # Sync to Supabase analytics table
        print(f"[LOG] Syncing analytics to Supabase...")
        try:
            # Try to upsert analytics (update if snapshot_date exists, insert if new)
            response = supabase.table('analytics').upsert(
                analytics_data,
                on_conflict='snapshot_date'
            ).execute()
            print(f"[OK] Analytics synced successfully")
        except Exception as e:
            # If table doesn't exist, try creating it via insert
            print(f"[!] [WARNING] Analytics table might not exist: {e}")
            print(f"[LOG] Attempting to insert analytics data...")
            try:
                response = supabase.table('analytics').insert(analytics_data).execute()
                print(f"[OK] Analytics inserted successfully")
            except Exception as e2:
                print(f"[!] [ERROR] Could not sync analytics: {e2}")
                print(f"[LOG] You may need to create the analytics table in Supabase first")
                print(f"[LOG] Run the SQL from 'create_analytics_table.sql' in Supabase SQL Editor")
        
    except Exception as e:
        print(f"[!] [ERROR] Error calculating analytics: {e}")
        import traceback
        traceback.print_exc()

def perform_analysis_and_sync(db_session):
    """Perform analysis on the data and sync to Supabase"""
    print("=" * 80)
    print("PRICESMART SUPABASE SYNC")
    print("=" * 80)
    
    # Sync products
    print("\n[1/3] Syncing products...")
    sync_products_to_supabase(db_session)
    
    # Sync price history (with product validation)
    print("\n[2/3] Syncing price history...")
    sync_price_history_to_supabase(db_session)
    
    # Calculate and sync analytics
    print("\n[3/3] Calculating and syncing analytics...")
    calculate_and_sync_analytics(db_session)
    
    print("\n" + "=" * 80)
    print("SYNC COMPLETE")
    print("=" * 80)

def test_supabase_connection():
    """Test connection to Supabase"""
    print("[LOG] Testing Supabase connection...")
    print(f"[LOG] URL: {SUPABASE_URL}")
    print(f"[LOG] Service Role Key: {SUPABASE_SERVICE_ROLE_KEY[:20]}...")
    
    try:
        print("[LOG] Attempting to query 'pricesmart_products' table...")
        response = supabase.table('pricesmart_products').select('id').limit(1).execute()
        print(f"[LOG] Query successful. Response received.")
        if hasattr(response, 'data'):
            print(f"[LOG] Response data: {len(response.data) if response.data else 0} records")
        print("[OK] [SUCCESS] Supabase connection successful")
        return True
    except Exception as e:
        print(f"[!] [ERROR] Error connecting to Supabase: {e}")
        print(f"[LOG] Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        print("[!] Please check your Supabase credentials and network connection.")
        return False

def main():
    """Main function"""
    print("=" * 80)
    print("PRICESMART SUPABASE SYNC UTILITY")
    print("=" * 80)
    
    # Check if SQLite database exists
    if not os.path.exists(Database):
        print(f"[!] Error: SQLite database not found at {Database}")
        print("[!] Please run the scraper first to generate the database.")
        print(f"[!] Expected path: {Database}")
        return
    
    # Test Supabase connection
    print("\n[*] Testing Supabase connection...")
    if not test_supabase_connection():
        return
    
    # Connect to SQLite database
    print(f"\n[*] Connecting to SQLite database: {Database}")
    try:
        engine = create_engine(f'sqlite:///{Database}', echo=False)
        Session = sessionmaker(bind=engine)
        db_session = Session()
        
        # Verify tables exist
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        
        if 'pricesmart_products' not in tables:
            print("[!] Error: 'pricesmart_products' table not found in SQLite database")
            print("[!] Please run the scraper first to create the database tables.")
            db_session.close()
            return
        
        print("[OK] [SUCCESS] SQLite database connection successful")
        print(f"[OK] Found tables: {', '.join(tables)}")
        
    except Exception as e:
        print(f"[!] Error connecting to SQLite database: {e}")
        import traceback
        traceback.print_exc()
        return
    
    try:
        perform_analysis_and_sync(db_session)
    except Exception as e:
        print(f"[!] Error during sync: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db_session.close()
        print("\n[*] Database connection closed.")

if __name__ == "__main__":
    main()

