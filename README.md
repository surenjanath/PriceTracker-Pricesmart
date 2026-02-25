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
- **Total products scraped**: 1171
- **Total value**: $133,428.05
- **Average price**: $113.94

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1169
- **Price changes detected**: 29
- **Stock/availability changes**: 24
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 186 |
|  | 138 |
| Badia | 18 |
| Swiss | 14 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Organic Trail Mix with Cranberries 737 g / 26 oz | Member's Selection | $164.95 | true |
| Royal Asia Honey Walnut Shrimp 907 g / 2 lb | Royal Asia | $169.95 | true |
| SeaPak Garlic Butter Shrimp 680 g / 1.5 lb | SeaPak | $134.95 | true |
| Sacla Hot Sauce for Arrabbiata Pasta with Tomatoes and Chili Peppers / 2 Units / 680 g / 24 oz | Sacla | $102.95 | true |
| Florida's Natural Strawberry Lemonade 2 Units 1.75 L / 59 oz | Florida's Natural | $99.95 | true |
| Carapelli Organic Extra Virgin Olive Oil 880 g / 33.8 oz | Carapelli | $119.95 | true |
| Pringles Honey Mustard, Sour Cream & Onion, and Cheddar Cheese 3-Pack / 158 g / 5.5 oz | Pringles | $79.95 | true |
| Bluewater Farms Cranberry Juice 1.65 L / 56 oz | Bluewater Farms | $59.95 | true |
| General Mills Triple Chex Cereal Mix 1.53 kg / 3 lb | General Mills | $97.95 | true |
| Sara Lee Classic Pound Butter Cake 2 Pack / 453 g / 15.9 oz | Sara Lee | $114.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 999
- **Price increases**: 447
- **Price decreases**: 516
- **Average increase**: 9.8%
- **Average decrease**: -5.1%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | $+48.25 | +497.4% | Increase |
| President Brie Cheese Spreadable 3 Units / 139 g / 4.9 oz | $0.00 | $74.95 | $+74.95 | +100.0% | New |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $222.82 | $226.18 | $+3.36 | +1.5% | Increase |
| Member's Selection Chilled Skinless Boneless Beef Stew, Tray | $137.40 | $137.12 | $-0.28 | -0.2% | Decrease |
| Papaya | $32.92 | $32.86 | $-0.06 | -0.2% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $190.05 | $190.33 | $+0.28 | +0.1% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $84.44 | $84.35 | $-0.09 | -0.1% | Decrease |
| Belgioioso Artigiano Vino Rosso Cheese 453 g / 16 oz | $0.00 | $99.95 | $+99.95 | +100.0% | New |
| Frozen Whole Boneless Pork Tenderloin Vacuum Packaged | $75.86 | $75.73 | $-0.13 | -0.2% | Decrease |
| Pork Belly with Skin Frozen Vacuum Packaged | $193.23 | $193.01 | $-0.22 | -0.1% | Decrease |
| Green pepper | $18.91 | $18.95 | $+0.04 | +0.2% | Increase |
| Fresh Ground Chicken Tray | $107.88 | $107.64 | $-0.24 | -0.2% | Decrease |
| Orchard Orange Juice with Vitamin C 6 Units / 1 L / 33.8 oz | $59.95 | $67.95 | $+8.00 | +13.3% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $154.40 | $155.30 | $+0.90 | +0.6% | Increase |
| Fresh Boneless Beef Eye of Round Whole Piece Vacuum Packaged | $417.51 | $421.08 | $+3.57 | +0.9% | Increase |

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
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Hillshire Farm Ham Mix 3 Units / 454 g / 16 oz | $194.95 | $69.70 | -64.2% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $109.95 | $39.70 | -63.9% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Bella Contadina Capricciosa Italiana Olives and Vegetables in Oil 600 g / 21 oz | Bella Contadina | $49.70 | 2026-02-23 |
| Terra Creta Greek Extra Virgin Olive Oil 500 mL / 16.9 oz | Terra Creta | $79.95 | 2026-02-22 |
| Flavorite Ponche De Crème & Sorrel Ice Cream 2 Units / 1 L / 33.8 oz | Flavorite | $59.70 | 2026-02-18 |
| Ribena Blackcurrant Juice 12 Units / 250 mL | Ribena | $79.95 | 2026-02-18 |
| Montchevre Goat Cheese with Blueberry and Vanilla 298 g / 10.51 oz | Montchevre | $59.95 | 2026-02-18 |
| Mixed Tomato Cherry 907 g / 2 lb |  | $49.95 | 2026-02-18 |
| Orchard Orange Drink 24 Units / 250 mL | Orchard | $89.95 | 2026-02-18 |
| Salmon Fillet with Skin on Boneless Skin Frozen Case |  | $1699.50 | 2026-02-18 |
| Mucci Farms Snack Cucumbers 681 g / 1.5 lb | Mucci Farms | $62.95 | 2026-02-17 |
| Green Cabbage Unit |  | $25.95 | 2026-02-15 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| President Brie Cheese Spreadable 3 Units / 139 g / 4.9 oz | President | $74.95 | G10D03 |
| Belgioioso Artigiano Vino Rosso Cheese 453 g / 16 oz | Belgioioso | $99.95 | G10D03 |
