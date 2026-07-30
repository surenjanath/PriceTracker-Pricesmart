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
- **Total products scraped**: 1113
- **Total value**: $123,922.59
- **Average price**: $111.34

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1111
- **Price changes detected**: 44
- **Stock/availability changes**: 11
- **Discontinued products**: 7

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 176 |
|  | 132 |
| Badia | 16 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| McCain Cassava Sticks 997 g / 2.2 lb | McCain | $43.95 | true |
| Ocean Spray Cranberry Juice 2 Units 1.89 L / 64 oz | Ocean Spray | $77.95 | true |
| Coke Sugar-Free Canned Soda 6 Units / 355 mL / 12 oz | Coca-Cola | $24.95 | true |
| Nature's Pride Lentils 2.3 kg / 5 lb | Nature's Pride | $44.95 | true |
| Cultured Cravings Coconut Yogurt 12 Units / 150 g / 5.3 oz | Cultured Cravings | $229.95 | true |
| Sprite Lemon-Lime Flavor Soda 24 Units / 355 mL | Sprite | $99.95 | true |
| Member's Selection Freshly Made Assorted Doughnuts 12 Units | Member's Selection | $55.95 | true |
| Member's Selection Freshly Baked Chocolate Chip Cookies 24 Units | Member's Selection | $60.95 | true |
| Member's Selection Fresh Baked Vanilla Cake 20 to 24 Slices | Member's Selection | $102.95 | true |
| Member's Selection Vanilla Chocolate Cake Freshly Baked 20 to 25 Slices | Member's Selection | $102.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 982
- **Price increases**: 549
- **Price decreases**: 404
- **Average increase**: 5.8%
- **Average decrease**: -5.3%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Amazon Coconut Water 2 L / 67 oz | $62.95 | $59.95 | $-3.00 | -4.8% | Decrease |
| Ribeye Choice Fillet Fresh Tray | $311.21 | $315.71 | $+4.50 | +1.4% | Increase |
| Tropicland Frozen Mango Chunks 2.2 kg / 5 lb | $0.00 | $94.95 | $+94.95 | +100.0% | New |
| Gwaltney Chicken Bologna 2 Units / 567 g | $57.95 | $59.95 | $+2.00 | +3.5% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $117.83 | $118.01 | $+0.18 | +0.2% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $68.58 | $68.65 | $+0.07 | +0.1% | Increase |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $197.03 | $197.62 | $+0.59 | +0.3% | Increase |
| Bumble Bee Tuna Salad Snack 6 Units / 100 g / 3.5 oz | $82.95 | $81.95 | $-1.00 | -1.2% | Decrease |
| Frozen Bone In Pork Shoulder Sliced Tray | $70.23 | $71.64 | $+1.41 | +2.0% | Increase |
| Florida's Natural Mango Lemonade 2 Units / 1.75 L / 59 oz | $112.95 | $79.70 | $-33.25 | -29.4% | Decrease |
| García Meat Sausage 794 g / 1.75 lb | $64.95 | $39.70 | $-25.25 | -38.9% | Decrease |
| Nescafé Classic Instant Coffee 3 in 1 3 Units / 114 g | $52.95 | $54.95 | $+2.00 | +3.8% | Increase |
| Fresh Ground Chicken Tray | $101.22 | $100.97 | $-0.25 | -0.2% | Decrease |
| State Fair Mini Corn Dogs 46 Units / 18.7 g / 0.66 oz | $77.95 | $79.95 | $+2.00 | +2.6% | Increase |
| Sprite Lemon Flavored Soft Drink in Can 24 Units / 355 mL / 12 oz | $97.95 | $99.95 | $+2.00 | +2.0% | Increase |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Fresh Beef Ribeye Steak Vacuum Packed | $246.08 | $2434.41 | +889.3% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $9.70 | $44.95 | +363.4% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $44.95 | $9.70 | -78.4% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Parthenon Premium Mediterranean Olive Medley 900 g / 31.74 oz | Parthenon | $49.70 | 2026-07-29 |
| Cole Cold Assorted Soft Drinks 24 Units / 370 mL / 12.5 oz | Cole Cold | $43.95 | 2026-07-29 |
| Black Raisins 1 kg / 2.2 lb |  | $49.95 | 2026-07-29 |
| Aziz's Assortment Pack of Freshly Baked Traditional Sweets | Aziz's | $63.95 | 2026-07-29 |
| Frozen Bone-In Pork Butt Blade Steak |  | $76.82 | 2026-07-29 |
| Member's Selection Frozen Skinless Boneless Salmon Fillets Vacuum Packaged | Member's Selection | $325.37 | 2026-07-29 |
| Member's Selection Frozen Skin On Boneless Salmon Fillet Vacuum Packed | Member's Selection | $156.14 | 2026-07-29 |
| Kellogg's Rice Krispies Treat 25 Units / 37 g / 1.3 oz | Kellogg's | $119.95 | 2026-07-27 |
| Bella Contadina Italian Antipasto Mix 600 g / 21 oz | Bella Contadina | $49.77 | 2026-07-26 |
| Chief Duck & Goat Curry Powder 600 g | Chief | $59.70 | 2026-07-22 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Tropicland Frozen Mango Chunks 2.2 kg / 5 lb | Tropicland | $94.95 | G10D03 |
| Crystal Farms Light String Cheese 24 Units 567 g / 1.25 lb | Crystal Farms | $75.95 | G10D03 |
