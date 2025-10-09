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
- **Total products scraped**: 1115
- **Total value**: $122,876.19
- **Average price**: $110.20

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1114
- **Price changes detected**: 22
- **Stock/availability changes**: 11
- **Discontinued products**: 7

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 184 |
|  | 144 |
| Badia | 18 |
| Swiss | 13 |
| Nestle | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Pepperoni Pizza 2 Units / 656 g / 1.44 lb | Member's Selection | $123.95 | true |
| Member's Selection Supreme Pizza 2 Units / 716 g / 1.57 lb | Member's Selection | $123.95 | true |
| Fratelli Beretta Roll & Go Charcuterie Board 425 g / 15 oz | Fratelli Beretta | $108.95 | true |
| Swiss Miss Dark Chocolate Flavor Cocoa Powder 50 Units 31 g / 1 oz  | Swiss Miss | $99.95 | true |
| My Mochi Peppermint Ice Cream 420 g / 15 oz | My Mochi | $99.95 | true |
| Pop-Tarts Snack Crunchy Poppers Filled with Strawberry and Brownie 2 Units 360 g / 12.6 oz  | Pop Tarts | $174.95 | true |
| McCain Mac and Cheese Triangles 2 Units / 400 g / 14 oz | McCain | $119.95 | true |
| Kellogg's Chocolatey Chip Waffles 2 Pack / 349 g / 12.3 oz | Kellogg's | $97.95 | true |
| Pafritas Potatoes with Black Truffle Flavor 500 g / 1.1 lb | Pafritas | $112.95 | true |
| Tostitos Snacks White Corn Chips Nachos / 283 g / 10 oz | Tostitos | $50.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1356
- **Price increases**: 765
- **Price decreases**: 511
- **Average increase**: 4.9%
- **Average decrease**: -3.7%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Carrot 2.27 kg / 5 lb | $36.95 | $37.95 | $+1.00 | +2.7% | Increase |
| Chilled Boneless Beef Eye of Round, Case | $3378.80 | $3750.81 | $+372.01 | +11.0% | Increase |
| Flavorite Cream Punch and Sorrel Ice Cream 2 Units / 1 L / 33.8 oz | $0.00 | $69.95 | $+69.95 | +100.0% | New |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $172.78 | $173.08 | $+0.30 | +0.2% | Increase |
| Frozen Lamb Leg Whole Vacuum Packed | $318.42 | $321.30 | $+2.88 | +0.9% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $95.64 | $95.49 | $-0.15 | -0.2% | Decrease |
| Fresh Chicken Leg Quarters Tray | $91.31 | $91.11 | $-0.20 | -0.2% | Decrease |
| Fresh Ground Chicken Tray | $84.06 | $84.18 | $+0.12 | +0.1% | Increase |
| Swift Frozen Chilled Pork Ribs Kansas City Style BBQ Vacuum Pack  | $140.17 | $140.00 | $-0.17 | -0.1% | Decrease |
| Fresh Chicken Breast Bone In Tray | $93.12 | $93.02 | $-0.10 | -0.1% | Decrease |
| Fresh Whole Chicken 2 Units | $102.82 | $102.75 | $-0.07 | -0.1% | Decrease |
| Frozen Bone-In Pork Spare Rib Vacuum Packaged | $147.60 | $147.36 | $-0.24 | -0.2% | Decrease |
| Gouda Cheese Block | $72.03 | $72.16 | $+0.13 | +0.2% | Increase |
| Frozen Boneless Skinless Chicken Breast Tray | $152.95 | $152.76 | $-0.19 | -0.1% | Decrease |
| Fresh Boneless Beef Eye of Round Whole Piece Vacuum Packaged | $405.81 | $404.30 | $-1.51 | -0.4% | Decrease |

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
| Galvanina Italian Sparkling Mineral Water 24 Units / 500 mL / 16.9 oz | Galvanina | $144.95 | 2025-10-08 |
| Rice Krispies Treats Assorted Mini Snacks 52 Units / 11 g / 0.39 oz | Rice Krispies Treats | $134.95 | 2025-10-08 |
|  Eggplant 793 g / 1.75 lb |  | $19.70 | 2025-10-08 |
| Pier 33 Gourmet Frozen Boneless Skin-On Salmon 680 g / 1.5 lb | Pier 33 | $164.95 | 2025-10-08 |
| Truffettes de France Mallows of French Origin 510 g / 18 oz | Truffettes | $39.70 | 2025-10-08 |
| Hunt's Tomato Paste 12 Units / 170 g / 6 oz | Hunt's | $39.70 | 2025-10-08 |
| Member's Selection Chocolate Chip, Colored Chocolate Chunk and Oatmeal Cookies, Freshly Baked 24 Units | Member's Selection | $32.95 | 2025-10-08 |
| Red Potato 4.5 kg / 10 lb |  | $69.95 | 2025-10-07 |
| Angie's Boom Chicka Pop Sweet and Salty Popcorn 652 g / 23 oz | Angie´s | $49.70 | 2025-10-06 |
| Ginger 454 g / 1 lb |  | $34.95 | 2025-10-06 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Flavorite Cream Punch and Sorrel Ice Cream 2 Units / 1 L / 33.8 oz | Flavorite | $69.95 | G10D03 |
