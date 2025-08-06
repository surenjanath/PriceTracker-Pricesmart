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
- **Total products scraped**: 1092
- **Total value**: $118,573.68
- **Average price**: $108.58

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1091
- **Price changes detected**: 32
- **Stock/availability changes**: 24
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 185 |
|  | 125 |
| Badia | 18 |
| Swiss | 15 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Califia Farms Matcha Latte Almond Milk 1.4 L / 48 oz | Califia Farms | $69.95 | true |
| Sunberry Farms Organic Mango Nectar Juice - Gluten Free 3.78 L / 128 oz | Sunberry Farms | $74.95 | true |
| Pringles Mingles Cheddar and Sour Cream Puffed Snacks 2 Units / 155 g / 5.5 oz | Pringles | $69.95 | true |
| Sunny Fruits Organic Dried Apricots 10 Units / 50 g / 1.76 oz | Sunny Fruits | $59.95 | true |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | Kozyshack | $87.95 | true |
| Goya Coconut Milk 3 Units / 400 mL / 13.5 oz | Goya | $65.95 | true |
| Stauffers Snaps Crunchy Lemon-Flavored Cookies 397 g / 14 oz | Stauffers | $49.95 | true |
| Blue Waters Sparkling Drink with Cran and Grape Flavor 12 Units / 330 mL / 11.15 oz | Blue Waters | $25.95 | true |
| Sensible Portions Vegetable Straws with Sea Salt 666 g / 23.5 oz | Sensible Portions | $109.95 | true |
| Member's Selection Frozen Boneless Salmon Portions with Skin 680 g / 1.5 lb | Member's Selection | $169.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1476
- **Price increases**: 183
- **Price decreases**: 180
- **Average increase**: 5.9%
- **Average decrease**: -3.6%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Reny Picot Brie with Peppercorns 396 g /14 oz | $0.00 | $68.95 | $+68.95 | +100.0% | New |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $160.59 | $160.86 | $+0.27 | +0.2% | Increase |
| Frozen Bone In Pork Shoulder Sliced Tray | $67.61 | $67.51 | $-0.10 | -0.1% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $93.99 | $94.14 | $+0.15 | +0.2% | Increase |
| Chilled Chicken Gizzard Tray Pack | $55.79 | $55.87 | $+0.08 | +0.1% | Increase |
| Fresh Chicken Leg Quarters Tray | $89.71 | $89.81 | $+0.10 | +0.1% | Increase |
| Fresh Seasoned BBQ Chicken Quarters Bag | $89.72 | $89.63 | $-0.09 | -0.1% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $139.77 | $139.47 | $-0.30 | -0.2% | Decrease |
| Fresh Ground Chicken Meat Bag | $264.96 | $262.21 | $-2.75 | -1.0% | Decrease |
| Assorted Peppers | $36.14 | $35.99 | $-0.15 | -0.4% | Decrease |
| Fresh Ground Chicken Tray | $85.83 | $85.95 | $+0.12 | +0.1% | Increase |
| Member's Selection Frozen Lamb Neck, Bone in, skinless, Tray | $67.48 | $67.37 | $-0.11 | -0.2% | Decrease |
| Nutrina Chilled Whole Chicken Bag | $307.59 | $308.34 | $+0.75 | +0.2% | Increase |
| Member's Selection Frozen Bone-In Lamb Stew Bag | $67.98 | $67.86 | $-0.12 | -0.2% | Decrease |
| Member's Selection Frozen Boneless Pork Loin Roast Tray | $104.84 | $104.42 | $-0.42 | -0.4% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $54.70 | $82.95 | +51.6% |
| Lush Natural Refreshing Apple Flavored Drink 36 Units / 200 ml | $52.70 | $72.95 | +38.4% |
| Badia Granulated Onion 566.9 g / 20 oz | $28.45 | $37.95 | +33.4% |
| Virginia Brand Vidalia Onion Vinaigrette 1 L / 33.8 oz | $39.95 | $49.95 | +25.0% |
| Kraft Slow-Simmered Original Barbecue Sauce 2.3 kg  | $71.95 | $89.95 | +25.0% |
| Honey Bunches of Oats Sweetened Cereal with Oats and Honey 1.36 kg / 3 lb | $71.95 | $89.95 | +25.0% |
| Snickers Chocolate Bar Party Variety Pack 680.96 g / 24.02 oz | $82.95 | $102.95 | +24.1% |
| Silk Almond Original Unsweetened Beverage 6 Units / 946 mL / 32 oz | $124.45 | $152.95 | +22.9% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Okra 30 Units | $26.95 | $19.95 | -26.0% |
| Badia Ground Turmeric 453.6 g / 16 oz  | $38.95 | $30.95 | -20.5% |
| Iceberg Lettuce Unit | $34.95 | $27.95 | -20.0% |
| State Fair Mini Corn Dogs 46 Units / 18.7 g / 0.66 oz | $74.95 | $59.95 | -20.0% |
| Froot Loops, Corn Pops, Apple Jacks, Cocoa Krispies and Frosted Flakes Assorted Cereal Pack 25 Units | $112.95 | $90.45 | -19.9% |
| Silk Almond Beverage with Vanilla Flavor 6 Units / 946 mL / 32 oz | $152.95 | $122.95 | -19.6% |
| Welch's Mixed Fruit Sweet Snacks 66 Units / 22.7 g | $137.95 | $111.95 | -18.8% |
| Nestle Honey Nut Cheerios 2 Units / 779 g / 27.5 oz | $132.95 | $108.95 | -18.1% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Busta Assorted Soft Drinks 24 Units / 500 mL | Busta | $39.70 | 2025-08-05 |
| Rajapuri Coconut Flavor Curry Powder 620 g / 22 oz | Rajapuri | $56.95 | 2025-08-04 |
| Swift Frozen Chilled Pork Ribs Kansas City Style BBQ Vacuum Pack  | Swift | $140.34 | 2025-08-04 |
| Dutch Yellow Onions 3 lb / 1.3 kg |  | $11.45 | 2025-08-02 |
| La Mere Poulard Selection Cookie Variety 750 g / 26 oz | La Mere Poulard | $47.70 | 2025-07-31 |
| All Inklusive Triple Berries and Strawberry Yogurt Cereal 2 Units / 500 g | All Inklusive | $94.95 | 2025-07-31 |
| Dare Viva Puffs Strawberry Cookies 2 Units / 300 g | Dare | $49.95 | 2025-07-30 |
| Avocado Mesh 5 Units |  | $34.95 | 2025-07-30 |
| Sweet Cane White Sugar 2 Units / 1.8 kg / 3.96 lb | Sweet Cane | $39.95 | 2025-07-30 |
| Just About Foods Mango Organic Dried Mango 15 Units / 28.35 g / 0.89 oz | Just About Foods | $40.70 | 2025-07-30 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Reny Picot Brie with Peppercorns 396 g /14 oz | Reny Picot | $68.95 | G10D03 |
