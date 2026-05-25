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
- **Total products scraped**: 1144
- **Total value**: $126,317.39
- **Average price**: $110.42

## Database Changes
- **New products added**: 3
- **Existing products updated**: 1141
- **Price changes detected**: 30
- **Stock/availability changes**: 10
- **Discontinued products**: 6

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 177 |
|  | 138 |
| Badia | 17 |
| Swiss | 15 |
| Brunswick | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member’s Selection Canola Oil 2 Units / 2.84 L / 96 oz | Member's Selection | $159.95 | true |
| Jimmy Dean Croissant Sausage, Egg & Cheese Sandwiches 1.53 kg / 3.38 lb | Jimmy Dean | $162.95 | true |
| Setton Farms Premium Quality Pub-Style Pistachio Mix 567 g / 20 oz | Setton Farms | $131.95 | true |
| Sunny Fruits Dried Organic Figs 10 Units / 50 g / 1.76 oz | Sunny Fruits | $79.95 | true |
| Coffee Toppers Cold Foam 2 Units / 425 g / 15 oz | Coffee Toppers | $77.95 | true |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | Curly's | $137.95 | true |
| Pascual Yogi Kids Strawberry and Banana Yogurt with Fruit Pouch 24 Units / 80 g | Pascual | $229.95 | true |
| Carnation Creamy Evaporated Milk 6 Units / 330 mL | Carnation | $54.95 | true |
| Butterball Turkey Sausage 3 Units / 369 g / 13 oz | Butterball | $129.95 | true |
| Welch's Concord Grape Fruit Juice 1.75 L / 59 oz | Welch's | $33.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1168
- **Price increases**: 599
- **Price decreases**: 540
- **Average increase**: 5.7%
- **Average decrease**: -4.6%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Frozen Lamb Leg Whole Vacuum Packed | $406.23 | $404.50 | $-1.73 | -0.4% | Decrease |
| Sincerely Brigitte Hot Pepper Prairie Jack Cheese 454 g / 16 oz | $0.00 | $67.95 | $+67.95 | +100.0% | New |
| Bombolo Biscotti Assorted Decorated Cookies with Colorful Icing Summer Edition | $0.00 | $75.95 | $+75.95 | +100.0% | New |
| Polly-O String Cheese Mozzarella & Cheddar 24 Units | $0.00 | $98.95 | $+98.95 | +100.0% | New |
| Frozen Lamb Leg Whole Boneless Tray Pack | $348.40 | $350.61 | $+2.21 | +0.6% | Increase |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $222.72 | $223.00 | $+0.28 | +0.1% | Increase |
| Papaya | $35.06 | $35.19 | $+0.13 | +0.4% | Increase |
| Fine Choice Fresh Marinated Chicken Tray | $90.89 | $90.98 | $+0.09 | +0.1% | Increase |
| Chilled Chicken Gizzard Tray Pack | $45.98 | $45.84 | $-0.14 | -0.3% | Decrease |
| Frozen Pork Belly Skin On Sliced Tray  | $120.67 | $120.43 | $-0.24 | -0.2% | Decrease |
| Ribeye Choice Fillet Fresh Tray | $324.48 | $325.24 | $+0.76 | +0.2% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $147.95 | $148.41 | $+0.46 | +0.3% | Increase |
| Fresh Whole Chicken for Frying Bag | $285.84 | $286.01 | $+0.17 | +0.1% | Increase |
| Frozen Boneless Skinless Chicken Breast Tray | $135.90 | $136.44 | $+0.54 | +0.4% | Increase |
| Fresh Ground Chicken Tray | $102.86 | $103.11 | $+0.25 | +0.2% | Increase |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Fresh Beef Ribeye Steak Vacuum Packed | $246.08 | $2434.41 | +889.3% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $9.70 | $44.95 | +363.4% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |

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
| Tropicland Collagen Smoothie 1.2 kg / 2.6 lb | Tropicland | $137.95 | 2026-05-24 |
| Tetley Caffeine-Free Mint Tea 60 Units / 1.6 g | Tetley | $35.95 | 2026-05-24 |
| Stamina Energy Carbonated Energy Drink 12 Units / 330 mL / 11.16 oz | Stamina Energy | $55.95 | 2026-05-24 |
| Kiss Fruit Rum Sponge Cake 6 Units / 65 g | Kiss | $28.95 | 2026-05-24 |
| Orchard Sorrel Drink 6 Units / 1 L | Orchard | $39.70 | 2026-05-24 |
| Member's Selection Walnuts Halves and Pieces 1.13 kg / 40 oz | Member's Selection | $149.95 | 2026-05-24 |
| Member's Selection Whole Almonds - Healthy Snack 907 g / 32 oz | Member's Selection | $129.95 | 2026-05-23 |
| Kellogg's Original Squishmallows Cereal 671 g / 1.4 lb | Kellogg's | $42.70 | 2026-05-22 |
| Swiss Mustard Assortment 2 Units / 454 g / 16 oz | Swiss | $37.95 | 2026-05-21 |
| Finest Call Margarita Mix 1 L | Finest Call | $52.95 | 2026-05-20 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Sincerely Brigitte Hot Pepper Prairie Jack Cheese 454 g / 16 oz | Sincerely  Brigitte | $67.95 | G10D03 |
| Bombolo Biscotti Assorted Decorated Cookies with Colorful Icing Summer Edition | Bombolo Biscotti | $75.95 | G10D03 |
| Polly-O String Cheese Mozzarella & Cheddar 24 Units | Polly-O | $98.95 | G10D03 |
