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
- **Total products scraped**: 1105
- **Total value**: $117,983.55
- **Average price**: $106.77

## Database Changes
- **New products added**: 3
- **Existing products updated**: 1102
- **Price changes detected**: 19
- **Stock/availability changes**: 20
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 185 |
|  | 143 |
| Badia | 19 |
| Swiss | 13 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Pepperoni Pizza 2 Units / 656 g / 1.44 lb | Member's Selection | $123.95 | true |
| Member's Selection Supreme Pizza 2 Units / 716 g / 1.57 lb | Member's Selection | $123.95 | true |
| Fratelli Beretta Roll & Go Charcuterie Board 425 g / 15 oz | Fratelli Beretta | $108.95 | true |
| Kellogg's Assorted Flavors Crackers 13 Packages / 1.47 kg / 52 oz | Kellogg's | $169.95 | true |
| Trias Assorted Flavor Special Cookies 2 Units / 300 g / 10.59 oz | Trias | $133.95 | true |
| Swiss Miss Dark Chocolate Flavor Cocoa Powder 50 Units 31 g / 1 oz  | Swiss Miss | $99.95 | true |
| My Mochi Peppermint Ice Cream 420 g / 15 oz | My Mochi | $99.95 | true |
| Kellogg's Chocolatey Chip Waffles 2 Pack / 349 g / 12.3 oz | Kellogg's | $97.95 | true |
| Member's Selection Mayonnaise 12 Units / 591 mL / 20 oz | Member's Selection | $349.95 | true |
| Heinz Tomato Ketchup 12 Units 591.5 mL / 20 oz | Heinz | $394.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1344
- **Price increases**: 760
- **Price decreases**: 525
- **Average increase**: 4.5%
- **Average decrease**: -3.3%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Glazed Fruits 908 g / 2 lb | $0.00 | $47.95 | $+47.95 | +100.0% | New |
| Fresh Chicken Thighs Boneless Tray | $73.26 | $73.39 | $+0.13 | +0.2% | Increase |
| Member's Selection Grade A Fancy Blueberries 1.36 kg / 3 lb | $0.00 | $83.95 | $+83.95 | +100.0% | New |
| Great Foods Frozen Smoked Chicken Ham 1.36 kg / 3 lb | $0.00 | $89.95 | $+89.95 | +100.0% | New |
| Chilled Chicken Gizzard Tray Pack | $55.65 | $55.57 | $-0.08 | -0.1% | Decrease |
|  Eggplant 793 g / 1.75 lb | $59.95 | $39.70 | $-20.25 | -33.8% | Decrease |
| Frozen Bone In Pork Shoulder Sliced Tray | $69.73 | $69.53 | $-0.20 | -0.3% | Decrease |
| Frozen Sliced Turkey Drumsticks | $151.33 | $148.17 | $-3.16 | -2.1% | Decrease |
| Gouda Cheese Block | $71.89 | $71.76 | $-0.13 | -0.2% | Decrease |
| Iceberg Lettuce Unit | $24.95 | $22.95 | $-2.00 | -8.0% | Decrease |
| Fresh Whole Chicken for Frying Bag | $261.46 | $261.16 | $-0.30 | -0.1% | Decrease |
| Fresh Chicken Breast Bone In Tray | $92.54 | $92.45 | $-0.09 | -0.1% | Decrease |
| Pork Chop with Bone Frozen Tray | $81.46 | $81.58 | $+0.12 | +0.1% | Increase |
| Fresh Celery  | $16.95 | $17.95 | $+1.00 | +5.9% | Increase |
| Fresh Chicken Mixed Parts Tray | $87.37 | $87.48 | $+0.11 | +0.1% | Increase |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $29.70 | $89.95 | +202.9% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $34.70 | $89.95 | +159.2% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| United With Earth Date and Almond Rolls 340 g / 12 oz | $26.70 | $54.95 | +105.8% |
| Purple Cabbage Unit | $14.70 | $29.95 | +103.7% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $34.70 | -61.4% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| United With Earth Date and Almond Rolls 340 g / 12 oz | $54.95 | $26.70 | -51.4% |
| Purple Cabbage Unit | $29.95 | $14.70 | -50.9% |
|  Eggplant 793 g / 1.75 lb | $59.95 | $29.70 | -50.5% |
| Reny Picot Brie with Peppercorns 396 g /14 oz | $69.95 | $34.70 | -50.4% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| RW Garcia Sweet Potato Gluten-Free Crackers 2 Units / 425 g / 15 oz | RW Garcia | $106.95 | 2025-09-29 |
| Best Fruit Tamarind Chili Snacks 453 g / 15.97 oz | Best Fruit | $64.95 | 2025-09-29 |
| Lush Mango Flavor Fruit Drink 3 Units / 1 L / 33.8 oz | Lush | $38.95 | 2025-09-29 |
| Celorrio Spanish Tomato Sauce 6 Units / 400 g / 14 oz | Celorrio | $29.70 | 2025-09-29 |
| Better Living Flavored Instant Oats Assortment 50 Units / 45 g | Better Living | $99.95 | 2025-09-29 |
| Kiss White Bread 665 g | Kiss | $16.45 | 2025-09-29 |
| Goya Coconut Milk 3 Units / 400 mL / 13.5 oz | Goya | $65.95 | 2025-09-29 |
| Jayone Honey Rice Rolls 2 Units / 80 g | Jayone | $39.95 | 2025-09-29 |
| Carolina Ground Turkey Meat, 2.3 kg / 5 lb | Carolina Turkey | $111.07 | 2025-09-28 |
| Snapple Fruit Flavored Juice 24 Units / 591 mL / 20 oz | Snapple | $269.95 | 2025-09-26 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Glazed Fruits 908 g / 2 lb |  | $47.95 | G10D03 |
| Member's Selection Grade A Fancy Blueberries 1.36 kg / 3 lb | Member's Selection | $83.95 | G10D03 |
| Great Foods Frozen Smoked Chicken Ham 1.36 kg / 3 lb | Great Foods | $89.95 | G10D03 |
