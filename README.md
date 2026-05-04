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
- **Total products scraped**: 1155
- **Total value**: $131,264.38
- **Average price**: $113.65

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1154
- **Price changes detected**: 49
- **Stock/availability changes**: 17
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 186 |
|  | 137 |
| Badia | 18 |
| Swiss | 15 |
| Brunswick | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Freshly Baked Vanilla Loaf Cake | Member's Selection | $30.95 | true |
| Member's Selection Freshly Baked Berries Cake 12 Slices | Member's Selection | $139.95 | true |
| Member's Selection Cookies and Cream Cake Decorated with Oreo Cookie 12 Slices | Member's Selection | $139.95 | true |
| Calbee Snacks Lightly Salted Baked Pea Crisps 567 g / 1.25 lb | Calbee | $116.95 | true |
| Eggo Thick & Fluffy Waffles Original & Blueberry 2 Units / 330 g / 11.6 oz | Eggo | $109.95 | true |
| Pizzacini Truffle and Mushroom Pizza 2 Units / 440 g / 15.5 oz | Pizzacini | $169.95 | true |
| Nescafé Classic Instant Coffee 100% Pure 170 g | Nescafé | $61.95 | true |
| Swiss Honey Mustard Sauce 2 Units / 454 g | Swiss | $42.95 | true |
| Sacla Italia Pizza Sauce 1 kg / 35.2 oz | Sacla | $64.95 | true |
| Heinz Tomato Ketchup 567 g / 20 oz | Heinz | $29.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1122
- **Price increases**: 605
- **Price decreases**: 494
- **Average increase**: 6.2%
- **Average decrease**: -5.5%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Fine Choice Fresh Marinated Chicken Tray | $83.06 | $83.27 | $+0.21 | +0.3% | Increase |
| Fresh Chicken Thighs Boneless Bag | $314.74 | $317.62 | $+2.88 | +0.9% | Increase |
| Quaker Instant Oatmeal 52 Units / 43 g / 1.51 oz | $127.07 | $157.44 | $+30.37 | +23.9% | Increase |
| Chobani Greek Yogurt 907 g / 32 oz | $55.95 | $67.95 | $+12.00 | +21.4% | Increase |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $202.99 | $201.03 | $-1.96 | -1.0% | Decrease |
| Member's Selection Freshly Prepared Tuna Salad Wraps 4 Units | $65.95 | $62.95 | $-3.00 | -4.5% | Decrease |
| Frozen Pork Belly Skin On Sliced Tray  | $116.83 | $117.79 | $+0.96 | +0.8% | Increase |
| Papaya | $32.57 | $32.76 | $+0.19 | +0.6% | Increase |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $0.00 | $137.95 | $+137.95 | +100.0% | New |
| Fresh Bone-in Chicken Thighs Tray | $68.24 | $68.38 | $+0.14 | +0.2% | Increase |
| Froot Loops, Corn Pops, Apple Jacks, Cocoa Krispies and Frosted Flakes Assorted Cereal Pack 25 Units | $114.95 | $91.45 | $-23.50 | -20.4% | Decrease |
| Frozen Sliced Turkey Drumsticks | $192.68 | $189.07 | $-3.61 | -1.9% | Decrease |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $222.72 | $223.86 | $+1.14 | +0.5% | Increase |
| Member's Selection Frozen Lamb Neck, Bone in, skinless, Tray | $85.23 | $85.11 | $-0.12 | -0.1% | Decrease |
| Member's Selection Breaded Chicken Bites Ready to Heat | $86.95 | $84.95 | $-2.00 | -2.3% | Decrease |

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
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $14.70 | $57.95 | +294.2% |

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
| Rastelli's Frozen New York Steak Case 10 Units / 225 g / 8 oz  | Rastelli's | $536.95 | 2026-05-01 |
| Frosted Flakes Donut Holes Glazed Cereal 893 g / 31.5 oz | Zucaritas | $54.70 | 2026-04-29 |
| Fireside Marshmallows 1 kg / 2.2 lb | Fireside | $72.95 | 2026-04-29 |
| Golden Kiwi 1 lb / 453 g |  | $74.95 | 2026-04-29 |
| Badia Crushed Parsley Flakes 56.7 g / 2 oz | Badia | $21.95 | 2026-04-28 |
| Rastelli's Ribeye Steak Frozen 10 Units / 225 g / 8 oz  | Rastelli's | $557.95 | 2026-04-28 |
| Rastelli’s Ribeye Steak 2 Units / 225 g / 8 oz | Rastelli's | $122.95 | 2026-04-28 |
| Califia Farms Pumpkin Spice Latte 1.4 L / 48 oz | Califia Farms | $69.95 | 2026-04-22 |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | Activia | $87.95 | 2026-04-22 |
| Baby Carrots 907 g / 2 lb |  | $34.95 | 2026-04-22 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Curly's Baby Back Pork Ribs 680 g / 24 oz | Curly's | $137.95 | G10D03 |
