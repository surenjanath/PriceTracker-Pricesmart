import asyncio
import aiohttp
import pandas as pd
import os
import datetime
from uuid import uuid4
import warnings
from time import perf_counter
import json
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, Date, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

warnings.simplefilter(action='ignore', category=FutureWarning)

# Configuration
cwd = os.getcwd()
Database_Name = 'PriceSmart_Products_Database.db'
Location = r'Database'
WorkingDir = os.path.join(cwd, Location)
if not os.path.exists(WorkingDir):
    os.mkdir(WorkingDir)

Database = os.path.join(WorkingDir, Database_Name)

Base = declarative_base()

class PriceHistory(Base):
    __tablename__ = 'price_history'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_pid = Column(String, ForeignKey('pricesmart_products.pid'))
    old_price = Column(Float)
    new_price = Column(Float)
    price_change = Column(Float)  # new_price - old_price
    price_change_percentage = Column(Float)
    change_type = Column(String)  # 'increase', 'decrease', 'new', 'discontinued'
    timestamp = Column(DateTime, default=datetime.datetime.now)
    
    def __repr__(self):
        return f"<PriceHistory(pid='{self.product_pid}', change='{self.price_change:.2f}', type='{self.change_type}')>"

class PriceSmart_Product(Base):
    __tablename__ = 'pricesmart_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pid = Column(String, unique=True)
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
    inventory_TT = Column(String)  # Changed from Integer to String to handle 'in stock' text
    promoid_TT = Column(String)
    category = Column(String)
    uniqueId = Column(String)
    last_updated = Column(DateTime)
    date_created = Column(DateTime)
    is_active = Column(String, default='true')  # Track if product is still available

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
        if self.date_created is None:
            self.date_created = datetime.datetime.now()
        self.last_updated = datetime.datetime.now()

    def __repr__(self):
        return f"<PriceSmart_Product(title='{self.title}', price={self.price_TT})>"

def clean_product_data(product_data):
    """Clean and prepare product data for database insertion"""
    cleaned_data = {}
    
    for key, value in product_data.items():
        if value is None:
            cleaned_data[key] = None
        elif isinstance(value, list):
            # Convert lists to comma-separated strings
            cleaned_data[key] = ', '.join(str(item) for item in value)
        elif isinstance(value, (int, float, str)):
            cleaned_data[key] = value
        else:
            # Convert any other types to string
            cleaned_data[key] = str(value)
    
    # Get fractionDigits for proper price conversion
    fraction_digits = cleaned_data.get('fractionDigits', 2)  # Default to 2 if not provided
    
    # Fix price_TT to convert using fractionDigits
    if 'price_TT' in cleaned_data and cleaned_data['price_TT'] is not None:
        try:
            # Convert using fractionDigits (e.g., if fractionDigits=2, divide by 10^2=100)
            price_in_cents = float(cleaned_data['price_TT'])
            divisor = 10 ** fraction_digits
            cleaned_data['price_TT'] = price_in_cents / divisor
        except (ValueError, TypeError):
            # If conversion fails, keep original value
            pass
    
    # Also fix other price fields if they exist
    price_fields = ['price', 'price_per_uom_TT', 'weight_TT']
    for field in price_fields:
        if field in cleaned_data and cleaned_data[field] is not None:
            try:
                price_in_cents = float(cleaned_data[field])
                divisor = 10 ** fraction_digits
                cleaned_data[field] = price_in_cents / divisor
            except (ValueError, TypeError):
                # If conversion fails, keep original value
                pass
    
    return cleaned_data

class PriceSmartScraper:
    def __init__(self, categories=None):
        self.categories = categories or ['G10D03']  # Default to Groceries category
        self.ParsedData = []
        self.request_count = 0
        self.last_request_time = 0
        
    def check_visit_time(self):
        """Check if current time is within allowed visiting hours (0600-1000)"""
        current_hour = datetime.datetime.now().hour
        return True  # PriceSmart doesn't have specific time restrictions
        
    def should_respect_rate_limit(self):
        """Ensure we don't exceed 1 request per 2 seconds for API calls"""
        current_time = perf_counter()
        if current_time - self.last_request_time < 2:
            return False
        return True

    async def fetch_products(self, session, category, start=0, rows=12):
        url = "https://www.pricesmart.com/api/br_discovery/getProductsByKeyword"
        
        # Check rate limiting
        while not self.should_respect_rate_limit():
            await asyncio.sleep(1)
            
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.pricesmart.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': f'https://www.pricesmart.com/en-tt/category/Groceries/{category}',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
        }
        
        cookies = {
            'vsf-locale': 'en-tt',
            'vsf-currency': 'TTD',
            'vsf-store': 'TT',
            'ajs_anonymous_id': 'd6022d33-52db-4cc5-ac52-07f59d935e1a',
            'vsf-channel': 'a67413c4-4eee-4bbe-8fef-355dd5d31b36',
            'vsf-country': 'TT'
        }
        
        payload = {
            "url": f"https://www.pricesmart.com/en-tt/category/Groceries/{category}",
            "start": start,
            "q": category,
            "fq": [],
            "search_type": "category",
            "rows": rows,
            "account_id": "7024",
            "auth_key": "ev7libhybjg5h1d1",
            "request_id": int(perf_counter() * 1000),
            "domain_key": "pricesmart_bloomreach_io_en",
            "fl": "pid,title,price,thumb_image,brand,slug,skuid,currency,fractionDigits,master_sku,sold_by_weight_TT,weight_TT,weight_uom_description_TT,sign_price_TT,price_per_uom_TT,uom_description_TT,availability_TT,price_TT,inventory_TT,promoid_TT",
            "view_id": "TT"
        }
        
        # Update request tracking
        self.request_count += 1
        self.last_request_time = perf_counter()
        
        retries = 3
        for attempt in range(retries):
            try:
                async with session.post(url, json=payload, headers=headers, cookies=cookies) as response:
                    # Save the raw JSON response for debugging
                    response_content = await response.content.read()
                    
                    ## Debugging information
                    # filename = f'response_{category}_{start}_{rows}.json'
                    # with open(filename, 'wb') as file:
                    #     file.write(response_content)
                    # print(f'[*] Saved response to: {filename}')

                    if response.status == 200:
                        try:
                            # Parse JSON response
                            data = json.loads(response_content.decode('utf-8'))
                            
                            # Extract products from response
                            products = data.get('response', {}).get('docs', [])
                            
                            # Process each product
                            for product in products:
                                product['category'] = category
                                self.ParsedData.append(product)
                            
                            print(f'[*] Data Scraped: {category} - {len(products)} products (start={start})')
                            return products
                            
                        except Exception as e:
                            print(f'[*] Error parsing JSON: {e} for {category}')
                            return None
                    else:
                        print(f'[*] Error {response.status} occurred while fetching data for {category}')
                        return None
                        
            except aiohttp.ClientConnectionError:
                if attempt < retries - 1:
                    print(f'[*] Connection error occurred. Retrying... Attempt {attempt + 1}/{retries}')
                    await asyncio.sleep(2)
                else:
                    print('[*] Maximum retries reached. Unable to establish connection.')
                    return None

    async def main(self):
        async with aiohttp.ClientSession() as session:
            print(f'[*] Starting scraping with {len(self.categories)} categories to process')
            print(f'[*] Respecting rate limiting: 1 request per 2 seconds')
            
            for i, category in enumerate(self.categories, 1):
                print(f'[*] Processing category {i}/{len(self.categories)}: {category}')
                
                # Fetch first page to get total count
                first_page = await self.fetch_products(session, category, start=0, rows=100)
                if first_page is None:
                    continue
                
                # Calculate total pages (assuming 12 products per page)
                total_products = len(first_page)
                if total_products == 100:  # If we got full page, there might be more
                    # Fetch additional pages
                    for start in range(100, 1200, 100):  # Limit to reasonable number of pages
                        await asyncio.sleep(2)  # Rate limiting
                        additional_products = await self.fetch_products(session, category, start=start, rows=100)
                        if additional_products is None or len(additional_products) == 0:
                            break
                
                # Additional delay between categories
                if i < len(self.categories):
                    print(f'[*] Waiting 2 seconds before next category...')
                    await asyncio.sleep(2)

def add_products_to_db(session, products_data):
    new_products = 0
    updated_products = 0
    price_changes = 0
    stock_changes = 0
    discontinued_products = 0
    
    # Get all current product PIDs to detect discontinued products
    current_pids = {p.pid for p in session.query(PriceSmart_Product).filter_by(is_active='true').all()}
    scraped_pids = {p.get('pid') for p in products_data if p.get('pid')}
    
    # Mark products as discontinued if they're not in current scrape
    discontinued_pids = current_pids - scraped_pids
    for pid in discontinued_pids:
        product = session.query(PriceSmart_Product).filter_by(pid=pid).first()
        if product:
            product.is_active = 'false'
            discontinued_products += 1
            print(f'[*] Product discontinued: {product.title}')
    
    for product_data in products_data:
        try:
            # Clean the product data to handle lists and other data types
            cleaned_data = clean_product_data(product_data)
            
            # Check if product already exists
            existing_product = session.query(PriceSmart_Product).filter_by(pid=cleaned_data.get('pid')).first()
            if existing_product:
                # Track changes before updating
                old_price = existing_product.price_TT
                old_availability = existing_product.availability_TT
                old_inventory = existing_product.inventory_TT
                
                # Update existing product
                for key, value in cleaned_data.items():
                    if hasattr(existing_product, key):
                        setattr(existing_product, key, value)
                existing_product.last_updated = datetime.datetime.now()
                existing_product.is_active = 'true'  # Mark as active since it's in current scrape
                
                # Check for significant changes
                new_price = cleaned_data.get('price_TT')
                new_availability = cleaned_data.get('availability_TT')
                new_inventory = cleaned_data.get('inventory_TT')
                
                # Track price changes with history
                if new_price and old_price and abs(new_price - old_price) > 0.01:
                    price_change = new_price - old_price
                    price_change_percentage = (price_change / old_price) * 100
                    change_type = 'increase' if price_change > 0 else 'decrease'
                    
                    # Create price history record
                    price_history = PriceHistory(
                        product_pid=cleaned_data.get('pid'),
                        old_price=old_price,
                        new_price=new_price,
                        price_change=price_change,
                        price_change_percentage=price_change_percentage,
                        change_type=change_type
                    )
                    session.add(price_history)
                    
                    print(f'[*] Price change detected for {cleaned_data.get("title", "Unknown")}: ${old_price:.2f} → ${new_price:.2f} ({price_change_percentage:+.1f}%)')
                    price_changes += 1
                
                # Log stock/availability changes
                if new_availability != old_availability or new_inventory != old_inventory:
                    print(f'[*] Stock/Availability change for {cleaned_data.get("title", "Unknown")}: {old_availability}/{old_inventory} → {new_availability}/{new_inventory}')
                    stock_changes += 1
                
                updated_products += 1
            else:
                # Create new product
                product_instance = PriceSmart_Product(**cleaned_data)
                session.add(product_instance)
                new_products += 1
                
                # Create price history record for new product
                if cleaned_data.get('price_TT'):
                    price_history = PriceHistory(
                        product_pid=cleaned_data.get('pid'),
                        old_price=0,
                        new_price=cleaned_data.get('price_TT'),
                        price_change=cleaned_data.get('price_TT'),
                        price_change_percentage=100,
                        change_type='new'
                    )
                    session.add(price_history)
                
                print(f'[*] New product added: {cleaned_data.get("title", "Unknown")} at ${cleaned_data.get("price_TT", 0):.2f}')
                
        except Exception as e:
            print('[*] Error:', e)
            print(f'[*] Problematic data: {product_data}')
    
    session.commit()
    
    # Summary of changes
    print(f'[*] Database update summary:')
    print(f'    - New products: {new_products}')
    print(f'    - Updated products: {updated_products}')
    print(f'    - Price changes detected: {price_changes}')
    print(f'    - Stock/availability changes: {stock_changes}')
    print(f'    - Discontinued products: {discontinued_products}')
    
    return {
        'new_products': new_products,
        'updated_products': updated_products,
        'price_changes': price_changes,
        'stock_changes': stock_changes,
        'discontinued_products': discontinued_products
    }

def generate_price_analysis_report(session, change_summary):
    """Generate detailed price analysis report"""
    
    # Get recent price changes (last 30 days)
    thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    recent_changes = session.query(PriceHistory).filter(
        PriceHistory.timestamp >= thirty_days_ago
    ).order_by(PriceHistory.timestamp.desc()).all()
    
    # Get biggest price increases and decreases
    biggest_increases = session.query(PriceHistory).filter(
        PriceHistory.change_type == 'increase'
    ).order_by(PriceHistory.price_change_percentage.desc()).limit(10).all()
    
    biggest_decreases = session.query(PriceHistory).filter(
        PriceHistory.change_type == 'decrease'
    ).order_by(PriceHistory.price_change_percentage.asc()).limit(10).all()
    
    # Get recently discontinued products
    discontinued_products = session.query(PriceSmart_Product).filter(
        PriceSmart_Product.is_active == 'false'
    ).order_by(PriceSmart_Product.last_updated.desc()).limit(10).all()
    
    # Get new products added today
    today = datetime.datetime.now().date()
    new_products = session.query(PriceSmart_Product).filter(
        PriceSmart_Product.date_created >= today
    ).order_by(PriceSmart_Product.date_created.desc()).all()
    
    # Calculate statistics
    total_price_changes = len(recent_changes)
    price_increases = len([c for c in recent_changes if c.change_type == 'increase'])
    price_decreases = len([c for c in recent_changes if c.change_type == 'decrease'])
    
    avg_increase = sum([c.price_change_percentage for c in recent_changes if c.change_type == 'increase']) / max(price_increases, 1)
    avg_decrease = sum([c.price_change_percentage for c in recent_changes if c.change_type == 'decrease']) / max(price_decreases, 1)
    
    markdown_report = f"""# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: {total_price_changes}
- **Price increases**: {price_increases}
- **Price decreases**: {price_decreases}
- **Average increase**: {avg_increase:.1f}%
- **Average decrease**: {avg_decrease:.1f}%

## Recent Price Changes
"""
    
    if recent_changes:
        markdown_report += """
| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
"""
        for change in recent_changes[:15]:  # Show last 15 changes
            product = session.query(PriceSmart_Product).filter_by(pid=change.product_pid).first()
            product_name = product.title if product else "Unknown"
            markdown_report += f"| {product_name} | ${change.old_price:.2f} | ${change.new_price:.2f} | ${change.price_change:+.2f} | {change.price_change_percentage:+.1f}% | {change.change_type.title()} |\n"
    else:
        markdown_report += "No recent price changes detected.\n"
    
    markdown_report += f"""
## Biggest Price Increases (All Time)
"""
    
    if biggest_increases:
        markdown_report += """
| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
"""
        for change in biggest_increases:
            product = session.query(PriceSmart_Product).filter_by(pid=change.product_pid).first()
            product_name = product.title if product else "Unknown"
            markdown_report += f"| {product_name} | ${change.old_price:.2f} | ${change.new_price:.2f} | +{change.price_change_percentage:.1f}% |\n"
    else:
        markdown_report += "No price increases recorded.\n"
    
    markdown_report += f"""
## Biggest Price Decreases (All Time)
"""
    
    if biggest_decreases:
        markdown_report += """
| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
"""
        for change in biggest_decreases:
            product = session.query(PriceSmart_Product).filter_by(pid=change.product_pid).first()
            product_name = product.title if product else "Unknown"
            markdown_report += f"| {product_name} | ${change.old_price:.2f} | ${change.new_price:.2f} | {change.price_change_percentage:.1f}% |\n"
    else:
        markdown_report += "No price decreases recorded.\n"
    
    markdown_report += f"""
## Recently Discontinued Products
"""
    
    if discontinued_products:
        markdown_report += """
| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
"""
        for product in discontinued_products:
            markdown_report += f"| {product.title} | {product.brand} | ${product.price_TT:.2f} | {product.last_updated.strftime('%Y-%m-%d')} |\n"
    else:
        markdown_report += "No discontinued products.\n"
    
    markdown_report += f"""
## New Products Added Today
"""
    
    if new_products:
        markdown_report += """
| Product | Brand | Price | Category |
|---------|-------|-------|----------|
"""
        for product in new_products:
            markdown_report += f"| {product.title} | {product.brand} | ${product.price_TT:.2f} | {product.category} |\n"
    else:
        markdown_report += "No new products added today.\n"
    
    return markdown_report

def generate_markdown_report(products_data, change_summary=None, db_session=None):
    if not products_data:
        return "# PriceSmart Products Report\n\nNo products found."
    
    # Basic statistics
    total_products = len(products_data)
    total_value = sum(float(p.get('price_TT', 0)) for p in products_data if p.get('price_TT'))
    avg_price = total_value / total_products if total_products > 0 else 0
    
    # Brand analysis
    brands = {}
    for product in products_data:
        brand = product.get('brand', 'Unknown')
        brands[brand] = brands.get(brand, 0) + 1
    
    top_brands = sorted(brands.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Generate Markdown
    markdown_report = f"""# PriceSmart Products Analysis Report

## Basic Analysis
- **Total products scraped**: {total_products}
- **Total value**: ${total_value:,.2f}
- **Average price**: ${avg_price:,.2f}
"""
    
    # Add change summary if available
    if change_summary:
        markdown_report += f"""
## Database Changes
- **New products added**: {change_summary['new_products']}
- **Existing products updated**: {change_summary['updated_products']}
- **Price changes detected**: {change_summary['price_changes']}
- **Stock/availability changes**: {change_summary['stock_changes']}
- **Discontinued products**: {change_summary['discontinued_products']}
"""
    
    markdown_report += f"""
## Top 5 Brands

| Brand | Count |
|-------|-------|
"""
    
    for brand, count in top_brands:
        markdown_report += f"| {brand} | {count} |\n"
    
    markdown_report += """
## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
"""
    
    # Show first 10 products
    for product in products_data[:10]:
        title = product.get('title', 'N/A')
        brand = product.get('brand', 'N/A')
        price = product.get('price_TT', 0)
        availability = product.get('availability_TT', 'N/A')
        markdown_report += f"| {title} | {brand} | ${price:,.2f} | {availability} |\n"
    
    # Add detailed price analysis if database session is available
    if db_session:
        markdown_report += "\n" + generate_price_analysis_report(db_session, change_summary)
    
    return markdown_report

async def run_scraper(categories, db_session):
    scraper = PriceSmartScraper(categories)
    await scraper.main()
    
    # Add products to database and get change summary
    change_summary = add_products_to_db(db_session, scraper.ParsedData)

    # Generate Markdown report with change information
    markdown_report = generate_markdown_report(scraper.ParsedData, change_summary, db_session)

    # Write Markdown report to file
    with open('pricesmart_analysis_report.md', 'w', encoding='utf-8') as file:
        file.write(markdown_report)
    # Also write to analysis_report.html for GitHub Action compatibility
    with open('analysis_report.html', 'w', encoding='utf-8') as file:
        file.write(markdown_report)

    print("PriceSmart analysis report generated successfully.")

if __name__ == "__main__":
    start = perf_counter()
    
    # Define categories to scrape (you can add more categories here)
    categories = ['G10D03']  # Groceries category
    
    engine = create_engine(f'sqlite:///{Database}', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db_session = Session()
    
    try:
        asyncio.run(run_scraper(categories, db_session))
        print('[*] Adding Data to Database ... ')

    except Exception as e:
        print('*'*100)
        print(f'Error Occurred : {e}')
        print('*'*100)
    finally:
        db_session.close()

    stop = perf_counter()
    print("[*] Time taken : ", stop - start) 