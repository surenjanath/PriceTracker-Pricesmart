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
- **Total products scraped**: 1098
- **Total value**: $118,515.35
- **Average price**: $107.94

## Database Changes
- **New products added**: 5
- **Existing products updated**: 1093
- **Price changes detected**: 25
- **Stock/availability changes**: 11
- **Discontinued products**: 3

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 183 |
|  | 134 |
| Badia | 18 |
| Swiss | 15 |
| Kiss | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Lipton Yellow Label Black Tea Sachets 312 Units / 2.2 g / 0.07 oz | Lipton | $104.95 | true |
| Badia All Purpose Seasoning 14 Spices 567 g / 20 oz | Badia | $69.75 | true |
| Pringles Mingles Cheddar and Sour Cream Puffed Snacks 2 Units / 155 g / 5.5 oz | Pringles | $69.95 | true |
| Member's Selection Shredded Mozzarella Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $97.95 | true |
| Sensible Portions Vegetable Straws with Sea Salt 666 g / 23.5 oz | Sensible Portions | $109.95 | true |
| Member's Selection Shredded Mexican-Style Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $108.95 | true |
| Member's Selection Shredded Mozzarella Cheese 5 Units / 453 g / 1 lb | Member's Selection | $149.95 | true |
| Florida's Natural Orange Juice 2.63 L / 89 oz | Florida's Natural | $87.95 | true |
| Member's Selection Shredded Cheddar Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $91.95 | true |
| Chobani Zero Sugar Yogurt 16 Units / 150 g / 5.3 oz | Chobani | $169.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1775
- **Price increases**: 301
- **Price decreases**: 341
- **Average increase**: 5.7%
- **Average decrease**: -4.4%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Potato Sweet 2.2 kg / 5 lb | $0.00 | $38.99 | $+38.99 | +100.0% | New |
| Avocado 2 Units | $24.70 | $29.95 | $+5.25 | +21.3% | Increase |
| Fresh Chicken Breast Boneless Skinless Tray | $124.09 | $123.93 | $-0.16 | -0.1% | Decrease |
| Member's Selection Whole Almonds 907 g / 2 lb | $115.95 | $114.99 | $-0.96 | -0.8% | Decrease |
| Purple Cabbage Unit | $0.00 | $29.95 | $+29.95 | +100.0% | New |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $201.09 | $200.56 | $-0.53 | -0.3% | Decrease |
| Member's Selection Chocolate Cake Covered and Filled with Chocolate Fudge Sweet Freshly Baked 12 Slices | $0.00 | $87.95 | $+87.95 | +100.0% | New |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $94.29 | $94.44 | $+0.15 | +0.2% | Increase |
| Perdue Chicken Breast Patties 816 g / 1.8 lb | $0.00 | $89.95 | $+89.95 | +100.0% | New |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $138.29 | $138.14 | $-0.15 | -0.1% | Decrease |
| Fresh Bone-in Chicken Thighs Tray | $81.26 | $81.18 | $-0.08 | -0.1% | Decrease |
| Fresh Seasoned BBQ Chicken Quarters Bag | $89.63 | $89.54 | $-0.09 | -0.1% | Decrease |
| Whole Rack Frozen Baby Back Ribs Vacuum Packaged | $167.06 | $166.84 | $-0.22 | -0.1% | Decrease |
| Member's Selection Frozen Lamb Neck, Bone in, skinless, Tray | $65.83 | $65.72 | $-0.11 | -0.2% | Decrease |
| Fresh Cello Carrots 1.3 kg / 3 lb | $19.70 | $24.95 | $+5.25 | +26.6% | Increase |

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
| Fresh Regular Tomato | $28.99 | $38.99 | +34.5% |
| Badia Granulated Onion 566.9 g / 20 oz | $28.45 | $37.95 | +33.4% |
| Fresh Cello Carrots 1.3 kg / 3 lb | $19.70 | $24.95 | +26.6% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $79.95 | $39.70 | -50.3% |
| Frito Lay Assortment Box 24 Units | $99.95 | $49.70 | -50.3% |
| Fresh Regular Tomato | $47.85 | $28.51 | -40.4% |
| Fresh Celery  | $15.95 | $9.70 | -39.2% |
| Iceberg Lettuce Unit | $27.95 | $19.70 | -29.5% |
| LOA Bakers White Pita Bread 12 Units / 900 g | $23.95 | $16.95 | -29.2% |
| Okra 30 Units | $26.95 | $19.95 | -26.0% |
| Tyson Turkey Ham 2 Units / 340 g / 12 oz | $57.95 | $44.95 | -22.4% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Great Lakes Colby Jack Cheese Cubes 908 g / 2 lb | Great Lakes | $76.95 | 2025-08-12 |
| Member's Selection Mocha Flavor Cold Coffee Drink 9 Units / 405 mL / 13.7 oz | Member's Selection | $176.95 | 2025-08-12 |
| Spam Baked Pork Ham 3 Units / 340.2 g / 12 oz | Spam | $115.95 | 2025-08-12 |
| Smartfood White Cheddar Cheese Flavor Popcorn 156 g / 5.50 oz | Smart Foods | $23.95 | 2025-08-11 |
| Erin Farms Turkey Ham 750 g / 1.6 lb | Erin Farm | $47.95 | 2025-08-11 |
| Munchy's Krunch Oat Cookies with Dark Chocolate 3 Units / 208 g | Munchy's | $51.95 | 2025-08-11 |
| Black's Family Sweet Potato Chips 510 g / 18 oz | Black's Family | $79.95 | 2025-08-08 |
| Lush Fruit Juice Assorted Flavors 36 Units / 200 mL / 6.7 mL | Lush | $37.70 | 2025-08-07 |
| Bragg Apple Cider Vinegar 2 Units / 473 mL | Bragg | $65.95 | 2025-08-07 |
| Member's Selection Shredded Mozzarella Cheese 453 g / 1 lb | Member's Selection | $28.95 | 2025-08-07 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Potato Sweet 2.2 kg / 5 lb |  | $38.99 | G10D03 |
| Purple Cabbage Unit |  | $29.95 | G10D03 |
| Member's Selection Chocolate Cake Covered and Filled with Chocolate Fudge Sweet Freshly Baked 12 Slices | Member's Selection | $87.95 | G10D03 |
| Perdue Chicken Breast Patties 816 g / 1.8 lb | Perdue | $89.95 | G10D03 |
| Tropicland Organic Sweet Potato Fries 1.8 kg / 4 lb | Tropicland | $114.95 | G10D03 |
