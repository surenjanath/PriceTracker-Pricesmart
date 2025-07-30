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
- **Total products scraped**: 1086
- **Total value**: $117,005.98
- **Average price**: $107.74

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1084
- **Price changes detected**: 23
- **Stock/availability changes**: 12
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 179 |
|  | 123 |
| Badia | 15 |
| Swiss | 14 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Terra Creta Greek Extra Virgin Olive Oil 500 mL / 16.9 oz | Terra Creta | $79.95 | true |
| Califia Farms Matcha Latte Almond Milk 1.4 L / 48 oz | Califia Farms | $72.95 | true |
| Galbani Galbani Mozzarella Cheese 907 g / 32 oz | Galbani | $59.95 | true |
| Sunberry Farms Organic Mango Nectar Juice - Gluten Free 3.78 L / 128 oz | Sunberry Farms | $84.95 | true |
| Chobani Greek Yogurt Vanilla 1.13 kg / 40 oz | Chobani | $85.95 | true |
| Creamery Novelties Neapolitan Ice Cream 3.78 L / 127.8 oz | Creamery Novelties | $49.95 | true |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | Kozyshack | $87.95 | true |
| Sunny D Tangy Original Orange Flavor Citrus Drink 2 Units / 1.89 L | SunnyD | $59.95 | true |
| Member's Selection Frozen Boneless Salmon Portions with Skin 680 g / 1.5 lb | Member's Selection | $169.95 | true |
| Member's Selection Cold Extracted Extra Virgin Olive Oil 2 L | Member's Selection | $134.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1163
- **Price increases**: 39
- **Price decreases**: 36
- **Average increase**: 9.4%
- **Average decrease**: -6.2%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Dare Graham Cookies with Chocolate Coating 2 Units / 280 g | $0.00 | $49.95 | $+49.95 | +100.0% | New |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $191.16 | $191.67 | $+0.51 | +0.3% | Increase |
| Frozen Bone In Pork Shoulder Sliced Tray | $67.61 | $67.71 | $+0.10 | +0.1% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $92.29 | $92.14 | $-0.15 | -0.2% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $129.65 | $129.94 | $+0.29 | +0.2% | Increase |
| Green pepper | $51.26 | $51.36 | $+0.10 | +0.2% | Increase |
| Fresh Chicken Thighs Bone In  | $80.57 | $80.49 | $-0.08 | -0.1% | Decrease |
| Frozen Whole Boneless Pork Tenderloin Vacuum Packaged | $74.34 | $73.97 | $-0.37 | -0.5% | Decrease |
| Fresh Ground Chicken Meat Bag | $262.63 | $266.02 | $+3.39 | +1.3% | Increase |
| Member's Selection Frozen Bone-In Pork Shoulder Picnic Stew, Tray | $55.49 | $55.40 | $-0.09 | -0.2% | Decrease |
| Member's Selection Frozen Lamb Neck, Bone in, skinless, Tray | $70.05 | $69.93 | $-0.12 | -0.2% | Decrease |
| Fresh Whole Chicken for Frying Bag | $262.66 | $262.36 | $-0.30 | -0.1% | Decrease |
| Frozen Lamb Shoulder Chops Tray | $99.88 | $100.04 | $+0.16 | +0.2% | Increase |
| Frozen Boneless Skinless Chicken Breast Tray | $192.03 | $198.61 | $+6.58 | +3.4% | Increase |
| Carbonell Extra Virgin Olive Oil Arbequina Special Selection 750 mL / 25.4 oz | $0.00 | $99.95 | $+99.95 | +100.0% | New |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $54.70 | $82.95 | +51.6% |
| Badia Granulated Onion 566.9 g / 20 oz | $28.45 | $37.95 | +33.4% |
| Virginia Brand Vidalia Onion Vinaigrette 1 L / 33.8 oz | $39.95 | $49.95 | +25.0% |
| Kraft Slow-Simmered Original Barbecue Sauce 2.3 kg  | $71.95 | $89.95 | +25.0% |
| Honey Bunches of Oats Sweetened Cereal with Oats and Honey 1.36 kg / 3 lb | $71.95 | $89.95 | +25.0% |
| Snickers Chocolate Bar Party Variety Pack 680.96 g / 24.02 oz | $82.95 | $102.95 | +24.1% |
| Silk Almond Original Unsweetened Beverage 6 Units / 946 mL / 32 oz | $124.45 | $152.95 | +22.9% |
| Wesson Canola Oil 4.73 L | $109.95 | $134.95 | +22.7% |
| Pringles Grab and Go Variety Pack 16 Units | $106.95 | $129.95 | +21.5% |
| Kellogg's Krispies Rice Cereal 1.19 kg / 42 oz | $107.95 | $129.95 | +20.4% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Badia Ground Turmeric 453.6 g / 16 oz  | $38.95 | $30.95 | -20.5% |
| State Fair Mini Corn Dogs 46 Units / 18.7 g / 0.66 oz | $74.95 | $59.95 | -20.0% |
| Froot Loops, Corn Pops, Apple Jacks, Cocoa Krispies and Frosted Flakes Assorted Cereal Pack 25 Units | $112.95 | $90.45 | -19.9% |
| Silk Almond Beverage with Vanilla Flavor 6 Units / 946 mL / 32 oz | $152.95 | $122.95 | -19.6% |
| Welch's Mixed Fruit Sweet Snacks 66 Units / 22.7 g | $137.95 | $111.95 | -18.8% |
| Nestle Honey Nut Cheerios 2 Units / 779 g / 27.5 oz | $132.95 | $108.95 | -18.1% |
| 4C Lemon Iced Tea Mix 2.34 kg / 5.16 lb | $79.95 | $65.95 | -17.5% |
| Pepperidge Farm Cheddar Cheese Goldfish Crackers 24 Units / 43 g / 1.5 oz | $109.95 | $90.95 | -17.3% |
| Kellogg's Nutri Grain Whole Grain and Real Fruit Bars 36 Units / 37 g / 1.3 oz | $99.95 | $83.95 | -16.0% |
| Butterball Turkey Burgers 12 Units 151 g / 5.3 oz | $184.95 | $156.95 | -15.1% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Chung Chun Teriyaki Sauce 2 Units / 560 g | Chung Chun | $57.95 | 2025-07-28 |
| Member's Selection Freshly Baked Rectangular Cheese Cake | Member's Selection | $31.95 | 2025-07-28 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Dare Graham Cookies with Chocolate Coating 2 Units / 280 g | Dare | $49.95 | G10D03 |
| Carbonell Extra Virgin Olive Oil Arbequina Special Selection 750 mL / 25.4 oz | Carbonell | $99.95 | G10D03 |
