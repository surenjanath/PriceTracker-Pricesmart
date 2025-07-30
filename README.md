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
- **Total products scraped**: 1074
- **Total value**: $116,197.70
- **Average price**: $108.19

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1074
- **Price changes detected**: 0
- **Stock/availability changes**: 0
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 179 |
|  | 122 |
| Badia | 15 |
| Swiss | 14 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Califia Farms Matcha Latte Almond Milk 1.4 L / 48 oz | Califia Farms | $72.95 | true |
| Sunberry Farms Organic Mango Nectar Juice - Gluten Free 3.78 L / 128 oz | Sunberry Farms | $84.95 | true |
| Pringles Mingles Cheddar and Sour Cream Puffed Snacks 2 Units / 155 g / 5.5 oz | Pringles | $69.95 | true |
| Sunny Fruits Organic Dried Apricots 10 Units / 50 g / 1.76 oz | Sunny Fruits | $59.95 | true |
| Welch's Passion Fruit Juice Zero Sugar 1.74 L / 59 oz | Welch's | $32.95 | true |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | Kozyshack | $87.95 | true |
| Goya Coconut Milk 3 Units / 400 mL / 13.5 oz | Goya | $65.95 | true |
| Stauffers Snaps Crunchy Lemon-Flavored Cookies 397 g / 14 oz | Stauffers | $49.95 | true |
| Blue Waters Sparkling Drink with Cran and Grape Flavor 12 Units / 330 mL / 11.15 oz | Blue Waters | $25.95 | true |
| Sensible Portions Vegetable Straws with Sea Salt 666 g / 23.5 oz | Sensible Portions | $109.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1190
- **Price increases**: 47
- **Price decreases**: 54
- **Average increase**: 8.0%
- **Average decrease**: -7.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Frozen Bone In Pork Shoulder Sliced Tray | $67.71 | $67.80 | $+0.09 | +0.1% | Increase |
| Mrs. Field's Chocolate Chip Cookie 20 Units / 59 g  / 2.1 oz  | $109.95 | $117.95 | $+8.00 | +7.3% | Increase |
| Fresh Boneless Beef Eye of Round Whole Piece Vacuum Packaged | $384.59 | $382.41 | $-2.18 | -0.6% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $129.94 | $130.09 | $+0.15 | +0.1% | Increase |
| Angel Parboiled Rice Extra Long Grain 9 kg / 19.8 lb | $84.95 | $83.95 | $-1.00 | -1.2% | Decrease |
| Green pepper | $51.36 | $51.26 | $-0.10 | -0.2% | Decrease |
| Fresh Chicken Thighs Bone In  | $80.49 | $80.57 | $+0.08 | +0.1% | Increase |
| Gouda Cheese Block | $71.08 | $71.21 | $+0.13 | +0.2% | Increase |
| Fresh Ground Chicken Meat Bag | $266.02 | $265.39 | $-0.63 | -0.2% | Decrease |
| Assorted Peppers | $36.58 | $36.21 | $-0.37 | -1.0% | Decrease |
| Fresh Chicken Mixed Parts Tray | $87.59 | $87.48 | $-0.11 | -0.1% | Decrease |
| Fresh Ground Chicken Tray | $87.13 | $87.25 | $+0.12 | +0.1% | Increase |
| Member's Selection Frozen Bone-In Pork Shoulder Picnic Stew, Tray | $55.40 | $55.49 | $+0.09 | +0.2% | Increase |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | $-55.25 | -69.1% | Decrease |
| Frozen Boneless Skinless Chicken Breast Tray | $198.61 | $198.05 | $-0.56 | -0.3% | Decrease |

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
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Badia Ground Turmeric 453.6 g / 16 oz  | $38.95 | $30.95 | -20.5% |
| State Fair Mini Corn Dogs 46 Units / 18.7 g / 0.66 oz | $74.95 | $59.95 | -20.0% |
| Froot Loops, Corn Pops, Apple Jacks, Cocoa Krispies and Frosted Flakes Assorted Cereal Pack 25 Units | $112.95 | $90.45 | -19.9% |
| Silk Almond Beverage with Vanilla Flavor 6 Units / 946 mL / 32 oz | $152.95 | $122.95 | -19.6% |
| Welch's Mixed Fruit Sweet Snacks 66 Units / 22.7 g | $137.95 | $111.95 | -18.8% |
| Nestle Honey Nut Cheerios 2 Units / 779 g / 27.5 oz | $132.95 | $108.95 | -18.1% |
| 4C Lemon Iced Tea Mix 2.34 kg / 5.16 lb | $79.95 | $65.95 | -17.5% |
| Pepperidge Farm Cheddar Cheese Goldfish Crackers 24 Units / 43 g / 1.5 oz | $109.95 | $90.95 | -17.3% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Dare Viva Puffs Strawberry Cookies 2 Units / 300 g | Dare | $49.95 | 2025-07-30 |
| Avocado Mesh 5 Units |  | $34.95 | 2025-07-30 |
| Sweet Cane White Sugar 2 Units / 1.8 kg / 3.96 lb | Sweet Cane | $39.95 | 2025-07-30 |
| Just About Foods Mango Organic Dried Mango 15 Units / 28.35 g / 0.89 oz | Just About Foods | $40.70 | 2025-07-30 |
| Narcissus Whole Mushrooms 8 Units / 184 g | Narcissus | $55.95 | 2025-07-30 |
| Southco Parboiled Rice 9 kg / 19.8 lb | Southco | $76.95 | 2025-07-30 |
| Lucozade  Medley  Energy Drink 12 Units / 360 ml   | Lucozade | $144.95 | 2025-07-30 |
| Wheat Crips Wheat Germ Cookies 18 Units / 32 g | Wheat Crisps | $44.95 | 2025-07-30 |
| Nature's Pride Red Beans 1.8 kg / 4 lb | Nature's Pride | $44.95 | 2025-07-30 |
| Tosh Bran and Honey Cookies 3 Units / 243 g / 8.57 oz | Tosh | $48.95 | 2025-07-30 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Angela Mia Pizza Sauce 3 kg / 6.61 lb | Angela Mia | $99.95 | G10D03 |
| Dare Graham Cookies with Chocolate Coating 2 Units / 280 g | Dare | $49.95 | G10D03 |
| Carbonell Extra Virgin Olive Oil Arbequina Special Selection 750 mL / 25.4 oz | Carbonell | $99.95 | G10D03 |
