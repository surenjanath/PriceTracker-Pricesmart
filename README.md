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
- **Total products scraped**: 1097
- **Total value**: $118,060.69
- **Average price**: $107.62

## Database Changes
- **New products added**: 6
- **Existing products updated**: 1091
- **Price changes detected**: 103
- **Stock/availability changes**: 9
- **Discontinued products**: 5

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 183 |
|  | 138 |
| Badia | 19 |
| Swiss | 13 |
| Kiss | 13 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Thai Jasmine Long Grain Rice 9.07 kg / 20 lb | Member's Selection | $149.95 | true |
| Nilo Soursop Juice 12 Units / 320 mL / 10.82 oz | Nilo | $139.95 | true |
| Idahoan Classic Instant Mashed Potatoes 1.47 kg / 3.25 lb | Idahoan | $109.95 | true |
| Loc Maria Biscuits Assorted French Cookies Butter and Salted Caramel 441 g / 15.6 oz | Loc Maria Biscuits | $156.95 | true |
| Karnis Hummus Mix 3 Units / 226 g / 7.97 oz | Karnis | $82.95 | true |
| Annie's Organic Macaroni and Cheese Variety Pack 12 Units / 170 g | Annies | $239.95 | true |
| Kellogg’s Assorted Cereals Corn Pops, Froot Loops & Apple Jacks 3 Bags / 1.05 kg / 37.3 oz | Kellogg's | $106.95 | true |
| Dewlands Passion Fruit and Apple Juice 3 Units / 1 L | Dewlands | $59.95 | true |
| Badia Mojo Rub Citrus Blend 680.4 g / 24 oz  | Badia | $89.95 | true |
| Nesquick Liquid Milk Drink with Cocoa Flavor 12 Units / 250 mL | Nesquik | $77.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1318
- **Price increases**: 707
- **Price decreases**: 549
- **Average increase**: 6.1%
- **Average decrease**: -3.6%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Violife Just Like Mozzarella Shredded 453 g / 1 lb | $92.95 | $94.95 | $+2.00 | +2.2% | Increase |
| Sabatasso's French Bread Pizza 9 Units / 152 g / 5.4 oz | $129.95 | $134.95 | $+5.00 | +3.8% | Increase |
| Breakstone's Sour Cream 680 g / 1.5 lb  | $41.95 | $42.95 | $+1.00 | +2.4% | Increase |
| Kirkland Signature Dried Blueberries 567 g / 1 lb  | $99.95 | $107.95 | $+8.00 | +8.0% | Increase |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $82.95 | $+3.00 | +3.8% | Increase |
| Tropicland Stir Fry Vegetables 2.26 kg / 5 lb | $99.95 | $104.95 | $+5.00 | +5.0% | Increase |
| Dietz & Watson Sliced Breast Turkey 454 g / 1 lb | $89.95 | $92.95 | $+3.00 | +3.3% | Increase |
| Chobani Greek Yogurt 907 g / 32 oz | $67.95 | $68.95 | $+1.00 | +1.5% | Increase |
| Member's Selection Havarti Cheese 680 g / 1.5 lb  | $87.95 | $89.95 | $+2.00 | +2.3% | Increase |
| Member's Selection Sliced Muenster Cheese 680 g / 1.5 lb | $87.95 | $89.95 | $+2.00 | +2.3% | Increase |
| Member’s Selection Breaded Mozzarella Sticks 2.04 kg / 4.5 lb | $149.95 | $152.95 | $+3.00 | +2.0% | Increase |
| My Mochi Peppermint Ice Cream 420 g / 15 oz | $0.00 | $99.95 | $+99.95 | +100.0% | New |
| Arcor Chocolate Rocklets 18 Units / 40 g | $72.95 | $59.70 | $-13.25 | -18.2% | Decrease |
| Ankara Penne Pasta 4 Units / 500 g | $0.00 | $41.95 | $+41.95 | +100.0% | New |
| Member's Selection Supreme Pizza 2 Units / 716 g / 1.57 lb | $0.00 | $123.95 | $+123.95 | +100.0% | New |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $29.70 | $89.95 | +202.9% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| Purple Cabbage Unit | $14.70 | $29.95 | +103.7% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $39.70 | $79.95 | +101.4% |
| Frito Lay Assortment Box 24 Units | $49.70 | $99.95 | +101.1% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Purple Cabbage Unit | $29.95 | $14.70 | -50.9% |
|  Eggplant 793 g / 1.75 lb | $59.95 | $29.70 | -50.5% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $79.95 | $39.70 | -50.3% |
| Frito Lay Assortment Box 24 Units | $99.95 | $49.70 | -50.3% |
| Angie's Boom Chicka Pop Sweet and Salty Popcorn 652 g / 23 oz | $99.95 | $49.70 | -50.3% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Mowi Lightly Smoked Salmon 680 g / 1.5 lb | Mowi | $144.70 | 2025-09-18 |
| Member’s Selection Coconut Swiss Roll  | Member's Selection | $31.95 | 2025-09-18 |
| Member's Selection Red Velvet Swiss Roll 230 g / 0.50 lb | Member's Selection | $41.95 | 2025-09-18 |
| Arcor Mogul Extreme Sour Gummy Bears 10 Units / 50g | Arcor | $25.70 | 2025-09-18 |
| Cap'n Crunch's Crispy Berry Flavored Cereal 2 Units / 293 g | Capn Crunch | $29.70 | 2025-09-18 |
| Member's Selection Freshly Baked Sweet and Creamy Vanilla Cake 80 to 100 Slices | Member's Selection | $399.95 | 2025-09-17 |
| Maison Perrier Sparkling Flavored Water Strawberry Flavor 10 Units / 250 mL | Maison Perrier | $89.95 | 2025-09-15 |
| Frozen Bone-In Pork Loin Center Cut Whole Piece Vacuum Packaged |  | $751.20 | 2025-09-15 |
| Sunberry Farms Organic Guava Nectar Juice - Gluten Free 3.78 L / 128 oz | Sunberry Farms | $84.95 | 2025-09-14 |
| Hoody's Keto Matcha Trail Mix 907 g / 32 oz  | Hoody's | $114.70 | 2025-09-12 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| My Mochi Peppermint Ice Cream 420 g / 15 oz | My Mochi | $99.95 | G10D03 |
| Ankara Penne Pasta 4 Units / 500 g | Ankara | $41.95 | G10D03 |
| Member's Selection Supreme Pizza 2 Units / 716 g / 1.57 lb | Member's Selection | $123.95 | G10D03 |
| Member’s Selection Freshly Prepared Holiday Cake | Member's Selection | $89.95 | G10D03 |
| Upper Crust Bakery Mini Soft and Creamy Brownie Pastries 32 Units | Upper Crust Bakery | $102.95 | G10D03 |
| Member's Selection Pepperoni Pizza 2 Units / 656 g / 1.44 lb | Member's Selection | $123.95 | G10D03 |
