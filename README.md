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
- **Total products scraped**: 1090
- **Total value**: $119,301.02
- **Average price**: $109.45

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1089
- **Price changes detected**: 25
- **Stock/availability changes**: 12
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 184 |
|  | 135 |
| Badia | 19 |
| Swiss | 13 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Tostitos Snacks White Corn Chips Nachos / 283 g / 10 oz | Tostitos | $50.95 | true |
| Nilo Coconut Water 12 Units / 320 mL / 10.82 oz | Nilo | $124.95 | true |
| Tropicland Organic Sweet Potato Fries 1.8 kg / 4 lb | Tropicland | $114.95 | true |
| Pafritas Paprika Flavor Potato Chips 500 g / 1.1 lb | Pafritas | $86.95 | true |
| Nilo Soursop Juice 12 Units / 320 mL / 10.82 oz | Nilo | $139.95 | true |
| Member's Selection Sliced Assorted Cheese Pack 907 g / 32 oz | Member's Selection | $87.95 | true |
| Crix Steelpan Original Cookies in Collectible Tin 768 g | Crix | $59.95 | true |
| Badia All Purpose Marinade Seasoning 591 mL / 20 oz  | Badia | $21.95 | true |
| Cheez-It White and Jack Cheddar Crackers 2 Pack 351 g / 12.4 oz | CheezIt | $89.95 | true |
| Jell-O Assorted Desserts 24 Units 2.41 kg / 5 lb | Jell-O | $159.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1257
- **Price increases**: 575
- **Price decreases**: 596
- **Average increase**: 6.4%
- **Average decrease**: -4.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Barista Coffee Salty Caramel-Flavored Cappuccino Mix 2 Units / 320 g / 11.2 oz | $70.95 | $79.82 | $+8.87 | +12.5% | Increase |
| Avocado 2 Units | $9.70 | $29.95 | $+20.25 | +208.8% | Increase |
| Freshway Red Dragon Fruit 794 g / 1.75 lb | $0.00 | $79.95 | $+79.95 | +100.0% | New |
| Frozen Sliced Turkey Drumsticks | $98.98 | $99.05 | $+0.07 | +0.1% | Increase |
| Chilled Chicken Gizzard Tray Pack | $55.72 | $55.79 | $+0.07 | +0.1% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $80.49 | $80.40 | $-0.09 | -0.1% | Decrease |
| Fresh Ground Chicken Meat Bag | $263.80 | $264.11 | $+0.31 | +0.1% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $134.96 | $135.10 | $+0.14 | +0.1% | Increase |
| Fresh Seasoned BBQ Chicken Quarters Bag | $89.72 | $89.81 | $+0.09 | +0.1% | Increase |
| Member's Selection Frozen Bone-In Pork Shoulder Picnic Stew, Tray | $58.94 | $59.04 | $+0.10 | +0.2% | Increase |
| Fresh Chicken Drumsticks Tray  | $89.13 | $89.24 | $+0.11 | +0.1% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Case | $1312.59 | $1366.86 | $+54.27 | +4.1% | Increase |
| Fresh Chicken Breast Bone In Tray | $91.87 | $91.97 | $+0.10 | +0.1% | Increase |
| Fresh Ground Chicken Tray | $87.01 | $86.89 | $-0.12 | -0.1% | Decrease |
| Frozen Whole Boneless Pork Tenderloin Vacuum Packaged | $71.99 | $71.74 | $-0.25 | -0.3% | Decrease |

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
| Capri Sun Variety 100% Juice 40 Units / 177 mL / 6 oz | Capri Sun | $104.95 | 2025-08-30 |
| Nanak Rasmalai 1 kg / 2.2 lb | Nanak | $79.70 | 2025-08-28 |
| Red Apples 2.26 kg / 5 lb |  | $59.95 | 2025-08-28 |
| Jennies Coconut Bites with Cacao Nibs and Dark Chocolate 680 g / 24 oz | Jennies | $129.95 | 2025-08-26 |
| Member's Selection Chocolate Cake Covered and Filled with Chocolate Fudge Sweet Freshly Baked 12 Slices | Member's Selection | $87.95 | 2025-08-26 |
| Suzy's Cream Cheesecake Assorted Flavors Cheesecake Squares 16 Units | Suzy's Cream Cheesecakes | $140.95 | 2025-08-24 |
| Lipton Raspberry and Lemon Flavor Tea Powder 2 Units / 670 g | Lipton | $84.95 | 2025-08-21 |
| Chef's Quality Crinkle Cut Fries 2.5kg / 5.5 lb | Chef's Quality | $49.95 | 2025-08-21 |
| The Baking Café Cross Buns 6 Units / 70 g / 0.15 lb | The Baking Café | $36.95 | 2025-08-21 |
| Aziz's Assortment Pack of Freshly Baked Traditional Sweets | Aziz's | $58.95 | 2025-08-21 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Freshway Red Dragon Fruit 794 g / 1.75 lb | Freshway | $79.95 | G10D03 |
