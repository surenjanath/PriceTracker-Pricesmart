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
- **Total products scraped**: 1153
- **Total value**: $131,854.78
- **Average price**: $114.36

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1151
- **Price changes detected**: 48
- **Stock/availability changes**: 15
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 186 |
|  | 133 |
| Badia | 18 |
| Swiss | 14 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Bob's Red Mill Oatmeal with Protein 1.81 kg / 4 lb | Bob's Red Mill | $144.95 | true |
| Just About Foods Organic and Creamy Peanut Butter 1.13 kg / 40 oz | Just About Foods | $97.95 | true |
| Swiss Miss Sugar-free Cocoa 60 Units / 20 g / 0.7 oz | Swiss Miss | $109.95 | true |
| Izzio Artisan Naturally Fermented Sourdough Bread Sliced | Izzio | $49.95 | true |
| Trevijano Thai Style Cous Cous Rice 800 g / 28.2 oz | Trevijano | $75.95 | true |
| YoguRico Strawberry Low Fat Drinkable Yogurt  1.68 L / 57 oz | YoguRico | $54.95 | true |
| Coffee Toppers Salted Caramel Whipped Cream 2 Units / 425 g / 15 oz | Coffee Toppers | $79.95 | true |
| Terra Creta Extra Virgin Olive Oil in Marasca 1 L / 33.81 oz | Terra Creta | $134.95 | true |
| Izzio Artisanal Sourdough Focaccia Bread with Rosemary, Garlic, and Olive Oil Ready to Bake | Izzio | $39.95 | true |
| Copper Kettle Dark Chocolate Truffles with Sea Salt 448 g / 16 oz | Copper Kettle | $139.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1052
- **Price increases**: 522
- **Price decreases**: 493
- **Average increase**: 8.6%
- **Average decrease**: -6.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Mixed Pepper Box 9 kg / 20 lb | $229.95 | $249.95 | $+20.00 | +8.7% | Increase |
| Nectarine 908 g / 2 lb | $59.95 | $72.95 | $+13.00 | +21.7% | Increase |
| Currants 1 kg / 2.2 lb | $59.95 | $29.70 | $-30.25 | -50.5% | Decrease |
| Fresh Strawberry 454 g / 1 lb | $39.95 | $34.95 | $-5.00 | -12.5% | Decrease |
| Cherries 454 g / 1 lb | $82.95 | $69.95 | $-13.00 | -15.7% | Decrease |
| Rastelli's Ribeye Steak 2 Units 225 g / 8 oz | $0.00 | $129.95 | $+129.95 | +100.0% | New |
| Frozen Pork Belly Skin On Sliced Tray  | $110.35 | $109.87 | $-0.48 | -0.4% | Decrease |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $240.78 | $242.32 | $+1.54 | +0.6% | Increase |
| Rastelli's New York Strip Steak 2 Units / 225 g / 8 oz | $0.00 | $126.95 | $+126.95 | +100.0% | New |
| Frozen Carite Steaks Bag 1 kg / 2.2 lb | $79.95 | $86.95 | $+7.00 | +8.8% | Increase |
| Frozen King Fish Steaks Bag 1 kg / 2.2 lb | $89.95 | $94.95 | $+5.00 | +5.6% | Increase |
| Prunes 1 kg / 2.2 lb | $54.95 | $29.70 | $-25.25 | -46.0% | Decrease |
| Fresh Bone-in Chicken Thighs Tray | $85.30 | $85.21 | $-0.09 | -0.1% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $209.44 | $208.49 | $-0.95 | -0.5% | Decrease |
| Avocado Mesh 5 Units | $42.95 | $39.95 | $-3.00 | -7.0% | Decrease |

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
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $34.70 | $89.95 | +159.2% |
| Cherries | $31.92 | $73.05 | +128.9% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $109.95 | $39.70 | -63.9% |
| Pop-Tarts Snack Crunchy Poppers Filled with Strawberry and Brownie 2 Units 360 g / 12.6 oz  | $174.95 | $64.70 | -63.0% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $34.70 | -61.4% |
| Frozen Bone-In Pork Shoulder Case | $1139.93 | $479.50 | -57.9% |
| Cherries | $75.18 | $32.76 | -56.4% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| United With Earth Date and Almond Rolls 340 g / 12 oz | United with Earth | $29.70 | 2026-01-15 |
| Cranberry 907 g / 2 lb |  | $57.95 | 2026-01-14 |
| Carapelli Organic Extra Virgin Olive Oil 880 g / 33.8 oz | Carapelli | $129.95 | 2026-01-14 |
| Pink Lady Apple 1.81 kg / 4 lb |  | $81.95 | 2026-01-14 |
| Coke Soft Drink Zero Sugar Free and Calorie Free 12 Units / 591 mL / 20 oz | Coca-Cola | $52.95 | 2026-01-14 |
| Gouda Block Cheese 500 g / 1.1 lb | Anchor | $54.95 | 2026-01-14 |
| My Mochi Peppermint Ice Cream 420 g / 15 oz | My Mochi | $29.70 | 2026-01-13 |
| Member’s Selection Breaded Mozzarella Sticks 2.04 kg / 4.5 lb | Member's Selection | $157.95 | 2026-01-12 |
| Mixed Tomato Cherry 907 g / 2 lb |  | $49.95 | 2026-01-12 |
| Chuckanut Bay Chocalate Covered Cheesecake Bites 634 g / 1.4 lb | Chuckanut Bay | $69.70 | 2026-01-12 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Rastelli's Ribeye Steak 2 Units 225 g / 8 oz | Rastelli's | $129.95 | G10D03 |
| Rastelli's New York Strip Steak 2 Units / 225 g / 8 oz | Rastelli's | $126.95 | G10D03 |
