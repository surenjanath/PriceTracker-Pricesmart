# PriceSmart Products Web Scraper

This is a Python web scraper designed to fetch product data from PriceSmart's API at [https://www.pricesmart.com](https://www.pricesmart.com) and store them in a SQLite database. It utilizes asyncio and aiohttp for asynchronous API calls and SQLAlchemy for database operations.

## About PriceSmart

PriceSmart is a membership-based warehouse club operator in the Caribbean and Central America. This scraper focuses on extracting product information from their Trinidad and Tobago (TT) store, including groceries, electronics, household items, and more.

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
- **Total products scraped**: 1123
- **Total value**: $125,448.36
- **Average price**: $111.71

## Database Changes
- **New products added**: 4
- **Existing products updated**: 1119
- **Price changes detected**: 96
- **Stock/availability changes**: 14
- **Discontinued products**: 7

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 186 |
|  | 148 |
| Badia | 18 |
| Swiss | 13 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Pepperoni Pizza 2 Units / 656 g / 1.44 lb | Member's Selection | $123.95 | true |
| Member's Selection Supreme Pizza 2 Units / 716 g / 1.57 lb | Member's Selection | $123.95 | true |
| Swiss Miss Dark Chocolate Flavor Cocoa Powder 50 Units 31 g / 1 oz  | Swiss Miss | $99.95 | true |
| McCain Mac and Cheese Triangles 2 Units / 400 g / 14 oz | McCain | $119.95 | true |
| Pop-Tarts Snack Crunchy Poppers Filled with Strawberry and Brownie 2 Units 360 g / 12.6 oz  | Pop Tarts | $174.95 | true |
| Pafritas Potatoes with Black Truffle Flavor 500 g / 1.1 lb | Pafritas | $112.95 | true |
| Fratelli Beretta Roll & Go Charcuterie Board 425 g / 15 oz | Fratelli Beretta | $108.95 | true |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | Bombolo Biscotti | $73.95 | true |
| My Mochi Peppermint Ice Cream 420 g / 15 oz | My Mochi | $99.95 | true |
| KFI Gluten-Free Curry and Coconut Sauce 2 Units / 695 g | KFI | $104.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1335
- **Price increases**: 764
- **Price decreases**: 489
- **Average increase**: 3.7%
- **Average decrease**: -3.7%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Fratelli Beretta Artisanal Charcuterie Tray 340 g / 12 oz | $92.95 | $94.95 | $+2.00 | +2.2% | Increase |
| Violife Just Like Mozzarella Shredded 453 g / 1 lb | $94.95 | $97.95 | $+3.00 | +3.2% | Increase |
| Angel Parboiled Rice Extra Long Grain 9 kg / 19.8 lb | $83.95 | $85.95 | $+2.00 | +2.4% | Increase |
| Dietz & Watson Maple Smoked Ham 454 g / 1 lb | $64.95 | $66.95 | $+2.00 | +3.1% | Increase |
| Dietz & Watson Sliced Breast Turkey 454 g / 1 lb | $94.95 | $96.95 | $+2.00 | +2.1% | Increase |
| Coke Sprite Schweppes  Assorted Sodas 24 Units / 237 mL / 8.34 oz | $86.95 | $88.95 | $+2.00 | +2.3% | Increase |
| Dietz and Watson Honey Turkey Breast 454 g / 16 oz | $94.95 | $96.95 | $+2.00 | +2.1% | Increase |
| Kings Basmati Rice 6.8 kg / 15 lb | $174.95 | $179.95 | $+5.00 | +2.9% | Increase |
| Member's Selection Thai Jasmine Long Grain Rice 9.07 kg / 20 lb | $149.95 | $159.95 | $+10.00 | +6.7% | Increase |
| Member's Selection Sliced Swiss Cheese 907 g / 2 lb | $92.95 | $89.95 | $-3.00 | -3.2% | Decrease |
| Member's Selection Variety Cheese Tray - 4 Types of Cheese / 907 g / 2 lb | $109.95 | $112.95 | $+3.00 | +2.7% | Increase |
| Member's Selection Sliced Mild Cheddar Cheese 907 g / 2 lb  | $62.95 | $64.95 | $+2.00 | +3.2% | Increase |
| Member's Selection Whole Almonds 907 g / 2 lb | $119.95 | $127.95 | $+8.00 | +6.7% | Increase |
| Lifeway Strawberry Kefir 2 Units / 946 mL / 32 oz | $86.95 | $89.95 | $+3.00 | +3.5% | Increase |
| Nongshim Shin Toomba Hot and Creamy Instant Ramen 4 Units / 137 g | $0.00 | $64.95 | $+64.95 | +100.0% | New |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $29.70 | $89.95 | +202.9% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $34.70 | $89.95 | +159.2% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| United With Earth Date and Almond Rolls 340 g / 12 oz | $26.70 | $54.95 | +105.8% |
| Purple Cabbage Unit | $14.70 | $29.95 | +103.7% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $109.95 | $39.70 | -63.9% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $34.70 | -61.4% |
| Black Seedless Grapes 907 g / 2 lb | $64.95 | $29.70 | -54.3% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Green Seedless Grapes 907 g / 2 lb | $62.95 | $29.70 | -52.8% |
| Leclerc Summer Cookies with Raspberry and Berry Flavor 2 Units / 300 g | $41.70 | $19.70 | -52.8% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Arcor Mint Hard Candies 2.26 Kg | Arcor | $89.95 | 2025-10-16 |
| Old El Paso Soft Flour Tortillas 8 Units / 38.87 g | Old El Paso | $37.95 | 2025-10-16 |
| Apple and Eve 100% Juice 36 Units / 200 mL / 6.76 oz | Apple & Eve | $149.95 | 2025-10-16 |
| Serge Vanilla Flavored Liquid Milk 12 Units / 200 mL | Serge | $29.70 | 2025-10-16 |
| Hunt's Assorted Pasta Sauce 3 Units / 680 g | Hunt's | $76.95 | 2025-10-16 |
| Sunshine Day Oh Banana Chips Variety Flavors 12 Units / 45 g | Sunshine | $54.95 | 2025-10-16 |
| Member’s Selection Freshly Prepared Holiday Cake | Member's Selection | $99.95 | 2025-10-16 |
| Freshway Red Dragon Fruit 794 g / 1.75 lb | Freshway | $79.95 | 2025-10-15 |
| Nestle Milo Ready to Drink 12 Units / 200 mL | Nestle | $69.95 | 2025-10-14 |
| Munchy's Vegetarian Salted Crackers 3 Units / 390 g / 13.75 oz | Munchy's | $49.95 | 2025-10-13 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Nongshim Shin Toomba Hot and Creamy Instant Ramen 4 Units / 137 g | Nongshim | $64.95 | G10D03 |
| Ankara Tricolor Pasta 4 Units / 350 g | Ankara | $33.95 | G10D03 |
| Member's Selection Ready-to-Eat Tuna Salad 907 g / 2 lb | Member's Selection | $121.95 | G10D03 |
| Member's Selection Chicken Caesar Wrap 4 Units | Member's Selection | $65.95 | G10D03 |
