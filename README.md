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
- **Total products scraped**: 1188
- **Total value**: $133,589.12
- **Average price**: $112.45

## Database Changes
- **New products added**: 5
- **Existing products updated**: 1183
- **Price changes detected**: 36
- **Stock/availability changes**: 8
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 178 |
|  | 150 |
| Swiss | 15 |
| Badia | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Zalea Gourmet Sliced Peaches in Light Syrup 2 Unidades / 425 g / 15 oz | Zalea Gourmet | $57.95 | true |
| Califia Farms Unsweetened Almond Drink 1.4 L / 48 oz | Califia Farms | $69.95 | true |
| Sincerely Brigitte Assorted Cheese Set 495 g / 17.5 oz | Sincerely  Brigitte | $124.95 | true |
| Rip Van Dark Chocolate Vegan Wafer Cookies 24 Units / 22 g / 0.78 oz | Rip Van | $146.95 | true |
| Member's Selection Low-Moisture Part-Skim Shredded Mozzarella Cheese 2.2 kg / 5 lb | Member's Selection | $124.95 | true |
|  MorningStar Farms Vegan Chicken-Style Nuggets 298 g / 10.5 oz | MorningStar Farms | $119.95 | true |
| Viva Zero Sugar Assorted Flavor Sparkling Water 24 Units / 355 mL | Viva | $89.95 | true |
| Sam Trade Red Lentil Protein-Based Penne Pasta 2 Units / 227 g / 8 oz | Sam Trade | $64.95 | true |
| Life Frozen Sweet Potato Fries 2.26 kg / 5 lb | Life | $69.95 | true |
| Nescafé Classic Instant Soluble Coffee 170 g + Cup | Nescafé | $63.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1148
- **Price increases**: 635
- **Price decreases**: 458
- **Average increase**: 7.4%
- **Average decrease**: -5.1%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Anjous Pears 1.36 kg / 3 lb | $64.95 | $79.95 | $+15.00 | +23.1% | Increase |
| Dutch Potatoes 22.6 kg / 50 lb | $109.95 | $132.95 | $+23.00 | +20.9% | Increase |
| Flavorite Cassatta Ice Cream 2.3 L / 77.7 oz | $0.00 | $59.95 | $+59.95 | +100.0% | New |
|  Gouda Cheese 20 kg / 44 lb | $0.00 | $1059.95 | $+1059.95 | +100.0% | New |
| Stahl Meyer Whole Smoked Frozen Turkey Thigh | $0.00 | $98.80 | $+98.80 | +100.0% | New |
| Creamery Novelties Ice Cream Punch de Créme 3.78 L / 1 gal | $72.95 | $74.95 | $+2.00 | +2.7% | Increase |
| Frozen Lamb Leg Whole Vacuum Packed | $399.61 | $398.74 | $-0.87 | -0.2% | Decrease |
| Frozen Sliced Turkey Wings, Bag | $163.79 | $163.33 | $-0.46 | -0.3% | Decrease |
| Frozen Beef Feet  | $116.03 | $115.13 | $-0.90 | -0.8% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $114.78 | $114.96 | $+0.18 | +0.2% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $66.13 | $66.20 | $+0.07 | +0.1% | Increase |
| Fresh Seasoned BBQ Chicken Quarters Bag | $94.89 | $94.66 | $-0.23 | -0.2% | Decrease |
| Fresh Ground Chicken Meat Bag | $303.59 | $304.07 | $+0.48 | +0.2% | Increase |
| Member's Selection Frozen Bone-In Lamb Stew Bag | $96.70 | $96.41 | $-0.29 | -0.3% | Decrease |
| Fresh Chicken Leg Quarters Tray | $93.81 | $93.91 | $+0.10 | +0.1% | Increase |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Fresh Beef Ribeye Steak Vacuum Packed | $246.08 | $2434.41 | +889.3% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $9.70 | $44.95 | +363.4% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $44.95 | $9.70 | -78.4% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $59.95 | $14.70 | -75.5% |
| Smithfield Smoked and Caramelized Pork Shoulder Cubes 453 g / 1 lb | $177.95 | $44.70 | -74.9% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Eggo Thick & Fluffy Waffles Original & Blueberry 2 Units / 330 g / 11.6 oz | Eggo | $109.95 | 2026-10-08 |
| Carmencita Paella Seasoning with Saffron 15 Units / 4 g / 0.14 oz | Carmencita | $24.70 | 2026-10-07 |
| Nature's Pride Yellow Split Peas 1.8 kg / 4 lb | Nature's Pride | $21.95 | 2026-10-07 |
| Heinz Tomato Ketchup 567 g / 20 oz | Heinz | $9.70 | 2026-10-07 |
| Stuffed Foods Lobster Ravioli 680 g / 24 oz | Stuffed Foods | $99.95 | 2026-10-05 |
| President Brie Cheese Spreadable 3 Units / 139 g / 4.9 oz | President | $27.70 | 2026-10-05 |
| Frozen Bone-In Pork Shoulder Vacuum Packed |  | $205.69 | 2026-10-05 |
| 6ix Naturals 100% Soybean Oil 5 L | 6ix Naturals | $82.95 | 2026-10-04 |
| Annie's Organic Macaroni and Cheese Variety Pack 12 Units / 170 g | Annies | $99.70 | 2026-10-04 |
| Member's Selection Frozen Boneless Pork Loin Roast Tray | Member's Selection | $100.71 | 2026-10-04 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Flavorite Cassatta Ice Cream 2.3 L / 77.7 oz | Flavorite | $59.95 | G10D03 |
|  Gouda Cheese 20 kg / 44 lb |  | $1059.95 | G10D03 |
| Stahl Meyer Whole Smoked Frozen Turkey Thigh | Stahl Meyer | $98.80 | G10D03 |
| Swiss Miss Hot Chocolate Mix with Marshmallows 60 Units / 28 g / 1 oz | Swiss Miss | $139.95 | G10D03 |
| Wellesley Farms Snacks Cheddar Cheese with Nuts and Cranberries 12 Units / 43 g / 1.5 oz | Wellsley Farms | $147.95 | G10D03 |
