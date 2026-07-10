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
- **Total products scraped**: 1121
- **Total value**: $125,146.94
- **Average price**: $111.64

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1119
- **Price changes detected**: 25
- **Stock/availability changes**: 7
- **Discontinued products**: 2

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 177 |
|  | 134 |
| Badia | 17 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Freshly Made Assorted Doughnuts 12 Units | Member's Selection | $55.95 | true |
| Member's Selection Freshly Baked Blueberry Mini Muffins 24 Units | Member's Selection | $43.95 | true |
| Member's Selection Freshly Baked Chocolate Chip Cookies 24 Units | Member's Selection | $60.95 | true |
| Member's Selection Small Freshly Baked Croissants 18 Units | Member's Selection | $55.95 | true |
| Member's Selection Freshly Baked Vanilla Cake 40 to 50 Slices | Member's Selection | $198.95 | true |
| Member's Selection Fresh Baked Vanilla Cake 20 to 24 Slices | Member's Selection | $102.95 | true |
| Member's Selection Fresh Baked Cheesecake 15 to 20 Slices | Member's Selection | $206.95 | true |
| Member's Selection Vanilla Chocolate Cake Freshly Baked 20 to 25 Slices | Member's Selection | $102.95 | true |
| Member's Selection Freshly Baked Black Forest Cake 10 to 12 Slices | Member's Selection | $139.95 | true |
| Member's Selection Freshly Baked Oatmeal Cookies 24 Units | Member's Selection | $60.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1027
- **Price increases**: 524
- **Price decreases**: 472
- **Average increase**: 6.6%
- **Average decrease**: -5.3%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Stamina Energy Drink Assorted Flavors 12 Units / 330 mL | $53.95 | $48.70 | $-5.25 | -9.7% | Decrease |
| Munchy's Krunch Oat Cookies with Dark Chocolate and Cranberries 3 Units / 208 g / 7.3 oz | $0.00 | $49.95 | $+49.95 | +100.0% | New |
| Chilled Chicken Gizzard Tray Pack | $44.58 | $44.30 | $-0.28 | -0.6% | Decrease |
| Papaya | $39.49 | $39.40 | $-0.09 | -0.2% | Decrease |
| Erin Farm Salami Stick 1 kg / 2.2 lb | $47.95 | $52.95 | $+5.00 | +10.4% | Increase |
| Ginger 1 kg / 2.2 lb | $0.00 | $24.95 | $+24.95 | +100.0% | New |
| Ribeye Choice Fillet Fresh Tray | $309.08 | $308.34 | $-0.74 | -0.2% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $117.59 | $117.41 | $-0.18 | -0.2% | Decrease |
| Fresh Bone-in Chicken Thighs Tray | $67.63 | $67.70 | $+0.07 | +0.1% | Increase |
| Frozen Bone In Pork Shoulder Sliced Tray | $71.43 | $71.33 | $-0.10 | -0.1% | Decrease |
| Member's Selection Frozen Boneless Pork Butt Stew Tray | $79.30 | $90.46 | $+11.16 | +14.1% | Increase |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $193.76 | $193.47 | $-0.29 | -0.1% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $160.68 | $159.67 | $-1.01 | -0.6% | Decrease |
| Fresh Chicken Breast Bone In Tray | $92.06 | $92.15 | $+0.09 | +0.1% | Increase |
| Fresh Chicken Mixed Parts Tray | $83.22 | $83.32 | $+0.10 | +0.1% | Increase |

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
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Maeva BIO Organic Extra Virgin Olive Oil Spray 2 Units / 200 mL / 6.7 oz | Maeva | $59.95 | 2026-07-09 |
| Tomato 11.3 kg / 25 lb |  | $259.95 | 2026-07-09 |
| Lush Natural Refreshing Apple Flavored Drink 36 Units / 200 ml | Lush | $79.70 | 2026-07-08 |
| Macfoods Roast Boneless Pork Belly, 1 kg / 2.2 lb | Macfoods | $79.95 | 2026-07-08 |
| Mixed Pepper Box 9 kg / 20 lb |  | $249.95 | 2026-07-07 |
| Member's Selection Freshly Baked Sweet and Creamy Vanilla Cake 80 to 100 Slices | Member's Selection | $399.95 | 2026-07-07 |
| Ocean Spray Cran Tropical Juices in Assorted Flavors with Vitamin C 24 Units / 295 mL / 10 oz | Ocean Spray | $179.95 | 2026-07-06 |
| Fruit Roll Ups Assorted Fruit Rolls 72 Units / 14 g | Fruit Roll-Ups | $174.70 | 2026-07-05 |
| Califia Farms Strawberry and Coconut Beverage 1.4 L / 48 oz | Califia Farms | $54.95 | 2026-07-05 |
| Riceworks Sea Salt Sesame Chips 454 g / 16 oz | Riceworks | $84.95 | 2026-07-04 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Munchy's Krunch Oat Cookies with Dark Chocolate and Cranberries 3 Units / 208 g / 7.3 oz | Munchy's | $49.95 | G10D03 |
| Ginger 1 kg / 2.2 lb |  | $24.95 | G10D03 |
