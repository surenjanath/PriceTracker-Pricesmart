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
- **Total value**: $117,635.64
- **Average price**: $109.53

## Database Changes
- **New products added**: 4
- **Existing products updated**: 1070
- **Price changes detected**: 35
- **Stock/availability changes**: 6
- **Discontinued products**: 20

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 184 |
|  | 132 |
| Badia | 18 |
| Swiss | 13 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Lipton Yellow Label Black Tea Sachets 312 Units / 2.2 g / 0.07 oz | Lipton | $104.95 | true |
| Badia All Purpose Seasoning 14 Spices 567 g / 20 oz | Badia | $69.95 | true |
| Pringles Mingles Cheddar and Sour Cream Puffed Snacks 2 Units / 155 g / 5.5 oz | Pringles | $69.95 | true |
| Sensible Portions Vegetable Straws with Sea Salt 666 g / 23.5 oz | Sensible Portions | $109.95 | true |
| Member's Selection Shredded Mexican-Style Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $108.95 | true |
| Member's Selection Shredded Mozzarella Cheese 5 Units / 453 g / 1 lb | Member's Selection | $149.95 | true |
| Member's Selection Shredded Mozzarella Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $97.95 | true |
| Member's Selection Shredded Cheddar Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $91.95 | true |
| Florida's Natural Orange Juice 2.63 L / 89 oz | Florida's Natural | $87.95 | true |
| Chobani Zero Sugar Yogurt 16 Units / 150 g / 5.3 oz | Chobani | $169.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1993
- **Price increases**: 397
- **Price decreases**: 448
- **Average increase**: 5.1%
- **Average decrease**: -4.4%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Fresh Regular Tomato | $39.39 | $39.55 | $+0.16 | +0.4% | Increase |
| Fresh Chicken Thighs Boneless Bag | $305.36 | $314.79 | $+9.43 | +3.1% | Increase |
| Edwards Key Lime Pie 861 g / 1.9 lb | $0.00 | $68.95 | $+68.95 | +100.0% | New |
| Member's Selection Pecan Pralines  850 g / 30 oz | $0.00 | $129.95 | $+129.95 | +100.0% | New |
| Nilo Soursop Juice 12 Units / 320 mL / 10.82 oz | $0.00 | $129.95 | $+129.95 | +100.0% | New |
| Fresh Chicken Thighs Boneless Tray | $72.61 | $72.74 | $+0.13 | +0.2% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $95.04 | $93.77 | $-1.27 | -1.3% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $137.69 | $135.54 | $-2.15 | -1.6% | Decrease |
| Frozen Bone In Baby Back Ribs Vacuum Packaged Case | $1899.00 | $1879.00 | $-20.00 | -1.1% | Decrease |
| Green pepper | $41.26 | $41.17 | $-0.09 | -0.2% | Decrease |
| Fresh Bone-in Chicken Thighs Tray | $81.00 | $80.92 | $-0.08 | -0.1% | Decrease |
| Fresh Chicken Mixed Parts Tray | $86.60 | $86.82 | $+0.22 | +0.3% | Increase |
| Chilled Skinless Boneless Beef Ribeye Steak Vacuum Package Whole Piece | $2180.13 | $2157.01 | $-23.12 | -1.1% | Decrease |
| Member's Selection Frozen Lamb Neck, Bone in, skinless, Tray | $65.72 | $65.83 | $+0.11 | +0.2% | Increase |
| Member's Selection Sliced Assorted Cheese Pack 907 g / 32 oz | $0.00 | $87.95 | $+87.95 | +100.0% | New |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $39.70 | $79.95 | +101.4% |
| Member's Selection Mocha Flavor Cold Coffee Drink 9 Units / 405 mL / 13.7 oz | $105.70 | $176.95 | +67.4% |
| Fresh Celery  | $9.70 | $14.95 | +54.1% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $54.70 | $82.95 | +51.6% |
| Lush Natural Refreshing Apple Flavored Drink 36 Units / 200 ml | $52.70 | $72.95 | +38.4% |
| Avocado Mesh 5 Units | $34.95 | $47.95 | +37.2% |
| Iceberg Lettuce Unit | $19.70 | $26.95 | +36.8% |
| Fresh Regular Tomato | $28.99 | $38.99 | +34.5% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Purple Cabbage Unit | $29.95 | $14.70 | -50.9% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $79.95 | $39.70 | -50.3% |
| Frito Lay Assortment Box 24 Units | $99.95 | $49.70 | -50.3% |
| Angie's Boom Chicka Pop Sweet and Salty Popcorn 652 g / 23 oz | $99.95 | $49.70 | -50.3% |
| Fresh Regular Tomato | $47.85 | $28.51 | -40.4% |
| Fresh Celery  | $15.95 | $9.70 | -39.2% |
| Real Coco Organic Coconut Water 12 Units / 500 mL / 17 oz | $129.95 | $90.70 | -30.2% |
| Iceberg Lettuce Unit | $27.95 | $19.70 | -29.5% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Dare Vinta Crackers with Cereals and Seeds 2 Units / 200 g | Dare | $19.70 | 2025-08-18 |
| Nescafe Latte Assorted Flavors 3 Units / 14.5 g | Nescafé | $79.95 | 2025-08-18 |
| Nongshim Kimchi Flavor Noodle Soup 4 Units / 120 g / 4.23 oz | Nongshim | $39.95 | 2025-08-18 |
| Jayone Yizu Citrus Flavored Sweet Crispy Rice Rolls 2 Units / 80 g | Jayone | $39.95 | 2025-08-18 |
| Svelty Skimmed Milk 6 Units / 1 L | Svelty | $94.95 | 2025-08-18 |
| Ginseng Up Mixed Bottles 24 Units/275 ml | Ginseng Up | $151.95 | 2025-08-18 |
| Nesquik Ice Cream Flavor Chocolate Powder Mix 525 g / 1.15 lb | Nesquik | $44.95 | 2025-08-18 |
| Bertie's Pimento Peppers Sauce 750 mL | Bertie's | $54.95 | 2025-08-18 |
| Russco's Honey Mustard Sauce 750 mL / 25 oz | Russco's | $39.95 | 2025-08-18 |
| Schweppes Chaser Assorted Flavor Soft Drink 24 Units / 237 mL | Schweppes | $84.95 | 2025-08-18 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Edwards Key Lime Pie 861 g / 1.9 lb | Edward's | $68.95 | G10D03 |
| Member's Selection Pecan Pralines  850 g / 30 oz | Member's Selection | $129.95 | G10D03 |
| Nilo Soursop Juice 12 Units / 320 mL / 10.82 oz | Nilo | $129.95 | G10D03 |
| Member's Selection Sliced Assorted Cheese Pack 907 g / 32 oz | Member's Selection | $87.95 | G10D03 |
