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
- **Total products scraped**: 1095
- **Total value**: $118,336.12
- **Average price**: $108.07

## Database Changes
- **New products added**: 7
- **Existing products updated**: 1088
- **Price changes detected**: 50
- **Stock/availability changes**: 7
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 183 |
|  | 130 |
| Badia | 18 |
| Swiss | 15 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Sunny Fruits Organic Dried Apricots 10 Units / 50 g / 1.76 oz | Sunny Fruits | $59.95 | true |
| Califia Farms Matcha Latte Almond Milk 1.4 L / 48 oz | Califia Farms | $69.95 | true |
| Pringles Mingles Cheddar and Sour Cream Puffed Snacks 2 Units / 155 g / 5.5 oz | Pringles | $69.95 | true |
| Sunberry Farms Organic Mango Nectar Juice - Gluten Free 3.78 L / 128 oz | Sunberry Farms | $74.95 | true |
| Sensible Portions Vegetable Straws with Sea Salt 666 g / 23.5 oz | Sensible Portions | $109.95 | true |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | Kozyshack | $87.95 | true |
| Blue Waters Sparkling Drink with Cran and Grape Flavor 12 Units / 330 mL / 11.15 oz | Blue Waters | $25.95 | true |
| Stauffers Snaps Crunchy Lemon-Flavored Cookies 397 g / 14 oz | Stauffers | $49.95 | true |
| Goya Coconut Milk 3 Units / 400 mL / 13.5 oz | Goya | $65.95 | true |
| Member's Selection Frozen Boneless Salmon Portions with Skin 680 g / 1.5 lb | Member's Selection | $169.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1615
- **Price increases**: 237
- **Price decreases**: 254
- **Average increase**: 5.4%
- **Average decrease**: -3.7%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Toppers Popcorn Gluten Free 600 g | $0.00 | $39.95 | $+39.95 | +100.0% | New |
| Lucema Snail Shell Pasta 6 Units / 250 g / 8.8 oz | $31.95 | $30.70 | $-1.25 | -3.9% | Decrease |
| Salad Tomato 1.5 kg / 3.5 lb | $0.00 | $29.95 | $+29.95 | +100.0% | New |
| Green Cabbage Unit | $0.00 | $25.95 | $+25.95 | +100.0% | New |
| Salad Tomato 1.5 kg / 3.5 lb | $0.00 | $29.95 | $+29.95 | +100.0% | New |
| Avocado Mesh 5 Units | $34.95 | $47.95 | $+13.00 | +37.2% | Increase |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $202.68 | $201.62 | $-1.06 | -0.5% | Decrease |
| Chilled Skinless Boneless Beef Ribeye Steak Vacuum Package Whole Piece | $2311.11 | $2180.13 | $-130.98 | -5.7% | Decrease |
| Pepsi Cola Soft Drink 24 Units / 500 mL | $71.95 | $69.95 | $-2.00 | -2.8% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $138.88 | $138.58 | $-0.30 | -0.2% | Decrease |
| Swiss Pasta Shells and Bow Ties 6 Units / 300 g | $31.95 | $28.70 | $-3.25 | -10.2% | Decrease |
| Mini Sweet Peppers 454 g / 1 lb | $42.95 | $47.95 | $+5.00 | +11.6% | Increase |
| Mixed Bell Pepper 1.36 kg / 3 lb | $0.00 | $36.95 | $+36.95 | +100.0% | New |
| Fresh Ground Chicken Meat Bag | $264.64 | $264.96 | $+0.32 | +0.1% | Increase |
| Avocado 2 Units | $29.95 | $24.70 | $-5.25 | -17.5% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| Member's Selection Mocha Flavor Cold Coffee Drink 9 Units / 405 mL / 13.7 oz | $105.70 | $176.95 | +67.4% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $54.70 | $82.95 | +51.6% |
| Lush Natural Refreshing Apple Flavored Drink 36 Units / 200 ml | $52.70 | $72.95 | +38.4% |
| Avocado Mesh 5 Units | $34.95 | $47.95 | +37.2% |
| Iceberg Lettuce Unit | $19.70 | $26.95 | +36.8% |
| Badia Granulated Onion 566.9 g / 20 oz | $28.45 | $37.95 | +33.4% |
| Virginia Brand Vidalia Onion Vinaigrette 1 L / 33.8 oz | $39.95 | $49.95 | +25.0% |
| Kraft Slow-Simmered Original Barbecue Sauce 2.3 kg  | $71.95 | $89.95 | +25.0% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Frito Lay Assortment Box 24 Units | $99.95 | $49.70 | -50.3% |
| Fresh Regular Tomato | $47.85 | $28.51 | -40.4% |
| Iceberg Lettuce Unit | $27.95 | $19.70 | -29.5% |
| Okra 30 Units | $26.95 | $19.95 | -26.0% |
| Fresh Cello Carrots 1.3 kg / 3 lb | $24.95 | $19.70 | -21.0% |
| Badia Ground Turmeric 453.6 g / 16 oz  | $38.95 | $30.95 | -20.5% |
| Iceberg Lettuce Unit | $34.95 | $27.95 | -20.0% |
| State Fair Mini Corn Dogs 46 Units / 18.7 g / 0.66 oz | $74.95 | $59.95 | -20.0% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Black's Family Sweet Potato Chips 510 g / 18 oz | Black's Family | $79.95 | 2025-08-08 |
| Lush Fruit Juice Assorted Flavors 36 Units / 200 mL / 6.7 mL | Lush | $37.70 | 2025-08-07 |
| Bragg Apple Cider Vinegar 2 Units / 473 mL | Bragg | $65.95 | 2025-08-07 |
| Member's Selection Shredded Mozzarella Cheese 453 g / 1 lb | Member's Selection | $28.95 | 2025-08-07 |
| Dare Veggie Chips with Sea Salt 405 g / 14.28 oz | Dare | $89.95 | 2025-08-07 |
| Bumble Bee Pink Salmon 4 Units / 418 g / 14.75 oz | Bumble Bee | $149.70 | 2025-08-07 |
| Seven French Fry 3/8 Case 10 kg / 22 lb | Seven | $153.95 | 2025-08-07 |
| Member's Selection Minced Garlic in Olive Oil 907 g / 32 oz | Member's Selection | $53.95 | 2025-08-07 |
| Black Seedless Grapes |  | $93.28 | 2025-08-06 |
| Busta Assorted Soft Drinks 24 Units / 500 mL | Busta | $39.70 | 2025-08-05 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Toppers Popcorn Gluten Free 600 g | Toppers | $39.95 | G10D03 |
| Salad Tomato 1.5 kg / 3.5 lb |  | $29.95 | G10D03 |
| Green Cabbage Unit |  | $25.95 | G10D03 |
| Salad Tomato 1.5 kg / 3.5 lb |  | $29.95 | G10D03 |
| Mixed Bell Pepper 1.36 kg / 3 lb |  | $36.95 | G10D03 |
| Hershey's Cocoa Powder 652 g / 23 oz | Hershey's | $109.95 | G10D03 |
| Carrot 2.27 kg / 5 lb |  | $36.95 | G10D03 |
