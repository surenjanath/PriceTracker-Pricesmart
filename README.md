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
- **Total products scraped**: 1147
- **Total value**: $127,836.52
- **Average price**: $111.45

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1147
- **Price changes detected**: 0
- **Stock/availability changes**: 24
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 182 |
|  | 136 |
| Badia | 19 |
| Swiss | 15 |
| Nestle | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Refined Avocado Oil 1 L / 33.8 oz | Member's Selection | $169.95 | true |
| Mrs Thinster Toasted Coconut Cookies 454 g | Mrs. Thinster's | $89.95 | true |
| Cheez-It Original, Grahams, and White Cheddar Cheez-It Gripz Variety Pack 12 Units / 25 g / 0.9 oz | CheezIt | $66.95 | true |
| Carrington Farms Coconut Oil Spray 2 Units / 141.7 g / 5 oz | Carrington Farms | $69.95 | true |
| Morning Star Farms Sausage Links Plant-Based 2 Units 225 g / 8 oz  | MorningStar Farms | $124.95 | true |
| Philadelphia Salmon Cream Cheese 2 Units / 212 g / 7.5 oz | Philadelphia | $82.95 | true |
| Sincerely Brigitte Cheese Sticks 24 Units / 510 g / 18 oz | Sincerely  Brigitte | $99.95 | true |
| Sunny Fruits Dried Organics Figs 10 Units / 50 g / 1.76 oz | Sunny Fruits | $79.95 | true |
| Aqua Star Breaded Shrimp 1.36 kg / 3 lb | Aqua Star | $192.95 | true |
| Prairie Farms Half and Half 946 mL / 32 oz | Prairie Farms | $37.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 993
- **Price increases**: 437
- **Price decreases**: 522
- **Average increase**: 10.7%
- **Average decrease**: -5.4%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Fresh Chicken Thighs Boneless Tray | $82.49 | $82.36 | $-0.13 | -0.2% | Decrease |
| Half Moon Assorted Vegan Ice Cream Popsicles 8 Units / 75 mL / 2.53 oz | $0.00 | $99.95 | $+99.95 | +100.0% | New |
| Member's Selection Frozen Bone-In Beef Feet Sliced, Tray | $225.89 | $228.70 | $+2.81 | +1.2% | Increase |
| Frozen Lamb Leg Whole Boneless Tray Pack | $359.44 | $358.33 | $-1.11 | -0.3% | Decrease |
| Frozen Pork Belly Skin On Sliced Tray  | $118.75 | $118.03 | $-0.72 | -0.6% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $189.53 | $189.81 | $+0.28 | +0.1% | Increase |
| Pork Belly with Skin Frozen Vacuum Packaged | $180.71 | $180.49 | $-0.22 | -0.1% | Decrease |
| Maggi Vegetable Soup 12 Units / 45 g | $79.95 | $65.95 | $-14.00 | -17.5% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $114.34 | $114.51 | $+0.17 | +0.1% | Increase |
| Frozen Bone In Pork Shoulder Sliced Tray | $78.77 | $78.87 | $+0.10 | +0.1% | Increase |
| Papaya | $32.06 | $32.03 | $-0.03 | -0.1% | Decrease |
| Fresh Chicken Breast Bone In Tray | $94.08 | $93.98 | $-0.10 | -0.1% | Decrease |
| Frozen Lamb Shoulder Chops Tray | $120.14 | $120.32 | $+0.18 | +0.1% | Increase |
| Pimento Peppers 40 Units | $20.95 | $19.95 | $-1.00 | -4.8% | Decrease |
| Orchard Assorted Drinks Juice Mix 6 Units / 1L | $69.95 | $56.95 | $-13.00 | -18.6% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Fresh Beef Ribeye Steak Vacuum Packed | $246.08 | $2434.41 | +889.3% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $14.70 | $57.95 | +294.2% |
| Carrot 2.27 kg / 5 lb | $9.70 | $37.95 | +291.2% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Popsalot Gourmet Caramel Popcorn with Almonds 283 g / 10 oz | Popsalot Gourmet | $84.95 | 2026-04-01 |
| Jayone Yizu Citrus Flavored Sweet Crispy Rice Rolls 2 Units / 80 g | Jayone | $39.95 | 2026-04-01 |
| Seedless Red Grapes |  | $97.01 | 2026-04-01 |
| Bombolo Biscotti Mini Tartlets Filled with Sweet Wild Berry and Vanilla Flavor | Bombolo Biscotti | $64.95 | 2026-04-01 |
| Fresh Red Globe Grapes |  | $81.07 | 2026-04-01 |
| Frozen Pork Belly Skin On Case |  | $1169.42 | 2026-04-01 |
| Fresh Beef Striploin Steak Tray |  | $170.27 | 2026-04-01 |
| Delimex Cocina Beef Taquitos 566 g / 1.25 lb | Delimex Cocina | $62.95 | 2026-03-31 |
| Member's Selection Frozen Skinless Boneless Salmon Fillets Vacuum Packaged | Member's Selection | $304.50 | 2026-03-31 |
| Suzy's Cream Assorted Flavors Cheesecake New York, Strawberry, Chocolate, and Caramel 12 Slices | Suzy's Cream Cheesecakes | $144.95 | 2026-03-29 |

## New Products Added Today
No new products added today.
