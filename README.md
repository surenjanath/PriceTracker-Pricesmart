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
- **Total value**: $125,251.40
- **Average price**: $112.53

## Database Changes
- **New products added**: 3
- **Existing products updated**: 1110
- **Price changes detected**: 22
- **Stock/availability changes**: 17
- **Discontinued products**: 2

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 174 |
|  | 134 |
| Badia | 16 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Terra Delyssa Mild Extra Virgin Olive Oil 1 L / 34 oz | Terra Delyssa | $84.95 | true |
| Maeva Avocado Oil Spray 2 Units / 200 mL / 6.7 oz | Maeva | $89.95 | true |
| Ocean Spray Cranberry Juice 2 Units 1.89 L / 64 oz | Ocean Spray | $77.95 | true |
| McCain Cassava Sticks 997 g / 2.2 lb | McCain | $44.95 | true |
| Cultured Cravings Coconut Yogurt 12 Units / 150 g / 5.3 oz | Cultured Cravings | $99.70 | true |
| Oikos Greek Yogurt 18 Units / 150 g / 5.3 oz | Oikos | $194.95 | true |
| Tropicland Frozen Mango Chunks 2.2 kg / 5 lb | Tropicland | $94.95 | true |
| Munchies Flamin' Hot Flavored Snack Mix 262.2 g / 9.25 oz | Munchies | $44.95 | true |
| Charles Chocolate Assorted Chocolate Snack Pack 30 Units | Charles Chocolates | $59.95 | true |
| Pepsi Zero Sugar Soft Drink 12 Units / 500 mL / 17 oz | Pepsi | $39.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1069
- **Price increases**: 523
- **Price decreases**: 513
- **Average increase**: 6.0%
- **Average decrease**: -5.8%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Table Foods Stuffed Peppers Variety 504 g / 18 oz | $0.00 | $116.95 | $+116.95 | +100.0% | New |
| Leclerc Tradition 1905 French Creme and Raspberry Filled Cookies 2 Units / 300 g | $0.00 | $49.95 | $+49.95 | +100.0% | New |
| Lee Kum Kee Traditional Soy Sauce for Cooking and Marinating 2 Units / 500 mL | $0.00 | $39.95 | $+39.95 | +100.0% | New |
| Seedless Watermelon  | $74.95 | $96.95 | $+22.00 | +29.4% | Increase |
| Papaya | $38.41 | $38.50 | $+0.09 | +0.2% | Increase |
| Mini Sweet Peppers 454 g / 1 lb | $59.95 | $57.95 | $-2.00 | -3.3% | Decrease |
| Plum 907 g / 2 lb | $59.95 | $62.95 | $+3.00 | +5.0% | Increase |
| Ribeye Choice Fillet Fresh Tray | $324.13 | $319.51 | $-4.62 | -1.4% | Decrease |
| Frozen Lamb Shoulder Chops Tray | $123.95 | $124.13 | $+0.18 | +0.1% | Increase |
| Fresh Chicken Thighs Boneless Tray | $90.15 | $90.02 | $-0.13 | -0.1% | Decrease |
| Fresh Kiwi 453 g / 1 lb | $49.95 | $54.95 | $+5.00 | +10.0% | Increase |
| Fresh Seasoned BBQ Chicken Quarters Bag | $93.00 | $93.05 | $+0.05 | +0.1% | Increase |
| Bosc Pear 1.36 kg / 3 lb | $76.95 | $79.95 | $+3.00 | +3.9% | Increase |
| Fresh Chicken Mixed Parts Tray | $83.22 | $83.12 | $-0.10 | -0.1% | Decrease |
| Frozen Bone In Pork Shoulder Sliced Tray | $71.38 | $71.28 | $-0.10 | -0.1% | Decrease |

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
| Molinaro's Organic Pizza Starter Kit 2 Units 380 g / 13.4 oz | Molinaro's | $66.95 | 2026-08-14 |
| Bagelmania Artisanal Simple Bagel Bread 6 Units | Bagelmania | $34.95 | 2026-08-14 |
| Pier 33 Wild Yellowfin Tuna Steak 397 g / 14 oz | Pier 33 | $109.95 | 2026-08-13 |
| Bombolo Biscotti Baked Cookies Decorated for Easter with Assorted Designs | Bombolo Biscotti | $74.95 | 2026-08-13 |
| Member's Selection Freshly Made Chicken Salad Wraps 4 Units | Member's Selection | $62.95 | 2026-08-13 |
| Member's Selection Ready-to-Eat Tuna Salad 907 g / 2 lb | Member's Selection | $79.95 | 2026-08-13 |
| Campoverde Spinach, Mango, Apple and Pineapple Mix 907 g / 2 lb | Campoverde | $112.95 | 2026-08-12 |
| KFI Gluten-Free Curry and Coconut Sauce 2 Units / 695 g | KFI | $69.70 | 2026-08-12 |
| Samyang Four Cheese and Ramen Flavor Instant Noodle Soup 5 Units / 140 g | Samyang | $62.95 | 2026-08-12 |
| Crystal Farms Light String Cheese 24 Units 567 g / 1.25 lb | Crystal Farms | $75.95 | 2026-08-10 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Table Foods Stuffed Peppers Variety 504 g / 18 oz | Table Foods | $116.95 | G10D03 |
| Leclerc Tradition 1905 French Creme and Raspberry Filled Cookies 2 Units / 300 g | Leclerc | $49.95 | G10D03 |
| Lee Kum Kee Traditional Soy Sauce for Cooking and Marinating 2 Units / 500 mL | Lee Kum Kee | $39.95 | G10D03 |
