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
- **Total products scraped**: 1166
- **Total value**: $130,253.55
- **Average price**: $111.71

## Database Changes
- **New products added**: 3
- **Existing products updated**: 1163
- **Price changes detected**: 67
- **Stock/availability changes**: 14
- **Discontinued products**: 4

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 176 |
|  | 146 |
| Swiss | 15 |
| Badia | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Sincerely Brigitte Assorted Cheese Set 495 g / 17.5 oz | Sincerely  Brigitte | $124.95 | true |
| Zalea Gourmet Sliced Peaches in Light Syrup 2 Unidades / 425 g / 15 oz | Zalea Gourmet | $56.95 | true |
| Member's Selection Frozen Boneless Salmon Portions with Skin 680 g / 1.5 lb | Member's Selection | $179.95 | true |
| Member's Selection Tuna in Water 6 Units / 136 g / 6 oz | Member's Selection | $65.95 | true |
| Member's Selection Premium Smoked Turkey Breast 2 Units / 340 g / 12 oz | Member's Selection | $107.95 | true |
| Member's Selection Cold Extracted Extra Virgin Olive Oil 2 L | Member's Selection | $149.95 | true |
| Member's Selection Premium Turkey Breast 2 Units / 340 g / 12 oz | Member's Selection | $107.95 | true |
| Blueberries 508 g / 1.12 lb |  | $99.95 | true |
| Member Selection String Cheese 24 Units / 28 g / 0.9 oz | Member's Selection | $63.95 | true |
| Member’s Selection Breaded Mozzarella Sticks 2.04 kg / 4.5 lb | Member's Selection | $159.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1133
- **Price increases**: 662
- **Price decreases**: 431
- **Average increase**: 6.6%
- **Average decrease**: -4.4%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Sara Lee Classic Pound Butter Cake 2 Pack / 453 g / 15.9 oz | $29.70 | $114.95 | $+85.25 | +287.0% | Increase |
| Miami Beef Beef Patties 40 / 113.5 g / 4 oz | $324.95 | $327.95 | $+3.00 | +0.9% | Increase |
| Nesquik Chocolate Powder Mix 1.27 kg / 2.8 lb | $89.95 | $99.95 | $+10.00 | +11.1% | Increase |
| Member's Selection Shredded Mozzarella Cheese 2.26 kg / 5 lb | $122.95 | $124.95 | $+2.00 | +1.6% | Increase |
| Nescafé Classic Instant Soluble Coffee 170 g + Cup | $0.00 | $63.95 | $+63.95 | +100.0% | New |
| Creamery Novelties Ice Cream Punch de Créme 3.78 L / 1 gal | $0.00 | $72.95 | $+72.95 | +100.0% | New |
| Frozen Bone-In Goat Carcass Case | $1246.51 | $1308.06 | $+61.55 | +4.9% | Increase |
| Snickers, M&M's, Skittles and Starburst Chocolates and Confectionery Assorted Jumbo Pack 895.6 g / 31.59 oz | $0.00 | $154.95 | $+154.95 | +100.0% | New |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $147.82 | $148.16 | $+0.34 | +0.2% | Increase |
| Frozen Sliced Turkey Drumsticks | $143.86 | $143.46 | $-0.40 | -0.3% | Decrease |
| Mandarin Orange Chicken 1.2 kg / 2.6 lb | $184.95 | $187.95 | $+3.00 | +1.6% | Increase |
| Frozen Sliced Baby Back Ribs | $156.26 | $186.37 | $+30.11 | +19.3% | Increase |
| Sweet Craft Dolceria Ube Cheesecake 6 Pack 113.4 g / 4 oz | $187.95 | $182.95 | $-5.00 | -2.7% | Decrease |
| Papaya | $38.89 | $38.76 | $-0.13 | -0.3% | Decrease |
| Fresh Whole Chicken 2 Units | $104.85 | $104.68 | $-0.17 | -0.2% | Decrease |

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
| Smithfield Smoked and Caramelized Pork Shoulder Cubes 453 g / 1 lb | $177.95 | $44.70 | -74.9% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Member's Selection Extra Virgin Olive Oil 750 mL / 25.36 oz | Member's Selection | $69.95 | 2026-09-30 |
| Welch's Sparkling Rose Non-Alcoholic 3 Units / 750 mL | Welch's | $79.70 | 2026-09-30 |
| Sacla Italia Pizza Sauce 1 kg / 35.2 oz | Sacla | $44.70 | 2026-09-30 |
| Member's Selection Frozen Boneless Pork Loin Steak Tray | Member's Selection | $82.24 | 2026-09-30 |
| Pan White Corn Meal Flour 2 Units / 1 kg | Pan | $34.95 | 2026-09-29 |
| Member's Selection Freshly Prepared Chicken Salad | Member's Selection | $99.95 | 2026-09-29 |
| Cadbury Delicious Milk Chocolate Bar 180 g       | Cadbury | $57.95 | 2026-09-28 |
| Ocean Delight Frozen Octopus 907 g / 2 lb | Ocean Delight | $98.95 | 2026-09-27 |
| Badia Spice with Lime Pepper Flavor 680.4 g / 24 oz | Badia | $59.70 | 2026-09-27 |
| Frozen Bone-In Pork Loin Case |  | $1551.85 | 2026-09-27 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Nescafé Classic Instant Soluble Coffee 170 g + Cup | Nescafé | $63.95 | G10D03 |
| Creamery Novelties Ice Cream Punch de Créme 3.78 L / 1 gal | Creamery Novelties | $72.95 | G10D03 |
| Snickers, M&M's, Skittles and Starburst Chocolates and Confectionery Assorted Jumbo Pack 895.6 g / 31.59 oz | Snickers | $154.95 | G10D03 |
