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
- **Total value**: $129,778.19
- **Average price**: $112.65

## Database Changes
- **New products added**: 3
- **Existing products updated**: 1149
- **Price changes detected**: 51
- **Stock/availability changes**: 25
- **Discontinued products**: 5

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
| Just About Foods Organic and Creamy Peanut Butter 1.13 kg / 40 oz | Just About Foods | $97.95 | true |
| Bob's Red Mill Oatmeal with Protein 1.81 kg / 4 lb | Bob's Red Mill | $144.95 | true |
| Coffee Toppers Salted Caramel Whipped Cream 2 Units / 425 g / 15 oz | Coffee Toppers | $79.95 | true |
| Trevijano Thai Style Cous Cous Rice 800 g / 28.2 oz | Trevijano | $75.95 | true |
| Izzio Artisan Naturally Fermented Sourdough Bread Sliced | Izzio | $49.95 | true |
| Swiss Miss Sugar-free Cocoa 60 Units / 20 g / 0.7 oz | Swiss Miss | $109.95 | true |
| Terra Creta Extra Virgin Olive Oil in Marasca 1 L / 33.81 oz | Terra Creta | $134.95 | true |
| YoguRico Strawberry Low Fat Drinkable Yogurt  1.68 L / 57 oz | YoguRico | $54.95 | true |
| Diamond Shelled Walnuts 907 g / 32 oz | Diamond | $139.95 | true |
| Copper Kettle Dark Chocolate Truffles with Sea Salt 448 g / 16 oz | Copper Kettle | $139.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1002
- **Price increases**: 501
- **Price decreases**: 466
- **Average increase**: 5.1%
- **Average decrease**: -5.9%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Dare Viva Puffs Cookies with Marshmallows and Strawberry Covered in Chocolate 2 Units / 300 g | $49.95 | $44.70 | $-5.25 | -10.5% | Decrease |
| Orchard Assorted Drinks Juice Mix 6 Units / 1L | $69.95 | $64.95 | $-5.00 | -7.1% | Decrease |
| Edwards Signatures Pecan Pie 907g / 2 lb | $68.95 | $69.95 | $+1.00 | +1.5% | Increase |
| Member's Selection Sliced Swiss Cheese 907 g / 2 lb | $89.95 | $87.95 | $-2.00 | -2.2% | Decrease |
| Member's Selection Shredded Mexican-Style Cheese 2 Units / 680 g / 1.5 lb | $106.95 | $104.95 | $-2.00 | -1.9% | Decrease |
| Apple & Eve Organic Orange Carrot Juice 2 Units / 2.84 L / 96 oz | $79.70 | $109.95 | $+30.25 | +38.0% | Increase |
| DeLallo Provoloni Antipasti 317 g / 11.2 oz | $0.00 | $69.95 | $+69.95 | +100.0% | New |
|  Best Fruit Ripe Dehydrated Mangoes 4 Units / 100 g | $94.95 | $82.70 | $-12.25 | -12.9% | Decrease |
| Smartfood White Cheddar Cheese Flavor Popcorn 156 g / 5.50 oz | $23.95 | $24.95 | $+1.00 | +4.2% | Increase |
| Annie's Organic Macaroni and Cheese Variety Pack 12 Units / 170 g | $199.70 | $99.70 | $-100.00 | -50.1% | Decrease |
| Swiss Sorrel Drink 3 Units / 750 mL / 25.36 oz | $43.70 | $29.70 | $-14.00 | -32.0% | Decrease |
| Member's Selection Canola Oil Spray 2 Units 400 mL / 13.5 oz | $0.00 | $74.95 | $+74.95 | +100.0% | New |
| Frozen Pork Belly Skin On Sliced Tray  | $109.87 | $110.35 | $+0.48 | +0.4% | Increase |
| Papaya | $32.06 | $31.90 | $-0.16 | -0.5% | Decrease |
| Holiday Snacks Assorted Hot Potato Chips 12 Units | $49.95 | $39.70 | $-10.25 | -20.5% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $29.70 | $89.95 | +202.9% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $34.70 | $89.95 | +159.2% |
| Cherries | $31.92 | $73.05 | +128.9% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Black Seedless Grapes 907 g / 2 lb | $29.70 | $64.95 | +118.7% |

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
| Cranberry 907 g / 2 lb |  | $57.95 | 2026-01-14 |
| Carapelli Organic Extra Virgin Olive Oil 880 g / 33.8 oz | Carapelli | $129.95 | 2026-01-14 |
| Pink Lady Apple 1.81 kg / 4 lb |  | $81.95 | 2026-01-14 |
| Coke Soft Drink Zero Sugar Free and Calorie Free 12 Units / 591 mL / 20 oz | Coca-Cola | $52.95 | 2026-01-14 |
| Gouda Block Cheese 500 g / 1.1 lb | Anchor | $54.95 | 2026-01-14 |
| My Mochi Peppermint Ice Cream 420 g / 15 oz | My Mochi | $29.70 | 2026-01-13 |
| Member’s Selection Breaded Mozzarella Sticks 2.04 kg / 4.5 lb | Member's Selection | $157.95 | 2026-01-12 |
| Mixed Tomato Cherry 907 g / 2 lb |  | $49.95 | 2026-01-12 |
| Chuckanut Bay Chocalate Covered Cheesecake Bites 634 g / 1.4 lb | Chuckanut Bay | $69.70 | 2026-01-12 |
| Member's Selection Spaghetti 4 Units / 454 g / 1 lb | Member's Selection | $59.95 | 2026-01-12 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| DeLallo Provoloni Antipasti 317 g / 11.2 oz | DeLallo | $69.95 | G10D03 |
| Member's Selection Canola Oil Spray 2 Units 400 mL / 13.5 oz | Member's Selection | $74.95 | G10D03 |
| Nature Valley Sweet and Salty Almond Granola Bar 36 Units / 34 g / 1.2 oz | Nature Valley | $129.95 | G10D03 |
