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
- **Total products scraped**: 1075
- **Total value**: $116,599.55
- **Average price**: $108.46

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1073
- **Price changes detected**: 40
- **Stock/availability changes**: 10
- **Discontinued products**: 0

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
| Lipton Yellow Label Black Tea Sachets 312 Units / 2.2 g / 0.07 oz | Lipton | $104.95 | true |
| Badia All Purpose Seasoning 14 Spices 567 g / 20 oz | Badia | $69.95 | true |
| Member's Selection Shredded Mexican-Style Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $108.95 | true |
| Sensible Portions Vegetable Straws with Sea Salt 666 g / 23.5 oz | Sensible Portions | $109.95 | true |
| Pringles Mingles Cheddar and Sour Cream Puffed Snacks 2 Units / 155 g / 5.5 oz | Pringles | $69.95 | true |
| Member's Selection Shredded Mozzarella Cheese 5 Units / 453 g / 1 lb | Member's Selection | $144.95 | true |
| Member's Selection Shredded Mozzarella Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $97.95 | true |
| Member's Selection Shredded Cheddar Cheese 2 Units / 680 g / 1.5 lb | Member's Selection | $91.95 | true |
| Member's Selection Chocolate Cake Covered and Filled with Chocolate Fudge Sweet Freshly Baked 12 Slices | Member's Selection | $87.95 | true |
| Chobani Zero Sugar Yogurt 16 Units / 150 g / 5.3 oz | Chobani | $169.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 2184
- **Price increases**: 489
- **Price decreases**: 537
- **Average increase**: 5.5%
- **Average decrease**: -4.1%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Samyang Spicy Chicken-Flavored Ramen with Cheese Sauce 5 Units / 140 g | $0.00 | $47.95 | $+47.95 | +100.0% | New |
| Avocado Mesh 5 Units | $47.95 | $42.95 | $-5.00 | -10.4% | Decrease |
| Bugalu Tomato 1.5 kg / 3.5 lb | $29.95 | $27.95 | $-2.00 | -6.7% | Decrease |
| Salad Tomato 1.5 kg / 3.5 lb | $29.95 | $27.95 | $-2.00 | -6.7% | Decrease |
| Frozen Pork Belly Skin On Vacuum Packed | $476.82 | $506.64 | $+29.82 | +6.3% | Increase |
| Badia Mojo Rub Citrus Blend 680.4 g / 24 oz  | $0.00 | $82.95 | $+82.95 | +100.0% | New |
| Frozen Skinless Pork Belly Center Cut Case | $2205.97 | $2293.10 | $+87.13 | +3.9% | Increase |
| Chilled Chicken Gizzard Tray Pack | $55.72 | $55.79 | $+0.07 | +0.1% | Increase |
| Frozen Sliced Turkey Drumsticks | $98.98 | $99.05 | $+0.07 | +0.1% | Increase |
| Frozen Lamb Leg Whole Vacuum Packed | $216.69 | $216.49 | $-0.20 | -0.1% | Decrease |
| Fresh Chicken Thighs Boneless Tray | $72.74 | $72.61 | $-0.13 | -0.2% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $135.40 | $135.54 | $+0.14 | +0.1% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $93.62 | $93.47 | $-0.15 | -0.2% | Decrease |
| Maggi Vegetable Soup 12 Units / 45 g | $72.95 | $79.95 | $+7.00 | +9.6% | Increase |
| Green pepper | $33.70 | $28.29 | $-5.41 | -16.1% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| Purple Cabbage Unit | $14.70 | $29.95 | +103.7% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $39.70 | $79.95 | +101.4% |
| Frito Lay Assortment Box 24 Units | $49.70 | $99.95 | +101.1% |
| Member's Selection Mocha Flavor Cold Coffee Drink 9 Units / 405 mL / 13.7 oz | $105.70 | $176.95 | +67.4% |
| Fresh Celery  | $9.70 | $14.95 | +54.1% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $54.70 | $82.95 | +51.6% |
| Fresh Cucumber 1 kg / 2.2 lb | $12.95 | $18.95 | +46.3% |

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
| Lipton Raspberry and Lemon Flavor Tea Powder 2 Units / 670 g | Lipton | $84.95 | 2025-08-21 |
| Chef's Quality Crinkle Cut Fries 2.5kg / 5.5 lb | Chef's Quality | $49.95 | 2025-08-21 |
| The Baking Café Cross Buns 6 Units / 70 g / 0.15 lb | The Baking Café | $36.95 | 2025-08-21 |
| Aziz's Assortment Pack of Freshly Baked Traditional Sweets | Aziz's | $58.95 | 2025-08-21 |
| Fruit Nation Guava Nectar 36 Units / 200 mL | Fruit Nation | $89.70 | 2025-08-21 |
| Frozen Bone-In Pork Shoulder Case |  | $1469.48 | 2025-08-21 |
| Member's Selection English Muffin Freshly Baked Rolls 12 Units | Member's Selection | $44.95 | 2025-08-21 |
| Member's Selection Organic Extra Virgin Olive Oil 2L / 67 oz | Member's Selection | $159.95 | 2025-08-21 |
| Member's Selection Neapolitan Ice Cream / 1.89 L / 64 oz | Member's Selection | $29.70 | 2025-08-20 |
| Butterball Turkey Sausages 24 Units / 40 g / 1.41 oz | Butterball | $64.95 | 2025-08-20 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Samyang Spicy Chicken-Flavored Ramen with Cheese Sauce 5 Units / 140 g | Samyang | $47.95 | G10D03 |
| Badia Mojo Rub Citrus Blend 680.4 g / 24 oz  | Badia | $82.95 | G10D03 |
