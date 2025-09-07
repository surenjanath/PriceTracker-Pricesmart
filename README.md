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
- **Total products scraped**: 1084
- **Total value**: $116,539.24
- **Average price**: $107.51

## Database Changes
- **New products added**: 4
- **Existing products updated**: 1080
- **Price changes detected**: 34
- **Stock/availability changes**: 11
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 182 |
|  | 132 |
| Badia | 19 |
| Swiss | 13 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Nilo Coconut Water 12 Units / 320 mL / 10.82 oz | Nilo | $124.95 | true |
| Cheez-It White and Jack Cheddar Crackers 2 Pack 351 g / 12.4 oz | CheezIt | $89.95 | true |
| Tostitos Snacks White Corn Chips Nachos / 283 g / 10 oz | Tostitos | $50.95 | true |
| Pafritas Paprika Flavor Potato Chips 500 g / 1.1 lb | Pafritas | $86.95 | true |
| Nilo Soursop Juice 12 Units / 320 mL / 10.82 oz | Nilo | $129.95 | true |
| Member's Selection Sliced Assorted Cheese Pack 907 g / 32 oz | Member's Selection | $73.95 | true |
| Crix Steelpan Original Cookies in Collectible Tin 768 g | Crix | $59.95 | true |
| Member's Selection Thai Jasmine Long Grain Rice 9.07 kg / 20 lb | Member's Selection | $149.95 | true |
| Kawan Plain Paratha 25 Units 2 kg / 4.4 lb | Kawan | $99.95 | true |
| Badia All Purpose Marinade Seasoning 591 mL / 20 oz  | Badia | $21.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1243
- **Price increases**: 575
- **Price decreases**: 597
- **Average increase**: 5.9%
- **Average decrease**: -4.1%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Mandarin Orange Chicken 1.2 kg / 2.6 lb | $157.95 | $179.95 | $+22.00 | +13.9% | Increase |
| Carolina Ground Turkey Meat, 2.3 kg / 5 lb | $0.00 | $111.07 | $+111.07 | +100.0% | New |
| President Brie Cheese 555 g / 1.2 lb | $74.95 | $75.95 | $+1.00 | +1.3% | Increase |
|  Eggplant 793 g / 1.75 lb | $0.00 | $67.95 | $+67.95 | +100.0% | New |
| Dewlands Passion Fruit and Apple Juice 3 Units / 1 L | $0.00 | $59.95 | $+59.95 | +100.0% | New |
| Tostitos Santa Elena Chips 430 g  / 15.17 oz | $0.00 | $34.95 | $+34.95 | +100.0% | New |
| Ginger 680 g / 1.5 | $32.95 | $34.95 | $+2.00 | +6.1% | Increase |
| Leclerc Summer Cookies with Raspberry and Berry Flavor 2 Units / 300 g | $47.95 | $41.70 | $-6.25 | -13.0% | Decrease |
| Gouda Cheese Block | $71.89 | $72.03 | $+0.14 | +0.2% | Increase |
| Avocado Mesh 5 Units | $44.95 | $47.95 | $+3.00 | +6.7% | Increase |
| Fresh Chicken Mixed Parts Tray | $84.29 | $84.07 | $-0.22 | -0.3% | Decrease |
| Fresh Seasoned BBQ Chicken Quarters Bag | $88.46 | $88.55 | $+0.09 | +0.1% | Increase |
| Fresh Ground Chicken Meat Bag | $262.42 | $265.81 | $+3.39 | +1.3% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $136.27 | $136.42 | $+0.15 | +0.1% | Increase |
| Green Cabbage 1.3 kg / 2.9 lb | $31.95 | $19.70 | $-12.25 | -38.3% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| Purple Cabbage Unit | $14.70 | $29.95 | +103.7% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $39.70 | $79.95 | +101.4% |
| Frito Lay Assortment Box 24 Units | $49.70 | $99.95 | +101.1% |
| Member's Selection Mocha Flavor Cold Coffee Drink 9 Units / 405 mL / 13.7 oz | $105.70 | $176.95 | +67.4% |
| Fresh Celery  | $9.70 | $14.95 | +54.1% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Purple Cabbage Unit | $29.95 | $14.70 | -50.9% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $79.95 | $39.70 | -50.3% |
| Frito Lay Assortment Box 24 Units | $99.95 | $49.70 | -50.3% |
| Angie's Boom Chicka Pop Sweet and Salty Popcorn 652 g / 23 oz | $99.95 | $49.70 | -50.3% |
| Cap'n Crunch's Crispy Berry Flavored Cereal 2 Units / 293 g | $52.70 | $29.70 | -43.6% |
| Fresh Regular Tomato | $47.85 | $28.51 | -40.4% |
| Fresh Celery  | $15.95 | $9.70 | -39.2% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Frozen Sliced Turkey Drumsticks |  | $98.45 | 2025-09-06 |
| Florida's Natural Orange Juice 2.63 L / 89 oz | Florida's Natural | $87.95 | 2025-09-05 |
| Pink Lady Apple 1.81 kg / 4 lb |  | $81.95 | 2025-09-04 |
| Kretcshmer Wheat Germ Honey 2 units / 311 g | Kretcshmer | $75.95 | 2025-09-04 |
| Sundays Assorted Ice Creams 16 Units / 90 mL / 3 oz | Sundays | $79.95 | 2025-09-04 |
| Ankara Shell Pasta 4 Units / 500 g | Ankara | $35.70 | 2025-09-04 |
| McCain Hashbrowns 1.3 kg / 2.8 lb | McCain | $49.95 | 2025-09-04 |
| Sea Best Raw Lobster Cake 762 g / 1.68 lb | Sea Best | $94.95 | 2025-09-03 |
| Fresh Red Apples 1.36 kg / 3 lb |  | $49.95 | 2025-09-03 |
| Mountain Peak Instant Coffee 170 g | Mountain Peak | $53.95 | 2025-09-03 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Carolina Ground Turkey Meat, 2.3 kg / 5 lb | Carolina Turkey | $111.07 | G10D03 |
|  Eggplant 793 g / 1.75 lb |  | $67.95 | G10D03 |
| Dewlands Passion Fruit and Apple Juice 3 Units / 1 L | Dewlands | $59.95 | G10D03 |
| Tostitos Santa Elena Chips 430 g  / 15.17 oz | Tostitos | $34.95 | G10D03 |
