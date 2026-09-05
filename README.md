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
- **Total products scraped**: 1128
- **Total value**: $124,856.22
- **Average price**: $110.69

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1128
- **Price changes detected**: 44
- **Stock/availability changes**: 20
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 175 |
|  | 135 |
| Badia | 16 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Oikos Greek Yogurt 18 Units / 150 g / 5.3 oz | Oikos | $199.95 | true |
| Table Foods Stuffed Peppers Variety 504 g / 18 oz | Table Foods | $116.95 | true |
| Lee Kum Kee Traditional Soy Sauce for Cooking and Marinating 2 Units / 500 mL | Lee Kum Kee | $39.95 | true |
| Lush Assorted Fruit Flavored Drinks 24 Units / 200 mL / 6.76 oz | Lush | $64.95 | true |
|  Chobani Greek Yogurt Plain 1.13 kg / 2.5 lb | Chobani | $78.95 | true |
| Smithfield Smoked and Caramelized Pork Shoulder Cubes 453 g / 1 lb | Smithfield | $177.95 | true |
| Nesquik Strawberry Flavored Whole Grain Corn Cereal 1.01 kg / 35.9 oz | Nesquik | $52.95 | true |
| King Cheese Feta with Flavors 2 Units / 227 g / 8 oz | King Cheese | $104.95 | true |
| Café Santo Domingo 100% Dominican Arabica Ground Coffee 2 Units / 453.6 g | Cafe Santo Domingo | $109.95 | true |
| Par Excellence 100% Refined Soybean Oil for Cooking and Frying 8.6 L | Par Excellence | $129.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1047
- **Price increases**: 507
- **Price decreases**: 500
- **Average increase**: 7.8%
- **Average decrease**: -6.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $34.70 | $57.95 | $+23.25 | +67.0% | Increase |
| Fresh Whole Striploin Fillet Vacuum packaged | $2379.57 | $2167.07 | $-212.50 | -8.9% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $114.60 | $114.42 | $-0.18 | -0.2% | Decrease |
| Member's Selection Frozen Bone-In Beef Feet Sliced, Tray | $134.23 | $134.48 | $+0.25 | +0.2% | Increase |
| Frozen Beef Feet  | $115.43 | $112.85 | $-2.58 | -2.2% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $201.48 | $200.90 | $-0.58 | -0.3% | Decrease |
| Swiss Elbows 6 Units / 300 g / 10.6 oz | $24.95 | $28.95 | $+4.00 | +16.0% | Increase |
| Swiss Twists 6 Units / 300 g | $24.95 | $28.95 | $+4.00 | +16.0% | Increase |
| Nectarine 908 g / 2 lb | $69.95 | $77.95 | $+8.00 | +11.4% | Increase |
| Mini Sweet Peppers 454 g / 1 lb | $42.95 | $52.95 | $+10.00 | +23.3% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $66.34 | $66.41 | $+0.07 | +0.1% | Increase |
| Frozen Bone-In Pork Shoulder Vacuum Packed | $194.41 | $209.69 | $+15.28 | +7.9% | Increase |
| Swiss Spaghetti 6 Units / 400 g | $28.95 | $32.95 | $+4.00 | +13.8% | Increase |
| Plum 907 g / 2 lb | $64.95 | $67.95 | $+3.00 | +4.6% | Increase |
| Member's Selection Frozen Boneless Pork Butt Stew Tray | $85.62 | $85.89 | $+0.27 | +0.3% | Increase |

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
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Pam Original Oil Spray 2 Units /  400 g / 14 oz | PAM | $109.95 | 2026-09-03 |
| Crispy Just Baked Mini Naan Bread Bites Baked and Crunchy Snack Style | Crispy Just Baked | $44.95 | 2026-09-03 |
| Ocean Delight Caribbean Spiny Lobster Tails 2 Units / 198 g / 7 oz | Ocean Delight | $245.95 | 2026-09-02 |
| Ginger 680 g / 1.5 lb |  | $24.95 | 2026-09-02 |
| Coffee Toppers Salted Caramel Whipped Cream 2 Units / 425 g / 15 oz | Coffee Toppers | $29.70 | 2026-09-02 |
| Just About Foods Organic and Creamy Peanut Butter 1.13 kg / 40 oz | Just About Foods | $96.95 | 2026-09-01 |
| Cream of Wheat Hot Cereal 794 g / 28 oz | Cream of Wheat | $59.95 | 2026-08-31 |
| Frozen Lamb Leg Whole Boneless Tray Pack |  | $352.45 | 2026-08-30 |
| Swift Frozen Chilled Pork Ribs Kansas City Style BBQ Vacuum Pack  | Swift | $175.90 | 2026-08-30 |
| Coffee Mate Italian Sweet Creme Coffee Creamer 1.89 L / 64 oz | Coffee Mate | $74.95 | 2026-08-27 |

## New Products Added Today
No new products added today.
