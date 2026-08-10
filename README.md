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
- **Total products scraped**: 1113
- **Total value**: $123,974.06
- **Average price**: $111.39

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1113
- **Price changes detected**: 69
- **Stock/availability changes**: 13
- **Discontinued products**: 5

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 176 |
|  | 132 |
| Badia | 16 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| McCain Cassava Sticks 997 g / 2.2 lb | McCain | $43.95 | true |
| Ocean Spray Cranberry Juice 2 Units 1.89 L / 64 oz | Ocean Spray | $77.95 | true |
| Cultured Cravings Coconut Yogurt 12 Units / 150 g / 5.3 oz | Cultured Cravings | $229.95 | true |
| Coke Sugar-Free Canned Soda 6 Units / 355 mL / 12 oz | Coca-Cola | $24.95 | true |
| Nature's Pride Lentils 2.3 kg / 5 lb | Nature's Pride | $44.95 | true |
| Sprite Lemon-Lime Flavor Soda 24 Units / 355 mL | Sprite | $99.95 | true |
| Member's Selection Freshly Made Assorted Doughnuts 12 Units | Member's Selection | $55.95 | true |
| Member's Selection Freshly Baked Chocolate Chip Cookies 24 Units | Member's Selection | $60.95 | true |
| Member's Selection Freshly Baked Black Forest Cake 10 to 12 Slices | Member's Selection | $139.95 | true |
| Member's Selection Fresh Baked Cheesecake 15 to 20 Slices | Member's Selection | $206.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1075
- **Price increases**: 544
- **Price decreases**: 505
- **Average increase**: 5.9%
- **Average decrease**: -5.3%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Fresh Bone-in Chicken Thighs Tray | $69.87 | $69.94 | $+0.07 | +0.1% | Increase |
| Fresh Chicken Mixed Parts Tray | $83.92 | $83.82 | $-0.10 | -0.1% | Decrease |
| Fresh Whole Chicken 2 Units | $104.68 | $104.50 | $-0.18 | -0.2% | Decrease |
| Member's Selection Frozen Sliced Turkey Wings, Bag | $166.42 | $161.15 | $-5.27 | -3.2% | Decrease |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $245.87 | $246.73 | $+0.86 | +0.3% | Increase |
| Swiss Crunchy Peanut Butter 1.3 kg | $42.95 | $34.95 | $-8.00 | -18.6% | Decrease |
| Papaya | $39.11 | $38.92 | $-0.19 | -0.5% | Decrease |
| Fresh Chicken Thighs Boneless Bag | $339.32 | $338.96 | $-0.36 | -0.1% | Decrease |
| Fresh Chicken Thighs Boneless Tray | $90.41 | $90.28 | $-0.13 | -0.1% | Decrease |
| Frozen Lamb Shoulder Chops Tray | $124.13 | $124.31 | $+0.18 | +0.1% | Increase |
| McVitie's Go Ahead Assortment of Crunchy Cookies with Fruity Filling 3 Units / 174 g / 6 oz | $47.95 | $39.85 | $-8.10 | -16.9% | Decrease |
| Ribeye Choice Fillet Fresh Tray | $324.90 | $324.13 | $-0.77 | -0.2% | Decrease |
| Soldanza Mix Holiday Snacks 12 Units | $52.95 | $44.95 | $-8.00 | -15.1% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $118.19 | $118.01 | $-0.18 | -0.2% | Decrease |
| Mr Topper's Premium Popcorn Kernels 1.8 kg / 4 lb | $36.95 | $28.95 | $-8.00 | -21.7% | Decrease |

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
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Red Rose Canned Pink Salmon in Water 2 Units / 418 g / 14.7 oz | Red Rose | $72.95 | 2026-08-09 |
| Mowi Lightly Smoked Salmon 680 g / 1.5 lb | Mowi | $214.95 | 2026-08-09 |
| Charles Chocolate Coated Jordanian Almond 1 kg / 2.2 lb | Charles Chocolates | $29.70 | 2026-08-09 |
| Idahoan Classic Instant Mashed Potatoes 1.47 kg / 3.25 lb | Idahoan | $49.70 | 2026-08-09 |
| The Baking Café Cross Buns 6 Units / 70 g / 0.15 lb | The Baking Café | $36.95 | 2026-08-09 |
| Florida's Natural Strawberry Lemonade 2 Units 1.75 L / 59 oz | Florida's Natural | $114.95 | 2026-08-08 |
| Member's Selection Mayonnaise 12 Units / 591 mL / 20 oz | Member's Selection | $199.95 | 2026-08-08 |
| Mowi Tuscan Frozen Herb Salmon Portions 710 g / 1.56 lb | Mowi | $194.95 | 2026-08-06 |
| Garden Foods Mixed Vegetables 1.36 kg / 3 lb | Garden Foods | $54.95 | 2026-08-05 |
| Tostitos Spinach and Cheese Cream Dips 2 Units / 425.2 g | Frito Lay | $59.95 | 2026-08-05 |

## New Products Added Today
No new products added today.
