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
- **Total products scraped**: 1121
- **Total value**: $123,008.40
- **Average price**: $109.73

## Database Changes
- **New products added**: 4
- **Existing products updated**: 1117
- **Price changes detected**: 26
- **Stock/availability changes**: 18
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 185 |
|  | 145 |
| Badia | 18 |
| Swiss | 13 |
| Nestle | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Pepperoni Pizza 2 Units / 656 g / 1.44 lb | Member's Selection | $123.95 | true |
| Member's Selection Supreme Pizza 2 Units / 716 g / 1.57 lb | Member's Selection | $123.95 | true |
| Member's Selection Mayonnaise 12 Units / 591 mL / 20 oz | Member's Selection | $349.95 | true |
| Kellogg's Assorted Flavors Crackers 13 Packages / 1.47 kg / 52 oz | Kellogg's | $169.95 | true |
| Fratelli Beretta Roll & Go Charcuterie Board 425 g / 15 oz | Fratelli Beretta | $108.95 | true |
| Trias Assorted Flavor Special Cookies 2 Units / 300 g / 10.59 oz | Trias | $133.95 | true |
| Swiss Miss Dark Chocolate Flavor Cocoa Powder 50 Units 31 g / 1 oz  | Swiss Miss | $99.95 | true |
| My Mochi Peppermint Ice Cream 420 g / 15 oz | My Mochi | $99.95 | true |
| Pop-Tarts Snack Crunchy Poppers Filled with Strawberry and Brownie 2 Units 360 g / 12.6 oz  | Pop Tarts | $174.95 | true |
| Kellogg's Chocolatey Chip Waffles 2 Pack / 349 g / 12.3 oz | Kellogg's | $97.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1365
- **Price increases**: 768
- **Price decreases**: 517
- **Average increase**: 4.9%
- **Average decrease**: -3.7%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Classic Cream Chocolate Whipped Cream 2 Units / 368 g / 13 oz | $0.00 | $84.95 | $+84.95 | +100.0% | New |
| La Yogurt Latin Flavor Mango 907 g / 32 oz | $0.00 | $32.95 | $+32.95 | +100.0% | New |
| Wellsley Farms Apple Cider 3.8 L / 128 oz | $0.00 | $84.95 | $+84.95 | +100.0% | New |
| Frozen Lamb Leg Whole Boneless Tray Pack | $303.52 | $306.09 | $+2.57 | +0.8% | Increase |
| Dietz & Watson Chef Carved Ham 1.36 kg / 3 lb | $0.00 | $165.95 | $+165.95 | +100.0% | New |
| Frozen Imported Pork Leg Slices | $74.67 | $75.96 | $+1.29 | +1.7% | Increase |
| Frozen Lamb Leg Whole Vacuum Packed | $317.55 | $318.42 | $+0.87 | +0.3% | Increase |
| Frozen Sliced Turkey Drumsticks | $151.33 | $150.66 | $-0.67 | -0.4% | Decrease |
| Fresh Seasoned BBQ Chicken Quarters Bag | $90.71 | $90.89 | $+0.18 | +0.2% | Increase |
| Maggi Vegetable Soup 12 Units / 45 g | $73.95 | $79.95 | $+6.00 | +8.1% | Increase |
| Fresh Ground Chicken Tray | $84.18 | $84.06 | $-0.12 | -0.1% | Decrease |
| Fresh Whole Chicken for Frying Bag | $260.86 | $260.71 | $-0.15 | -0.1% | Decrease |
| Swift Frozen Chilled Pork Ribs Kansas City Style BBQ Vacuum Pack  | $140.00 | $140.17 | $+0.17 | +0.1% | Increase |
| Fresh Whole Chicken 2 Units | $102.89 | $102.82 | $-0.07 | -0.1% | Decrease |
| Whole Rack Frozen Baby Back Ribs Vacuum Packaged | $155.66 | $155.87 | $+0.21 | +0.1% | Increase |

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
| Red Potato 4.5 kg / 10 lb |  | $69.95 | 2025-10-07 |
| Angie's Boom Chicka Pop Sweet and Salty Popcorn 652 g / 23 oz | Angie´s | $49.70 | 2025-10-06 |
| Ginger 454 g / 1 lb |  | $34.95 | 2025-10-06 |
| Avocado 2 Units |  | $29.95 | 2025-10-06 |
| Pringles Potato Chips Mix 3 Units / 158 g / 5.5 oz | Pringles | $69.95 | 2025-10-04 |
| Town House Assorted Flavor Crackers 3 Units | Town House | $119.95 | 2025-10-04 |
| Mowi Tuscan Frozen Herb Salmon Portions 710 g / 1.56 lb | Mowi | $185.95 | 2025-10-03 |
| MacKnight Roasted Salmon Flakes 454 g / 1 lb | MacKnight | $49.70 | 2025-10-03 |
| Assorted Peppers |  | $33.62 | 2025-10-03 |
| Bermudez Vanilla Cookies 6 Units / 142 g / 5 oz | Bermudez | $53.95 | 2025-10-02 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Classic Cream Chocolate Whipped Cream 2 Units / 368 g / 13 oz | Classic Cream | $84.95 | G10D03 |
| La Yogurt Latin Flavor Mango 907 g / 32 oz | La Yogurt | $32.95 | G10D03 |
| Wellsley Farms Apple Cider 3.8 L / 128 oz | Wellsley Farms | $84.95 | G10D03 |
| Dietz & Watson Chef Carved Ham 1.36 kg / 3 lb | Dietz and Watson | $165.95 | G10D03 |
