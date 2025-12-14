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
- **Total products scraped**: 1168
- **Total value**: $134,148.99
- **Average price**: $114.85

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1166
- **Price changes detected**: 17
- **Stock/availability changes**: 22
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 195 |
|  | 148 |
| Badia | 18 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Unsweetened Almond Beverage 6 Units /  946 mL / 32 oz | Member's Selection | $99.95 | true |
| Member's Selection Iced Coffee Mocha Drink 12 Units / 296 mL / 10 oz | Member's Selection | $154.95 | true |
| Crazy Monkey Baking Granola Snacks with Dark Chocolate 680 g / 1.5 lb | Crazy Monkey Baking | $119.95 | true |
| Mariani Dried Red Fruit Mix with Cherries, Blueberries, and Strawberries 567 g / 20 oz | Mariani | $90.95 | true |
| Nonni's Almond and Cranberry Cookies 575 g / 1.26 lb | Nonni's | $134.95 | true |
| Marie Callender's Italian Meat Lasagna 879 g / 1.94 lb | Marie Callender's | $83.95 | true |
|  Best Fruit Ripe Dehydrated Mangoes 4 Units / 100 g | Best Fruit | $94.95 | true |
| Helado Mexico Ice Cream Bars 24 Units / 81 mL / 2.74 oz | Helado México | $167.95 | true |
| Aqua Star Breaded Shrimp 680 g / 1.5 lb | Aqua Star | $92.95 | true |
| Suzy's Cream Assorted Flavors Cheesecake New York, Strawberry, Chocolate, and Caramel 12 Slices | Suzy's Cream Cheesecakes | $144.84 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1402
- **Price increases**: 793
- **Price decreases**: 540
- **Average increase**: 5.0%
- **Average decrease**: -6.9%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Red Rose Pink Salmon 3 Units / 418 g | $0.00 | $125.95 | $+125.95 | +100.0% | New |
| Riceworks Sea Salt Sesame Chips 454 g / 16 oz | $0.00 | $85.95 | $+85.95 | +100.0% | New |
| Green pepper | $40.04 | $39.96 | $-0.08 | -0.2% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $112.42 | $112.58 | $+0.16 | +0.1% | Increase |
| Fresh Seasoned BBQ Chicken Quarters Bag | $94.66 | $94.62 | $-0.04 | -0.0% | Decrease |
| Member's Selection Frozen Sliced Turkey Wings, Bag | $154.55 | $154.35 | $-0.20 | -0.1% | Decrease |
| Frozen Lamb Shoulder Chops Tray | $124.53 | $124.71 | $+0.18 | +0.1% | Increase |
| Cherries | $34.01 | $34.15 | $+0.14 | +0.4% | Increase |
| Frozen Lamb Leg Whole Vacuum Packed | $393.56 | $397.88 | $+4.32 | +1.1% | Increase |
| Frozen Bone-In Pork Spare Rib Vacuum Packaged | $153.27 | $153.53 | $+0.26 | +0.2% | Increase |
| Whole Rack Frozen Baby Back Ribs Vacuum Packaged | $151.54 | $150.97 | $-0.57 | -0.4% | Decrease |
| Frozen Boneless Skinless Chicken Breast Tray | $148.29 | $149.41 | $+1.12 | +0.8% | Increase |
| Member's Selection Chilled Chicken Liver, Tray Pack | $41.56 | $41.61 | $+0.05 | +0.1% | Increase |
| Member's Selection Frozen Boneless Pork Loin Roast Tray | $101.93 | $101.61 | $-0.32 | -0.3% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Stew Tray | $95.85 | $96.15 | $+0.30 | +0.3% | Increase |

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
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Black Seedless Grapes 907 g / 2 lb | $29.70 | $64.95 | +118.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |

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
| Hormel Turkey Pepperoni 2 Units / 227 g / 8 oz | Hormel | $74.95 | 2025-12-12 |
| Russco's Green Pepper Salsa 750 mL | Russco's | $19.95 | 2025-12-10 |
| La Yogurt Latin Flavor Mango 907 g / 32 oz | La Yogurt | $32.95 | 2025-12-10 |
| Toppers Popcorn Gluten Free 600 g | Toppers | $39.95 | 2025-12-10 |
| Kellogg's Special K Flakes with Red Berries 1.07 kg / 38 oz | Kellogg's | $89.70 | 2025-12-10 |
| Devon Digestive Bites 12 Units / 50 g | Devon | $48.70 | 2025-12-10 |
| Russet Potato 2.2 kg / 5 lb |  | $22.95 | 2025-12-10 |
| Kiss Mighty Loaf Wheat Bread 945 g | Kiss | $16.45 | 2025-12-10 |
| Russco's Green Herbal Seasoning 750 mL | Russco's | $22.95 | 2025-12-10 |
| Kala Brand Madras Curry 1.2 kg  | Kala Brand | $79.95 | 2025-12-10 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Red Rose Pink Salmon 3 Units / 418 g | Red Rose | $125.95 | G10D03 |
| Riceworks Sea Salt Sesame Chips 454 g / 16 oz | Riceworks | $85.95 | G10D03 |
