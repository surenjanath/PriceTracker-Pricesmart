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
- **Total products scraped**: 1145
- **Total value**: $126,319.98
- **Average price**: $110.32

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1143
- **Price changes detected**: 47
- **Stock/availability changes**: 15
- **Discontinued products**: 2

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 176 |
|  | 141 |
| Badia | 15 |
| Swiss | 15 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Riceworks Avocado Chips 453 g / 16 oz | Riceworks | $92.95 | true |
| Chobani Lactose Free Yogurt Drink with 20 g Protein 12 Units / 283 g / 10 oz | Chobani | $234.95 | true |
| Bigelow Vanilla Chai Tea 60 Bags / 139 g | Bigelow | $94.95 | true |
| Member's Selection Freshly Baked Sliced Butter Brioche Bread | Member's Selection | $66.95 | true |
| Crystal Farms Light String Cheese 24 Units 567 g / 1.25 lb | Crystal Farms | $75.95 | true |
| Garofalo Fusilli & Farfalle Pasta Variety Pack 4 Units / 500 g / 1.1 lb | Garofalo | $97.95 | true |
| Bella Contadina Garlic with Green Pesto 330 g / 11.7 oz | Bella Contadina | $72.95 | true |
| Fruta Assorted Flavor Juice Boxes 24 Units / 200 mL / 6.8 oz | Fruta | $69.95 | true |
| Smithfield Smoked and Caramelized Pork Shoulder Cubes 453 g / 1 lb | Smithfield | $177.95 | true |
| POM Pomegranate Juice 1.4 L / 48 oz | POM | $107.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1088
- **Price increases**: 594
- **Price decreases**: 452
- **Average increase**: 7.7%
- **Average decrease**: -5.2%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Melissa's Black Mission Figs 227 g / 8. oz | $42.95 | $64.95 | $+22.00 | +51.2% | Increase |
| Mini Sweet Peppers 454 g / 1 lb | $47.95 | $54.95 | $+7.00 | +14.6% | Increase |
| Nectarine 908 g / 2 lb | $77.95 | $79.95 | $+2.00 | +2.6% | Increase |
| Peach 908 g / 2 lb | $62.95 | $67.95 | $+5.00 | +7.9% | Increase |
| Cauliflower 1 Unit | $37.95 | $59.95 | $+22.00 | +58.0% | Increase |
| Golden Kiwi 1 lb / 453 g | $77.95 | $79.95 | $+2.00 | +2.6% | Increase |
| Romaine Lettuce Hearts 3 Units | $39.95 | $42.95 | $+3.00 | +7.5% | Increase |
| Plum 907 g / 2 lb | $67.95 | $69.95 | $+2.00 | +2.9% | Increase |
| Blueberries 508 g / 1.12 lb | $79.95 | $89.95 | $+10.00 | +12.5% | Increase |
| Frozen Bone-In Goat Carcass Case | $1372.42 | $1246.51 | $-125.91 | -9.2% | Decrease |
| Member's Selection Low-Moisture Part-Skim Shredded Mozzarella Cheese 2.2 kg / 5 lb | $0.00 | $119.95 | $+119.95 | +100.0% | New |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $241.03 | $240.75 | $-0.28 | -0.1% | Decrease |
| Ocean Spray Sparkling Cranberry Juice Canned Soda 4 Units / 340 mL / 11.5 oz | $0.00 | $49.95 | $+49.95 | +100.0% | New |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $129.58 | $129.74 | $+0.16 | +0.1% | Increase |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $199.16 | $198.87 | $-0.29 | -0.1% | Decrease |

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
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Cultured Cravings Coconut Yogurt 12 Units / 150 g / 5.3 oz | $229.95 | $59.70 | -74.0% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Nonni's Almond and Cranberry Cookies 575 g / 1.26 lb | Nonni's | $129.95 | 2026-09-17 |
| Sincerely Brgitte Cheese with Truffle 453 g / 1.1 lb | Sincerely  Brigitte | $79.95 | 2026-09-17 |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | Garcia | $44.95 | 2026-09-16 |
| Badia All Purpose Marinade Seasoning 591 mL / 20 oz  | Badia | $12.70 | 2026-09-16 |
| Brunswick Canned Mackerel in Oil 3 Units / 225 g / 7.9 oz | Brunswick | $34.95 | 2026-09-16 |
| Bombolo Biscotti Mini Tartlets Filled with Sweet Wild Berry and Vanilla Flavor | Bombolo Biscotti | $64.95 | 2026-09-16 |
| Philadelphia Salmon Cream Cheese 2 Units / 212 g / 7.5 oz | Philadelphia | $82.95 | 2026-09-15 |
| Member's Selection Freshly Baked Sweet and Creamy Vanilla Cake 80 to 100 Slices | Member's Selection | $399.95 | 2026-09-15 |
| YoguRico Strawberry Low Fat Drinkable Yogurt  1.68 L / 57 oz | YoguRico | $54.95 | 2026-09-15 |
| Ocean Spray Cranberry Juice 2 Units / 2.83 L / 96 oz  | Ocean Spray | $79.70 | 2026-09-15 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Member's Selection Low-Moisture Part-Skim Shredded Mozzarella Cheese 2.2 kg / 5 lb | Member's Selection | $119.95 | G10D03 |
| Ocean Spray Sparkling Cranberry Juice Canned Soda 4 Units / 340 mL / 11.5 oz | Ocean Spray | $49.95 | G10D03 |
