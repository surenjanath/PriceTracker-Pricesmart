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
- **Total products scraped**: 1142
- **Total value**: $128,161.35
- **Average price**: $112.23

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1141
- **Price changes detected**: 22
- **Stock/availability changes**: 10
- **Discontinued products**: 4

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 181 |
|  | 135 |
| Badia | 19 |
| Swiss | 15 |
| Brunswick | 10 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Freshly Baked Vanilla Loaf Cake | Member's Selection | $37.95 | true |
| Member's Selection Straight Cut French Fries 2.5 kg / 88 oz | Member's Selection | $44.95 | true |
| Member's Selection Cookies and Cream Cake Decorated with Oreo Cookie 12 Slices | Member's Selection | $139.95 | true |
| Member's Selection Freshly Baked Berries Cake 12 Slices | Member's Selection | $139.95 | true |
| Eggo Thick & Fluffy Waffles Original & Blueberry 2 Units / 330 g / 11.6 oz | Eggo | $106.95 | true |
| Pizzacini Truffle and Mushroom Pizza 2 Units / 440 g / 15.5 oz | Pizzacini | $169.95 | true |
| Spirella Prosciutto with Mozzarella 454 g / 16 oz |  | $114.95 | true |
| Crispy Just Baked Mini Naan Bread Bites Baked and Crunchy Snack Style | Crispy Just Baked | $39.95 | true |
| Calbee Snacks Lightly Salted Baked Pea Crisps 567 g / 1.25 lb | Calbee | $116.95 | true |
| Heinz Tomato Ketchup 567 g / 20 oz | Heinz | $29.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1083
- **Price increases**: 539
- **Price decreases**: 512
- **Average increase**: 7.5%
- **Average decrease**: -6.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Karnis Assorted Flavored Dressings 3 Units / 226 g / 8 oz | $0.00 | $94.95 | $+94.95 | +100.0% | New |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $201.21 | $201.51 | $+0.30 | +0.1% | Increase |
| Frozen Bone-In Goat Carcass Case | $1144.43 | $1173.39 | $+28.96 | +2.5% | Increase |
| Papaya | $32.19 | $32.16 | $-0.03 | -0.1% | Decrease |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $229.29 | $229.86 | $+0.57 | +0.2% | Increase |
| Pork Belly with Skin Frozen Vacuum Packaged | $178.33 | $177.69 | $-0.64 | -0.4% | Decrease |
| Fresh Bone-in Chicken Thighs Tray | $66.54 | $66.81 | $+0.27 | +0.4% | Increase |
| Brunswick Canned Chicken Vienna Sausage 12 pieces / 141 g / 4.9 oz | $66.95 | $71.95 | $+5.00 | +7.5% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $163.43 | $164.06 | $+0.63 | +0.4% | Increase |
| Ribeye Choice Fillet Fresh Tray | $299.56 | $300.96 | $+1.40 | +0.5% | Increase |
| Fresh Chicken Leg Quarters Tray | $92.51 | $93.51 | $+1.00 | +1.1% | Increase |
| Nutrina Chilled Whole Chicken Bag | $342.02 | $350.49 | $+8.47 | +2.5% | Increase |
| Frozen Lamb Shoulder Chops Tray | $121.20 | $121.02 | $-0.18 | -0.1% | Decrease |
| Member's Selection Frozen Sliced Turkey Wings, Bag | $207.41 | $209.15 | $+1.74 | +0.8% | Increase |
| Fresh Ground Chicken Meat Bag | $297.23 | $299.58 | $+2.35 | +0.8% | Increase |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Fresh Beef Ribeye Steak Vacuum Packed | $246.08 | $2434.41 | +889.3% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $9.70 | $44.95 | +363.4% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $14.70 | $57.95 | +294.2% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $44.95 | $9.70 | -78.4% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Apple Jacks Cereal de Manzana y Canela 1.03 kg / 36.5 oz | Apple Jacks | $98.95 | 2026-04-21 |
| Swiss Miss Dark Chocolate Flavor Cocoa Powder 50 Units 31 g / 1 oz  | Swiss Miss | $94.95 | 2026-04-21 |
| Krusteaz Butter and Honey Pancake Mix 8 Units / 907 g / 2 lb | Krusteaz | $149.70 | 2026-04-21 |
| Erin Farm Back Bacon 500 g / 1.1 lb | Erin Farm | $47.95 | 2026-04-21 |
| Butterball Whole Turkey 4.5 kg - 5.4 kg / 10 lb - 12 lb | Butterball | $339.95 | 2026-04-19 |
| Lindt Assorted Chocolates 600 g / 21.16 oz | Lindt | $164.95 | 2026-04-19 |
| Montchevre Goat Cheese 298 g / 10.5 oz | Montchevre | $59.95 | 2026-04-19 |
| Edwards Signatures Pecan Pie 907g / 2 lb | Edward's | $69.95 | 2026-04-19 |
| Member's Selection Chilled Ground Beef Tray | Member's Selection | $104.93 | 2026-04-19 |
| Par Excellence Long Grain White Jasmine Rice 4 kg | Par Excellence | $69.95 | 2026-04-15 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Karnis Assorted Flavored Dressings 3 Units / 226 g / 8 oz | Karnis | $94.95 | G10D03 |
