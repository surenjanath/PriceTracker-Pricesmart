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
- **Total products scraped**: 1152
- **Total value**: $129,298.32
- **Average price**: $112.24

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1151
- **Price changes detected**: 43
- **Stock/availability changes**: 10
- **Discontinued products**: 2

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 187 |
|  | 132 |
| Badia | 18 |
| Swiss | 14 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Just About Foods Organic and Creamy Peanut Butter 1.13 kg / 40 oz | Just About Foods | $97.95 | true |
| Bob's Red Mill Oatmeal with Protein 1.81 kg / 4 lb | Bob's Red Mill | $144.95 | true |
| Izzio Artisan Naturally Fermented Sourdough Bread Sliced | Izzio | $49.95 | true |
| Coffee Toppers Salted Caramel Whipped Cream 2 Units / 425 g / 15 oz | Coffee Toppers | $79.95 | true |
| Swiss Miss Sugar-free Cocoa 60 Units / 20 g / 0.7 oz | Swiss Miss | $109.95 | true |
| Trevijano Thai Style Cous Cous Rice 800 g / 28.2 oz | Trevijano | $75.95 | true |
| Izzio Artisanal Sourdough Focaccia Bread with Rosemary, Garlic, and Olive Oil Ready to Bake | Izzio | $39.95 | true |
| Terra Creta Extra Virgin Olive Oil in Marasca 1 L / 33.81 oz | Terra Creta | $134.95 | true |
| Galvanina Lemon Flavor Sparkling Mineral Water 24 Units / 500 mL / 16.9 oz | Galvanina | $169.95 | true |
| Copper Kettle Dark Chocolate Truffles with Sea Salt 448 g / 16 oz | Copper Kettle | $139.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 961
- **Price increases**: 431
- **Price decreases**: 496
- **Average increase**: 10.6%
- **Average decrease**: -6.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Plum 907 g / 2 lb | $77.95 | $82.95 | $+5.00 | +6.4% | Increase |
| Peach 908 g / 2 lb | $59.95 | $79.95 | $+20.00 | +33.4% | Increase |
| Molinaro's Organic Pizza Starter Kit 2 Units 380 g / 13.4 oz | $64.95 | $66.95 | $+2.00 | +3.1% | Increase |
| Hillshire Farm Ham Mix 3 Units / 454 g / 16 oz | $69.70 | $194.95 | $+125.25 | +179.7% | Increase |
| Green Seedless Grapes 907 g / 2 lb | $69.95 | $99.95 | $+30.00 | +42.9% | Increase |
| Pringles Honey Mustard, Sour Cream & Onion, and Cheddar Cheese 3-Pack / 158 g / 5.5 oz | $0.00 | $79.95 | $+79.95 | +100.0% | New |
| Frozen Pork Belly Skin On Sliced Tray  | $110.83 | $111.07 | $+0.24 | +0.2% | Increase |
| Nectarine 908 g / 2 lb | $72.95 | $69.95 | $-3.00 | -4.1% | Decrease |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $230.71 | $231.30 | $+0.59 | +0.3% | Increase |
| Papaya | $31.80 | $31.74 | $-0.06 | -0.2% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $194.70 | $195.29 | $+0.59 | +0.3% | Increase |
| Badia All Purpose Marinade Seasoning 591 mL / 20 oz  | $20.95 | $22.95 | $+2.00 | +9.5% | Increase |
| Fresh Chicken Breast Bone In Tray | $97.34 | $97.24 | $-0.10 | -0.1% | Decrease |
| Fresh Chicken Mixed Parts Tray | $92.76 | $92.87 | $+0.11 | +0.1% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $152.67 | $152.36 | $-0.31 | -0.2% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $29.70 | $89.95 | +202.9% |
| Hillshire Farm Ham Mix 3 Units / 454 g / 16 oz | $69.70 | $194.95 | +179.7% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $34.70 | $89.95 | +159.2% |
| Cherries | $31.92 | $73.05 | +128.9% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Hillshire Farm Ham Mix 3 Units / 454 g / 16 oz | $194.95 | $69.70 | -64.2% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $109.95 | $39.70 | -63.9% |
| Pop-Tarts Snack Crunchy Poppers Filled with Strawberry and Brownie 2 Units 360 g / 12.6 oz  | $174.95 | $64.70 | -63.0% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $34.70 | -61.4% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Gouda Cheese Block |  | $85.48 | 2026-01-22 |
| Swift Frozen Pork Ribs Kansas City Style BBQ Vacuum Packing | Swift | $1169.78 | 2026-01-22 |
| Prunes 1 kg / 2.2 lb |  | $29.70 | 2026-01-21 |
| Orchard Orange Drink 24 Units / 250 mL | Orchard | $85.95 | 2026-01-21 |
| Currants 1 kg / 2.2 lb |  | $29.70 | 2026-01-20 |
| Terra Real Vegetable Chips 425 g / 15 oz | Terra | $82.95 | 2026-01-19 |
| Sunny Fruits Organic Dried Apricots 10 Units / 50 g / 1.76 oz | Sunny Fruits | $59.95 | 2026-01-19 |
| Lipton Yellow Label Tea 2 Packs / 100 Units / 2 g | Lipton | $119.95 | 2026-01-19 |
| Red Rose Pink Salmon 3 Units / 418 g | Red Rose | $125.95 | 2026-01-18 |
| Member's Selection Freshly Made Chicken Salad Wraps 4 Units | Member's Selection | $65.95 | 2026-01-18 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Pringles Honey Mustard, Sour Cream & Onion, and Cheddar Cheese 3-Pack / 158 g / 5.5 oz | Pringles | $79.95 | G10D03 |
