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
- **Total products scraped**: 1151
- **Total value**: $127,275.77
- **Average price**: $110.58

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1151
- **Price changes detected**: 19
- **Stock/availability changes**: 5
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 186 |
|  | 136 |
| Badia | 19 |
| Swiss | 14 |
| Nestle | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Happy Village Organic Fig and Nut Mini Bars 24 Units / 20 g / 0.7 oz | Happy Village | $146.95 | true |
| Maeva Extra Virgin Olive Oil Spray 2 Units / 400 mL / 13.5 oz | Maeva | $94.95 | true |
| President Brie Cheese Spreadable 3 Units / 139 g / 4.9 oz | President | $74.95 | true |
| Bussetto Prosciutto Classico 189 g / 7 oz | Bussetto | $164.95 | true |
| Badia Parsley Flakes 85 g / 3 oz | Badia | $24.95 | true |
| Pan White Corn Meal Flour 2 Units / 1 kg | Pan | $34.95 | true |
| Belgioioso Artigiano Vino Rosso Cheese 453 g / 16 oz | Belgioioso | $99.95 | true |
| Kashi Strawberry Banana Multi-Grain Cereal 720 g / 25.4 oz | Kashi | $97.95 | true |
| Morning Star Farms Sausage Links Plant-Based 2 Units 225 g / 8 oz  | MorningStar Farms | $124.95 | true |
| Wellsley Farms Crab Cakes 510 g / 1 lb | Wellsley Farms | $219.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1071
- **Price increases**: 480
- **Price decreases**: 552
- **Average increase**: 9.3%
- **Average decrease**: -5.4%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $186.47 | $186.19 | $-0.28 | -0.2% | Decrease |
| Fresh Beef Ribeye Steak Vacuum Packed | $235.16 | $246.08 | $+10.92 | +4.6% | Increase |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $229.68 | $228.61 | $-1.07 | -0.5% | Decrease |
| Member's Selection Chilled Skinless Boneless Beef Stew, Tray | $137.40 | $136.57 | $-0.83 | -0.6% | Decrease |
| Ribeye Choice Fillet Fresh Tray | $264.13 | $285.06 | $+20.93 | +7.9% | Increase |
| Pork Belly with Skin Frozen Vacuum Packaged | $193.01 | $192.37 | $-0.64 | -0.3% | Decrease |
| Frozen Whole Boneless Pork Tenderloin Vacuum Packaged | $74.69 | $74.82 | $+0.13 | +0.2% | Increase |
| Fresh Chicken Leg Quarters Tray | $90.71 | $90.81 | $+0.10 | +0.1% | Increase |
| Fresh Chicken Breast Bone In Tray | $92.83 | $93.02 | $+0.19 | +0.2% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $108.66 | $108.35 | $-0.31 | -0.3% | Decrease |
| Fresh Ground Chicken Tray | $101.39 | $101.87 | $+0.48 | +0.5% | Increase |
| Nutrina Chilled Whole Chicken Bag | $312.83 | $313.43 | $+0.60 | +0.2% | Increase |
| Carnation Evaporated Milk 6 Units / 371 mL / 12.5 oz | $71.95 | $55.95 | $-16.00 | -22.2% | Decrease |
| Swift Frozen Chilled Pork Ribs Kansas City Style BBQ Vacuum Pack  | $160.11 | $162.42 | $+2.31 | +1.4% | Increase |
| Nestle Sweetened Condensed Milk 6 Pack / 395 g / 14 oz | $89.95 | $76.95 | $-13.00 | -14.5% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Carrot 2.27 kg / 5 lb | $9.70 | $37.95 | +291.2% |
| Silk Unsweetened Original 2 Units 1.89 L / 64 oz | $29.70 | $99.95 | +236.5% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Green pepper | $49.48 | $16.93 | -65.8% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Curly's Baby Back Pork Ribs 680 g / 24 oz | Curly's | $134.95 | 2026-03-09 |
| San Pellegrino Sparkling Mineral Water 6 Units / 250 mL / 8.45 oz | San Pellegrino | $59.70 | 2026-03-08 |
| Orchard Orange Drink 24 Units / 200 mL / 6.7 oz | Orchard | $67.95 | 2026-03-08 |
| Thinsters Chocolate Chip Cookies 454 g / 16 oz | Thinsters | $79.95 | 2026-03-08 |
| Cheetos Puffs Snack Cheese Flavor 255 g / 9 oz | Cheetos | $24.95 | 2026-03-08 |
| Reny Picot Brie with Peppercorns 396 g /14 oz | Reny Picot | $69.95 | 2026-03-08 |
| Member's Selection Freshly Baked Sweet and Creamy Vanilla Cake 80 to 100 Slices | Member's Selection | $399.95 | 2026-03-08 |
| Frozen Chicken Legs 1 kg / 2.2 lb |  | $39.95 | 2026-03-08 |
| Member's Selection Freshly Baked Berries Cake 12 Slices | Member's Selection | $139.95 | 2026-03-07 |
| Member's Selection Cookies and Cream Cake Decorated with Oreo Cookie 12 Slices | Member's Selection | $139.95 | 2026-03-07 |

## New Products Added Today
No new products added today.
