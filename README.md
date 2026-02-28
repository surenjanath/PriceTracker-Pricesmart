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
- **Total products scraped**: 1161
- **Total value**: $129,132.40
- **Average price**: $111.23

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1160
- **Price changes detected**: 23
- **Stock/availability changes**: 15
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 186 |
|  | 136 |
| Badia | 18 |
| Swiss | 14 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Organic Trail Mix with Cranberries 737 g / 26 oz | Member's Selection | $164.95 | true |
| Happy Village Organic Fig and Nut Mini Bars 24 Units / 20 g / 0.7 oz | Happy Village | $146.95 | true |
| Royal Asia Honey Walnut Shrimp 907 g / 2 lb | Royal Asia | $169.95 | true |
| Carapelli Organic Extra Virgin Olive Oil 880 g / 33.8 oz | Carapelli | $114.95 | true |
| Maeva Extra Virgin Olive Oil Spray 2 Units / 400 mL / 13.5 oz | Maeva | $109.95 | true |
| Belgioioso Artigiano Vino Rosso Cheese 453 g / 16 oz | Belgioioso | $99.95 | true |
| Tropical Gold Breaded Calamari Rings 2 Units / 454 g / 1 lb | Tropical Gold | $92.95 | true |
| Moy Park Frozen Chicken Drumstick 10 kg / 22 lb | Moy Park | $349.95 | true |
| President Brie Cheese Spreadable 3 Units / 139 g / 4.9 oz | President | $74.95 | true |
| Wellsley Farms Crab Cakes 510 g / 1 lb | Wellsley Farms | $219.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1077
- **Price increases**: 490
- **Price decreases**: 551
- **Average increase**: 9.1%
- **Average decrease**: -5.2%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Ocean Delight Frozen Blue Crab Meat 680 g / 1.5 lb | $0.00 | $124.95 | $+124.95 | +100.0% | New |
| Ribeye Choice Fillet Fresh Tray | $259.75 | $260.37 | $+0.62 | +0.2% | Increase |
| Frozen Pork Belly Skin On Sliced Tray  | $114.91 | $114.67 | $-0.24 | -0.2% | Decrease |
| Fresh Chicken Breast Bone In Tray | $95.71 | $95.80 | $+0.09 | +0.1% | Increase |
| Frozen Whole Boneless Pork Tenderloin Vacuum Packaged | $75.08 | $74.82 | $-0.26 | -0.3% | Decrease |
| Pork Belly with Skin Frozen Vacuum Packaged | $193.23 | $191.72 | $-1.51 | -0.8% | Decrease |
| Mini Sweet Peppers 454 g / 1 lb | $36.95 | $42.95 | $+6.00 | +16.2% | Increase |
| Fresh Chicken Mixed Parts Tray | $90.78 | $90.67 | $-0.11 | -0.1% | Decrease |
| Nutrina Chilled Whole Chicken Bag | $325.86 | $324.36 | $-1.50 | -0.5% | Decrease |
| Fresh Chicken Leg Quarters Tray | $92.21 | $92.31 | $+0.10 | +0.1% | Increase |
| Fine Choice Fresh Marinated Chicken Tray | $86.30 | $86.39 | $+0.09 | +0.1% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $155.15 | $155.00 | $-0.15 | -0.1% | Decrease |
| Frozen Boneless Skinless Chicken Breast Tray | $127.09 | $126.13 | $-0.96 | -0.8% | Decrease |
| Dutch Potatoes 4.54 kg / 10 lb | $24.95 | $27.95 | $+3.00 | +12.0% | Increase |
| Fresh Ground Chicken Meat Bag | $270.89 | $271.10 | $+0.21 | +0.1% | Increase |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Carrot 2.27 kg / 5 lb | $9.70 | $37.95 | +291.2% |
| Silk Unsweetened Original 2 Units 1.89 L / 64 oz | $29.70 | $99.95 | +236.5% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Hillshire Farm Ham Mix 3 Units / 454 g / 16 oz | $194.95 | $69.70 | -64.2% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $109.95 | $39.70 | -63.9% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Fresh Beef Eye of Round Case |  | $4216.42 | 2026-02-27 |
| Glazed Fruits 908 g / 2 lb |  | $53.95 | 2026-02-26 |
| Ferrero Rocher Hazelnut & Chocolate Cream Filled Chocolates 24 Units / 12.5 g / 0.4 oz | Ferrero Rocher | $109.95 | 2026-02-26 |
| Angel Parboiled Rice 4 kg | Angel | $39.95 | 2026-02-25 |
| Nature's Pride Pigeon Peas 1.8 kg / 4 lb | Nature's Pride | $41.95 | 2026-02-25 |
| Caffe D'Vita Piña Colada Powdered Drink Mix 907 g / 32 oz | Caffe D'Vita | $35.70 | 2026-02-25 |
| McVitie's Ginger Nut Biscuits 4 Units / 250 g | McVitie's | $37.70 | 2026-02-25 |
| Southco Parboiled Rice 9 kg / 19.8 lb | Southco | $81.95 | 2026-02-25 |
| Kiss Assorted Flavor Pastries 9 Units | Kiss | $39.95 | 2026-02-25 |
| Best Fruit Premium Dehydrated Coconut 5 Units / 80 g / 2.82 oz | Best Fruit | $59.70 | 2026-02-25 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Ocean Delight Frozen Blue Crab Meat 680 g / 1.5 lb | Ocean Delight | $124.95 | G10D03 |
