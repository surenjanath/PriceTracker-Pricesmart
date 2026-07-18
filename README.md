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
- **Total products scraped**: 1115
- **Total value**: $124,461.73
- **Average price**: $111.62

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1114
- **Price changes detected**: 37
- **Stock/availability changes**: 17
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 177 |
|  | 135 |
| Badia | 16 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| El Exquisito Sabor Traditional Tiramisu with Ladyfingers and Mascarpone | El Exquisito Sabor | $91.95 | true |
| Perrier Sparkling Mineral Water Refreshing and Bubbly Pack of 4 Units / 330 mL / 11.15 oz | Perrier | $39.95 | true |
| SIPPZZ Assorted Flavor Sparkling Juices 24 Units / 250 mL / 8.5 oz | SIPPZZ | $154.95 | true |
| Bagelmania Artisanal Simple Bagel Bread 6 Units | Bagelmania | $34.95 | true |
| Kirkland Signature Mini Chocolate Chip Cookies 30 Units 28 g / 1 oz | Kirkland Signature | $172.95 | true |
| Chobani Low-Fat Greek Yogurt 16 Units / 128 g / 4.5 oz | Chobani | $174.95 | true |
| Maison Perrier Sparkling Water with Lime Flavor 10 Units / 250 mL / 8.5 oz | Maison Perrier | $89.95 | true |
| Barista Vanilla Cappuccino Powder Mix 2 Units / 320 g | Café Barista | $74.95 | true |
| Lush Apple Flavored Fruit Drink 24 Units / 200 mL / 6.76 oz | Lush | $59.95 | true |
| Crix Crispy Salted Crackers 4 Units / 300 g | Crix | $55.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1055
- **Price increases**: 561
- **Price decreases**: 464
- **Average increase**: 5.9%
- **Average decrease**: -5.3%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Member's Selection Frozen Sliced Turkey Wings, Bag | $193.68 | $193.29 | $-0.39 | -0.2% | Decrease |
| Member's Selection Frozen Boneless Pork Butt Stew Tray | $90.90 | $91.04 | $+0.14 | +0.2% | Increase |
| Garofalo Gluten Free Spaghetti 4 Units / 340 g / 12 oz | $0.00 | $84.95 | $+84.95 | +100.0% | New |
| Mini Sweet Peppers 454 g / 1 lb | $47.95 | $49.95 | $+2.00 | +4.2% | Increase |
| Frozen Sliced Turkey Drumsticks | $190.94 | $191.48 | $+0.54 | +0.3% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $117.24 | $117.06 | $-0.18 | -0.2% | Decrease |
| Fresh Bone-in Chicken Thighs Tray | $68.10 | $68.17 | $+0.07 | +0.1% | Increase |
| Gouda Cheese Block | $89.29 | $89.42 | $+0.13 | +0.1% | Increase |
| Peach 908 g / 2 lb | $54.95 | $57.95 | $+3.00 | +5.5% | Increase |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $193.76 | $193.47 | $-0.29 | -0.1% | Decrease |
| Mini Potato 1.3 kg / 3 lb | $47.95 | $52.95 | $+5.00 | +10.4% | Increase |
| Fine Choice Fresh Marinated Chicken Tray | $92.82 | $92.59 | $-0.23 | -0.2% | Decrease |
| Plum 907 g / 2 lb | $72.95 | $69.95 | $-3.00 | -4.1% | Decrease |
| Cauliflower 1 Unit | $41.95 | $52.95 | $+11.00 | +26.2% | Increase |
| Frozen Lamb Shoulder Chops Tray | $120.14 | $119.96 | $-0.18 | -0.1% | Decrease |

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
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Nature's Pride Small Red Beans 1.8 kg | Nature's Pride | $42.95 | 2026-07-17 |
| Leclerc Quattro French Creme Cookies 2 Unit / 300 g | Leclerc | $47.95 | 2026-07-15 |
| Pascual Yogi Kids Strawberry and Banana Yogurt with Fruit Pouch 24 Units / 80 g | Pascual | $229.95 | 2026-07-15 |
| Prana Granola Organic Oatmeal Cookie Flavor 1 kg / 35.27 oz | Prana | $105.95 | 2026-07-14 |
| Hostess Twinkies and Cupcakes Individually Packaged Assorted 32 Units | Hostess | $104.95 | 2026-07-14 |
| Member's Selection Freshly Baked Sweet and Creamy Vanilla Cake 80 to 100 Slices | Member's Selection | $399.95 | 2026-07-14 |
| Banner Farms Straight-Cut French Fries  | Banner Farms | $305.95 | 2026-07-12 |
| Badia Mojo Rub Citrus Blend 680.4 g / 24 oz  | Badia | $32.70 | 2026-07-12 |
| Nature Valley Sweet and Salty Almond Granola Bar 36 Units / 34 g / 1.2 oz | Nature Valley | $129.95 | 2026-07-11 |
| Pafritas Paprika Flavor Potato Chips 500 g / 1.1 lb | Pafritas | $59.70 | 2026-07-11 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Garofalo Gluten Free Spaghetti 4 Units / 340 g / 12 oz | Garofalo | $84.95 | G10D03 |
