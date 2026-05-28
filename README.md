# PriceSmart Products Web Scraper

This is a Python web scraper designed to fetch product data from PriceSmart's API at [https://www.pricesmart.com](https://www.pricesmart.com) and store them in a SQLite database. It utilizes asyncio and aiohttp for asynchronous API calls and SQLAlchemy for database operations.

## About PriceSmart

PriceSmart is a membership-based warehouse club operator in the Caribbean and Central America. This scraper focuses on extracting product information from their Trinidad and Tobago (TT) store, including groceries, electronics, household items, and more.

## MOBILE APP -- > see our [Launch App](https://surenjanath.github.io/PriceTracker-Pricesmart/)

## Features

- **API-Based Scraping**: Uses PriceSmart's internal API for reliable data extraction
- **Asynchronous Processing**: Efficient fetching using asyncio and aiohttp
- **Rate Limiting**: Implements proper rate limiting (1 request per 2 seconds) to be respectful
- **JSON Response Parsing**: Robust JSON parsing for structured data extraction
- **SQLite Database Storage**: Structured storage of product data using SQLAlchemy ORM
- **Error Handling**: Comprehensive error handling with retry logic and connection recovery
- **JSON Response Saving**: Saves raw JSON responses for debugging and verification
- **Data Analysis**: Generates comprehensive analysis reports including brand analysis and pricing statistics
- **Multi-Category Support**: Can scrape multiple product categories
- **Pagination Handling**: Automatically handles pagination to get all available products

## Requirements

- Python 3.7 or higher
- aiohttp
- pandas
- SQLAlchemy
- beautifulsoup4
- lxml
- html5lib

## Installation

1. Clone the repository or download the files
2. Install the required dependencies:
   ```bash
   pip install -r pricesmart_requirements.txt
   ```

## Usage

1. The scraper is pre-configured to scrape PriceSmart products from the Trinidad and Tobago store
2. Run the scraper:
   ```bash
   python pricesmart_scraper.py
   ```
3. The scraper will:
   - Fetch product data from PriceSmart's API with proper rate limiting
   - Parse the JSON responses and extract product information
   - Store results in the SQLite database
   - Generate analysis reports
   - Save JSON responses for debugging

## Configuration

### Categories
You can modify the `categories` list in the main section to scrape different product categories:

```python
categories = ['G10D03', 'G10D04', 'G10D05']  # Add more category codes
```

### Rate Limiting
The scraper implements a 2-second delay between requests to be respectful to the API:
- Built-in rate limiting ensures 1 request per 2 seconds
- Automatic delays between category processing

### Database Settings
- **Database Name**: `PriceSmart_Products_Database.db`
- **Location**: `Database/` folder
- Customize by modifying `Database_Name` and `Location` variables

## Data Structure

The scraper extracts the following data for each product:

- **pid**: Product ID
- **title**: Product title/name
- **price**: Base price
- **thumb_image**: Product thumbnail image URL
- **brand**: Product brand
- **slug**: URL slug
- **skuid**: SKU ID
- **currency**: Currency code (TTD)
- **fractionDigits**: Price decimal places
- **master_sku**: Master SKU reference
- **sold_by_weight_TT**: Whether sold by weight
- **weight_TT**: Weight value
- **weight_uom_description_TT**: Weight unit of measure
- **sign_price_TT**: Sign price
- **price_per_uom_TT**: Price per unit of measure
- **uom_description_TT**: Unit of measure description
- **availability_TT**: Product availability
- **price_TT**: Price in Trinidad and Tobago dollars
- **inventory_TT**: Inventory count
- **promoid_TT**: Promotion ID
- **category**: Product category

## Output Files

- **Database**: `Database/PriceSmart_Products_Database.db` - SQLite database with all scraped product data
- **HTML Reports**: `pricesmart_analysis_report.html` - Generated analysis report
- **Debug Files**: `response_{category}_{start}_{rows}.json` - Raw JSON responses for debugging

## Analysis Features

The generated HTML report includes:

- **Basic Statistics**: Total products, total value, average price
- **Brand Analysis**: Top 5 brands by product count
- **Recent Products**: Sample of scraped products with details
- **Pricing Analysis**: Price distribution and trends

## Technical Details

### API Endpoint
- **URL**: `https://www.pricesmart.com/api/br_discovery/getProductsByKeyword`
- **Method**: POST
- **Content-Type**: application/json

### Request Structure
The scraper sends properly formatted JSON payloads including:
- Category codes
- Pagination parameters
- Authentication keys
- Request metadata

### Error Handling
- Retry logic for connection failures (3 attempts)
- Graceful handling of JSON parsing errors
- Comprehensive logging for debugging
- Rate limiting to prevent API overload

### Database Schema
- Uses SQLAlchemy ORM for data management
- Auto-incrementing primary key
- Automatic timestamp tracking for data freshness
- Unique ID generation for each record
- Duplicate detection and update logic

## Ethical Scraping

This scraper is designed to be respectful to PriceSmart's servers:

- **Rate Limiting**: 2-second delays between requests
- **Proper Headers**: Uses appropriate User-Agent and headers
- **Session Management**: Maintains proper session cookies
- **Error Recovery**: Graceful handling of temporary failures
- **Data Usage**: Intended for research and analysis purposes only

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project was inspired by the need to analyze PriceSmart's product offerings and pricing
- Special thanks to the developers of aiohttp, pandas, SQLAlchemy, and other libraries
- Respectful API usage following best practices for data collection

## Disclaimer

This scraper is for educational and research purposes only. Please respect PriceSmart's terms of service and use the data responsibly. The scraper is designed to be respectful to their servers and should not be used for commercial purposes without proper authorization.

This project has recently gained unexpected attention. It was created for personal, educational purposes ONLY.

* **DO NOT ABUSE THIS SCRIPT:** Do not run it excessively or use it for commercial purposes.
* **RESPECT THE WEBSITE:** Scraping places a load on a website's servers. This script includes a 10-second delay between requests to be respectful. Please do not remove it.
* **USE AT YOUR OWN RISK:** The user is solely responsible for their use of this script. I (the author) am not responsible for any misuse, server overloads, IP bans, or any legal action that may result from its use. This project is provided as-is for educational demonstration.




## Analysis Results

<!--START_SECTION:analysis-->
{{analysis_placeholder}}
# PriceSmart Products Analysis Report

## Basic Analysis
- **Total products scraped**: 1142
- **Total value**: $127,041.91
- **Average price**: $111.25

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1141
- **Price changes detected**: 40
- **Stock/availability changes**: 11
- **Discontinued products**: 8

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 177 |
|  | 136 |
| Badia | 17 |
| Swiss | 15 |
| Brunswick | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member’s Selection Canola Oil 2 Units / 2.84 L / 96 oz | Member's Selection | $159.95 | true |
| Jimmy Dean Croissant Sausage, Egg & Cheese Sandwiches 1.53 kg / 3.38 lb | Jimmy Dean | $162.95 | true |
| Carnation Creamy Evaporated Milk 6 Units / 330 mL | Carnation | $54.95 | true |
| Coffee Toppers Cold Foam 2 Units / 425 g / 15 oz | Coffee Toppers | $77.95 | true |
| Sunny Fruits Dried Organic Figs 10 Units / 50 g / 1.76 oz | Sunny Fruits | $79.95 | true |
| Karnis Assorted Flavored Dressings 3 Units / 226 g / 8 oz | Karnis | $97.95 | true |
| Setton Farms Premium Quality Pub-Style Pistachio Mix 567 g / 20 oz | Setton Farms | $131.95 | true |
| Pascual Yogi Kids Strawberry and Banana Yogurt with Fruit Pouch 24 Units / 80 g | Pascual | $229.95 | true |
| Butterball Turkey Sausage 3 Units / 369 g / 13 oz | Butterball | $129.95 | true |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | Curly's | $137.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1149
- **Price increases**: 589
- **Price decreases**: 531
- **Average increase**: 5.8%
- **Average decrease**: -4.9%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Fresh Chicken Thighs Boneless Tray | $87.16 | $87.29 | $+0.13 | +0.1% | Increase |
| Frozen Lamb Leg Whole Boneless Tray Pack | $350.61 | $348.40 | $-2.21 | -0.6% | Decrease |
| Munchy's Krunch Oat Cookies with Strawberry and Black Currant 3 Units / 208 g / 7.33 oz | $0.00 | $49.95 | $+49.95 | +100.0% | New |
| Gouda Cheese Block | $88.88 | $89.01 | $+0.13 | +0.1% | Increase |
| Polly-O String Cheese Mozzarella & Cheddar 24 Units | $98.95 | $96.95 | $-2.00 | -2.0% | Decrease |
| Old El Paso Crispy Stand 'N Stuff Taco Shells 6 Units / 81 g | $56.95 | $54.70 | $-2.25 | -4.0% | Decrease |
| Frozen Pork Belly Skin On Sliced Tray  | $120.67 | $120.43 | $-0.24 | -0.2% | Decrease |
| Frozen Sliced Turkey Drumsticks | $188.80 | $187.59 | $-1.21 | -0.6% | Decrease |
| Fresh Chicken Leg Quarters Tray | $94.01 | $93.91 | $-0.10 | -0.1% | Decrease |
| Fresh Seasoned BBQ Chicken Quarters Bag | $91.44 | $91.21 | $-0.23 | -0.3% | Decrease |
| Fine Choice Fresh Marinated Chicken Tray | $90.98 | $91.21 | $+0.23 | +0.3% | Increase |
| Snack Pack Chocolate and Vanilla Pudding 36 Units / 92 g / 3 oz | $156.95 | $160.95 | $+4.00 | +2.5% | Increase |
| Nesquik Liquid Milk Drink with Cocoa Flavor 12 Units / 250 mL | $63.95 | $65.95 | $+2.00 | +3.1% | Increase |
| Swiss Jumbo Econopak Tomato Ketchup 8 Units / 2 L / 67 oz | $179.95 | $169.95 | $-10.00 | -5.6% | Decrease |
| Frozen Boneless Skinless Chicken Breast Tray | $137.94 | $138.35 | $+0.41 | +0.3% | Increase |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Fresh Beef Ribeye Steak Vacuum Packed | $246.08 | $2434.41 | +889.3% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $9.70 | $44.95 | +363.4% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $44.95 | $9.70 | -78.4% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Nestos Small Gherkins 520 g / 18.34 oz | Nestos | $62.95 | 2026-05-27 |
| Wellsley Farms Assorted Mini Quiches 1.02 kg / 2.25 lb | Wellsley Farms | $99.95 | 2026-05-27 |
| Creamery Novelties Coconut Ice Cream 3.78 L / 1 gal | Creamery Novelties | $49.95 | 2026-05-27 |
| Chicken Drumsticks Case 15 kg / 33 lb |  | $499.95 | 2026-05-27 |
| Dare Viva Puffs Cookies with Marshmallows and Strawberry Covered in Chocolate 2 Units / 300 g | Dare | $44.70 | 2026-05-27 |
| Seedless Watermelon  |  | $109.95 | 2026-05-27 |
| Treasured Harvest Mixed Nuts 907 g | Treasured Harvest | $99.95 | 2026-05-27 |
| Pepe's Nature´s Pride Pack of Peas and Dry Legumes 5 Units / 1 kg | Pepe's Nature's Pride | $112.70 | 2026-05-27 |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | Pillsbury | $71.70 | 2026-05-25 |
| Sunberry Farms Organic Mango Nectar Juice - Gluten Free 3.78 L / 128 oz | Sunberry Farms | $79.95 | 2026-05-25 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Munchy's Krunch Oat Cookies with Strawberry and Black Currant 3 Units / 208 g / 7.33 oz | Munchy's | $49.95 | G10D03 |
