"""
Test script to query and display analytics data from Supabase
"""
import os
import sys
import json
from supabase import create_client

# Fix Unicode encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'replace')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'replace')

# Supabase configuration (load from environment variables)
# No hardcoded values - must be set via .env file or environment variables
SUPABASE_URL = os.getenv('SUPABASE_URL', '')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY', '')

if not SUPABASE_URL:
    print("[ERROR] SUPABASE_URL not found in environment variables!")
    print("[INFO] Please set SUPABASE_URL in .env file or environment variables")
    exit(1)

if not SUPABASE_KEY:
    print("[ERROR] SUPABASE_SERVICE_ROLE_KEY not found in environment variables!")
    print("[INFO] Please set SUPABASE_SERVICE_ROLE_KEY in .env file or environment variables")
    print("[INFO] See .env.example for template")
    exit(1)

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("=" * 80)
print("TESTING ANALYTICS TABLE QUERIES")
print("=" * 80)

# Query 1: Get latest analytics (matches README)
print("\n[QUERY 1] Latest Analytics (matching README structure):")
print("-" * 80)
try:
    response = supabase.table('analytics')\
        .select('*')\
        .order('snapshot_date', desc=True)\
        .limit(1)\
        .execute()
    
    if response.data and len(response.data) > 0:
        latest = response.data[0]
        print(f"Snapshot Date: {latest.get('snapshot_date')}")
        print(f"\n[Basic Analysis]")
        print(f"  - Total products: {latest.get('total_products')}")
        print(f"  - Total value: ${float(latest.get('total_value', 0)):,.2f}")
        print(f"  - Average price: ${float(latest.get('average_price', 0)):,.2f}")
        
        print(f"\n[Product Status]")
        print(f"  - Active products: {latest.get('active_products')}")
        print(f"  - Discontinued products: {latest.get('discontinued_products')}")
        
        print(f"\n[Database Changes]")
        print(f"  - New products added: {latest.get('new_products_added')}")
        print(f"  - Existing products updated: {latest.get('existing_products_updated')}")
        print(f"  - Price changes detected: {latest.get('price_changes_detected')}")
        print(f"  - Stock/availability changes: {latest.get('stock_availability_changes')}")
        print(f"  - Discontinued products: {latest.get('discontinued_products_count')}")
        
        print(f"\n[Price Change Summary (30 days)]")
        print(f"  - Total price changes: {latest.get('total_price_changes_30d')}")
        print(f"  - Price increases: {latest.get('price_increases_30d')}")
        print(f"  - Price decreases: {latest.get('price_decreases_30d')}")
        print(f"  - Average increase: {float(latest.get('average_increase_percentage', 0)):.1f}%")
        print(f"  - Average decrease: {float(latest.get('average_decrease_percentage', 0)):.1f}%")
        
        # Parse and display top brands
        top_brands_json = latest.get('top_brands_json')
        if top_brands_json:
            try:
                top_brands = json.loads(top_brands_json)
                print(f"\n[Top 5 Brands]")
                for i, brand_data in enumerate(top_brands[:5], 1):
                    brand_name = brand_data.get('brand', '(No brand)')
                    count = brand_data.get('count', 0)
                    print(f"  {i}. {brand_name}: {count} products")
            except json.JSONDecodeError:
                print(f"\n[WARNING] Could not parse top_brands_json: {top_brands_json}")
        
        print(f"\n[Metadata]")
        print(f"  - Last updated: {latest.get('last_updated')}")
        print(f"  - Created at: {latest.get('created_at')}")
    else:
        print("[ERROR] No analytics data found")
except Exception as e:
    print(f"[ERROR] Error querying analytics: {e}")

# Query 2: Get historical trends (last 7 days)
print("\n\n[QUERY 2] Historical Trends (Last 7 Days):")
print("-" * 80)
try:
    response = supabase.table('analytics')\
        .select('snapshot_date, total_products, active_products, total_price_changes_30d, price_increases_30d, price_decreases_30d')\
        .order('snapshot_date', desc=True)\
        .limit(7)\
        .execute()
    
    if response.data:
        print(f"{'Date':<12} {'Total':<8} {'Active':<8} {'Changes':<10} {'Increases':<12} {'Decreases':<12}")
        print("-" * 80)
        for record in response.data:
            date = record.get('snapshot_date', 'N/A')
            total = record.get('total_products', 0)
            active = record.get('active_products', 0)
            changes = record.get('total_price_changes_30d', 0)
            increases = record.get('price_increases_30d', 0)
            decreases = record.get('price_decreases_30d', 0)
            print(f"{date:<12} {total:<8} {active:<8} {changes:<10} {increases:<12} {decreases:<12}")
    else:
        print("[ERROR] No historical data found")
except Exception as e:
    print(f"[ERROR] Error querying historical data: {e}")

# Query 3: Compare with README values
print("\n\n[QUERY 3] Verification - Comparing with README:")
print("-" * 80)
print("Expected from README:")
print("  - Total products scraped: 1149")
print("  - Total value: $129,165.51")
print("  - Average price: $112.42")
print("  - Price changes (30d): 1370")
print("  - Price increases: 776")
print("  - Price decreases: 527")
print("\nActual from Database:")
try:
    response = supabase.table('analytics')\
        .select('total_products, total_value, average_price, total_price_changes_30d, price_increases_30d, price_decreases_30d')\
        .order('snapshot_date', desc=True)\
        .limit(1)\
        .execute()
    
    if response.data:
        latest = response.data[0]
        print(f"  - Total products: {latest.get('total_products')}")
        print(f"  - Total value: ${float(latest.get('total_value', 0)):,.2f}")
        print(f"  - Average price: ${float(latest.get('average_price', 0)):,.2f}")
        print(f"  - Price changes (30d): {latest.get('total_price_changes_30d')}")
        print(f"  - Price increases: {latest.get('price_increases_30d')}")
        print(f"  - Price decreases: {latest.get('price_decreases_30d')}")
        
        # Verify match
        print("\n[Verification]")
        expected_total = 1149
        actual_total = latest.get('total_products')
        if abs(actual_total - expected_total) <= 200:  # Allow some variance
            print(f"  [OK] Total products match (within range)")
        else:
            print(f"  [WARNING] Total products differ: Expected ~{expected_total}, Got {actual_total}")
            
        expected_changes = 1370
        actual_changes = latest.get('total_price_changes_30d')
        if abs(actual_changes - expected_changes) <= 50:
            print(f"  [OK] Price changes match (within range)")
        else:
            print(f"  [WARNING] Price changes differ: Expected ~{expected_changes}, Got {actual_changes}")
except Exception as e:
    print(f"[ERROR] Error verifying: {e}")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)

