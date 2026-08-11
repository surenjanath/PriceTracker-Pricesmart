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
- **Total products scraped**: 1116
- **Total value**: $124,177.87
- **Average price**: $111.27

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1114
- **Price changes detected**: 30
- **Stock/availability changes**: 21
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 176 |
|  | 133 |
| Badia | 16 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Terra Delyssa Mild Extra Virgin Olive Oil 1 L / 34 oz | Terra Delyssa | $84.95 | true |
| Maeva Avocado Oil Spray 2 Units / 200 mL / 6.7 oz | Maeva | $89.95 | true |
| McCain Cassava Sticks 997 g / 2.2 lb | McCain | $43.95 | true |
| Ocean Spray Cranberry Juice 2 Units 1.89 L / 64 oz | Ocean Spray | $77.95 | true |
| Cultured Cravings Coconut Yogurt 12 Units / 150 g / 5.3 oz | Cultured Cravings | $229.95 | true |
| Oikos Greek Yogurt 18 Units / 150 g / 5.3 oz | Oikos | $194.95 | true |
| Tropicland Frozen Mango Chunks 2.2 kg / 5 lb | Tropicland | $94.95 | true |
| Munchies Flamin' Hot Flavored Snack Mix 262.2 g / 9.25 oz | Munchies | $44.95 | true |
| Pepsi Zero Sugar Soft Drink 12 Units / 500 mL / 17 oz | Pepsi | $39.95 | true |
| Charles Chocolate Assorted Chocolate Snack Pack 30 Units | Charles Chocolates | $59.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1067
- **Price increases**: 537
- **Price decreases**: 503
- **Average increase**: 5.9%
- **Average decrease**: -5.4%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Papaya | $38.92 | $38.66 | $-0.26 | -0.7% | Decrease |
| Anthon Berg Baileys Chocolate-Covered Marzipan with Baileys Liqueur 20 Count / 25 g / 0.8 oz | $0.00 | $149.95 | $+149.95 | +100.0% | New |
| Member's Selection Frozen Sliced Turkey Wings, Bag | $161.15 | $160.55 | $-0.60 | -0.4% | Decrease |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $246.73 | $245.87 | $-0.86 | -0.3% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $200.73 | $200.15 | $-0.58 | -0.3% | Decrease |
| Frozen Sliced Turkey Drumsticks | $193.49 | $194.42 | $+0.93 | +0.5% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $69.94 | $70.00 | $+0.06 | +0.1% | Increase |
| Reny Picot Camembert Cheese 397 g / 14 oz | $49.70 | $69.95 | $+20.25 | +40.7% | Increase |
| Better Living Nuts, Seeds and Dehydrated Fruit Mix 1.3 kg | $79.95 | $87.95 | $+8.00 | +10.0% | Increase |
| Eve Dried Pigeon Peas 6 Units / 400 g / 14 oz | $49.95 | $52.95 | $+3.00 | +6.0% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $149.17 | $148.49 | $-0.68 | -0.5% | Decrease |
| Fresh Boneless Beef Eye of Round Whole Piece Vacuum Packaged | $446.36 | $453.97 | $+7.61 | +1.7% | Increase |
| Frozen Lamb Shoulder Chops Tray | $124.31 | $124.13 | $-0.18 | -0.1% | Decrease |
| Fresh Chicken Thighs Boneless Bag | $338.96 | $339.32 | $+0.36 | +0.1% | Increase |
| Fresh Ground Chicken Tray | $100.97 | $100.85 | $-0.12 | -0.1% | Decrease |

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
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Crystal Farms Light String Cheese 24 Units 567 g / 1.25 lb | Crystal Farms | $75.95 | 2026-08-10 |
| Red Rose Canned Pink Salmon in Water 2 Units / 418 g / 14.7 oz | Red Rose | $72.95 | 2026-08-09 |
| Mowi Lightly Smoked Salmon 680 g / 1.5 lb | Mowi | $214.95 | 2026-08-09 |
| Charles Chocolate Coated Jordanian Almond 1 kg / 2.2 lb | Charles Chocolates | $29.70 | 2026-08-09 |
| Idahoan Classic Instant Mashed Potatoes 1.47 kg / 3.25 lb | Idahoan | $49.70 | 2026-08-09 |
| The Baking Café Cross Buns 6 Units / 70 g / 0.15 lb | The Baking Café | $36.95 | 2026-08-09 |
| Florida's Natural Strawberry Lemonade 2 Units 1.75 L / 59 oz | Florida's Natural | $114.95 | 2026-08-08 |
| Member's Selection Mayonnaise 12 Units / 591 mL / 20 oz | Member's Selection | $199.95 | 2026-08-08 |
| Mowi Tuscan Frozen Herb Salmon Portions 710 g / 1.56 lb | Mowi | $194.95 | 2026-08-06 |
| Garden Foods Mixed Vegetables 1.36 kg / 3 lb | Garden Foods | $54.95 | 2026-08-05 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Anthon Berg Baileys Chocolate-Covered Marzipan with Baileys Liqueur 20 Count / 25 g / 0.8 oz | Anthon Berg | $149.95 | G10D03 |
|  Chobani Greek Yogurt Plain 1.13 kg / 2.5 lb | Chobani | $78.95 | G10D03 |
