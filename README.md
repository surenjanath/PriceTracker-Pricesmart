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
- **Total products scraped**: 1120
- **Total value**: $127,539.67
- **Average price**: $113.87

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1120
- **Price changes detected**: 0
- **Stock/availability changes**: 24
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 177 |
|  | 134 |
| Badia | 17 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Juver 100% Multifruit Juice 30 Units / 200 mL / 6.76 oz | Juver | $124.95 | true |
| Nescafé Ice Instant Coffee 2 Units / 100 g / 3.5 oz + Glass | Nescafé | $86.95 | true |
| Pringles Football Edition Potato Chips Assorted Flavors with Collectible Color-Changing Cup 3 Units 150 g / 5.2 oz | Pringles | $94.95 | true |
| Galbani Mozzarella Cheese Block 2.26 kg / 5 lb | Galbani | $122.95 | true |
| SIPPZZ Assorted Flavor Sparkling Juices 24 Units / 250 mL / 8.5 oz | SIPPZZ | $154.95 | true |
| 4C Peach Tea 2.34 kg / 5 lb | 4C | $89.95 | true |
| Lush Apple Flavored Fruit Drink 24 Units / 200 mL / 6.76 oz | Lush | $59.95 | true |
| Member's Selection Freshly Made Assorted Doughnuts 12 Units | Member's Selection | $55.95 | true |
| Member's Selection Freshly Baked Chocolate Chip Cookies 24 Units | Member's Selection | $60.95 | true |
| Member's Selection Freshly Baked Blueberry Mini Muffins 24 Units | Member's Selection | $43.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1045
- **Price increases**: 517
- **Price decreases**: 503
- **Average increase**: 6.5%
- **Average decrease**: -4.8%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Fresh Whole Chicken for Frying Bag | $283.04 | $282.88 | $-0.16 | -0.1% | Decrease |
| Fresh Whole Chicken 2 Units | $104.50 | $104.33 | $-0.17 | -0.2% | Decrease |
| Barista Vanilla Cappuccino Powder Mix 2 Units / 320 g | $0.00 | $74.95 | $+74.95 | +100.0% | New |
| McVitie's Ginger Nut Biscuits 4 Units / 250 g | $34.95 | $24.70 | $-10.25 | -29.3% | Decrease |
| Papaya | $39.40 | $39.36 | $-0.04 | -0.1% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $117.41 | $117.59 | $+0.18 | +0.2% | Increase |
| Member's Selection Frozen Bone-In Lamb Stew Bag | $88.70 | $89.12 | $+0.42 | +0.5% | Increase |
| Fresh Chicken Leg Quarters Tray | $95.40 | $95.50 | $+0.10 | +0.1% | Increase |
| Fresh Beef Striploin Steak Tray | $240.39 | $243.72 | $+3.33 | +1.4% | Increase |
| Member's Selection Frozen Boneless Pork Butt Stew Tray | $79.17 | $79.30 | $+0.13 | +0.2% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $162.53 | $162.19 | $-0.34 | -0.2% | Decrease |
| Fresh Ground Chicken Tray | $100.47 | $100.22 | $-0.25 | -0.2% | Decrease |
| Frozen Lamb Shoulder Chops Tray | $119.79 | $119.96 | $+0.17 | +0.1% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Case | $1625.64 | $1629.84 | $+4.20 | +0.3% | Increase |
| Fresh Chicken Thighs Boneless Bag | $334.52 | $334.28 | $-0.24 | -0.1% | Decrease |

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
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Marbella Asian Sushi Roll 10 Units | Marbella | $58.95 | 2026-07-01 |
| Kellogg’s Assorted Cereals Corn Pops, Froot Loops & Apple Jacks 3 Bags / 1.05 kg / 37.3 oz | Kellogg's | $49.70 | 2026-07-01 |
| Pafritas Potatoes with Black Truffle Flavor 500 g / 1.1 lb | Pafritas | $59.70 | 2026-07-01 |
| Ferrero Rocher Giant Chocolate Bonbon Filled with Hazelnut and Chocolate Cream 125 g / 4.4 oz | Ferrero Rocher | $69.95 | 2026-07-01 |
| Fresh Apple Cosmic Crisp 1.36 kg / 3 lb |  | $67.95 | 2026-07-01 |
| Copper Kettle Dark Chocolate Truffles with Sea Salt 448 g / 16 oz | Copper Kettle | $149.95 | 2026-06-30 |
| KFI Gluten-Free Butter Chicken Sauce 2 Units / 695 g | KFI | $69.70 | 2026-06-30 |
| Par Excellence Jasmine White Rice 10 kg / 352.74 oz | Par Excellence | $124.70 | 2026-06-28 |
| Amare Probiotics Sorrel Hibiscus with Infused Water Kefir 3 Units / 355 mL / 12 oz | Amare Probiotics | $76.95 | 2026-06-28 |
| Garofalo Organic Penne Rigate 4 Units / 500 g / 1.1 lb | Garofalo | $89.95 | 2026-06-28 |

## New Products Added Today
No new products added today.
