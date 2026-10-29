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
- **Total products scraped**: 1174
- **Total value**: $138,330.41
- **Average price**: $117.83

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1173
- **Price changes detected**: 50
- **Stock/availability changes**: 15
- **Discontinued products**: 4

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 178 |
|  | 149 |
| Swiss | 16 |
| Badia | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Krusteaz Cinnamon Swirl Crumb Cake & Muffin Mix with Toppings 3 Units / 411 g / 14.5 oz | Krusteaz | $94.95 | true |
| Carmencita Mediterranean Spice Mix with Grinder 190 g / 6.7 oz | Carmencita | $48.95 | true |
| Carmencita Himalayan Pink Salt with Grinder 370 g / 13 oz | Carmencita | $41.45 | true |
| Chief Ground Split Peas for Soups and Dhal 1.2 kg | Chief | $36.95 | true |
| Member's Selection Extra Virgin Olive Oil 750 mL / 25.36 oz | Member's Selection | $69.95 | true |
| aribbean Flavours Creamy Egg-Free Mayonnaise 3 Units / 330 mL | Karibbean Flavours | $52.95 | true |
| Carretilla Quinoa Salad with Chili Dressing Ready to Eat 4 Units 230 g / 8.8 oz | Carretilla | $129.95 | true |
| Delve Dip Variety Pack 3 Units / 170 g / 6 oz | Delve | $109.95 | true |
| Rip Van Dark Chocolate Vegan Wafer Cookies 24 Units / 22 g / 0.78 oz | Rip Van | $146.95 | true |
| Poppycock Gourmet Caramel Popcorn with Cashews 850 g / 30 oz | Poppycock | $169.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1150
- **Price increases**: 619
- **Price decreases**: 481
- **Average increase**: 10.4%
- **Average decrease**: -6.1%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Re-Lyte Hydration Electrolyte Powder Variety Flavors 30 Units / 6.3 g / 0.22 oz | $0.00 | $306.95 | $+306.95 | +100.0% | New |
| Phillip Seafood Crab Claw Meat 454 g / 16 oz  | $134.95 | $137.95 | $+3.00 | +2.2% | Increase |
| Breakstone's Cottage Cheese 680 g / 1.5 lb | $48.95 | $49.95 | $+1.00 | +2.0% | Increase |
| Member's Selection Pumpkin and Spice Swiss Roll Freshly Baked | $35.95 | $37.95 | $+2.00 | +5.6% | Increase |
| Dare Viva Puffs Candy Cane 2 Units / 300 g | $49.95 | $52.95 | $+3.00 | +6.0% | Increase |
| Smoked Pork Chop with Bone Frozen Tray | $80.07 | $81.28 | $+1.21 | +1.5% | Increase |
| Papaya | $37.74 | $37.71 | $-0.03 | -0.1% | Decrease |
| Fresh Beef Ribeye Steak Vacuum Packed | $3076.13 | $3184.23 | $+108.10 | +3.5% | Increase |
| Member's Selection Frozen Bone-In Lamb Stew Bag | $98.06 | $97.91 | $-0.15 | -0.2% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $148.87 | $149.73 | $+0.86 | +0.6% | Increase |
| Member's Selection Frozen Bone-In Beef Feet Sliced, Tray | $135.63 | $136.04 | $+0.41 | +0.3% | Increase |
| Fresh Boneless Beef Eye of Round Whole Piece Vacuum Packaged | $404.63 | $407.07 | $+2.44 | +0.6% | Increase |
| Amare Probiotics Sauerkraut / Chucrut 500 g / 17.6 oz | $46.95 | $47.95 | $+1.00 | +2.1% | Increase |
| Cookeen Margarine 6 Units / 227 g / 8 oz | $110.95 | $109.95 | $-1.00 | -0.9% | Decrease |
| Member's Selection Chilled Chicken Liver, Tray Pack | $30.92 | $31.02 | $+0.10 | +0.3% | Increase |

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
| Quantum Energy Bars Cookie Dough Flavor with Chocolate Chips and Peanut Butter with Dark Chocolate 16 Units / 48 g / 1.7 oz | $79.70 | $10.70 | -86.6% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Garcia Chicken & Pork Smoked Sausage 680 g / 1.5 lb | $44.95 | $9.70 | -78.4% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $59.95 | $14.70 | -75.5% |
| Smithfield Smoked and Caramelized Pork Shoulder Cubes 453 g / 1 lb | $177.95 | $44.70 | -74.9% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Toppers Assorted Popcorn 20 Units / 14 g | Toppers | $37.70 | 2026-10-28 |
| Takis Fuego with Hot Chili and Lemon 46 Units / 28 g | Takis | $228.70 | 2026-10-28 |
| KFI Korma Cooking Sauce 2 Units / 650 mL | KFI | $52.70 | 2026-10-28 |
| Lee Kum Kee Traditional Soy Sauce for Cooking and Marinating 2 Units / 500 mL | Lee Kum Kee | $39.95 | 2026-10-28 |
| Chobani Greek Yogurt 20G Protein 8 Units / 296 mL / 10 oz | Chobani | $159.95 | 2026-10-27 |
| Zalea Gourmet Sliced Peaches in Light Syrup 3 Units / 680 g / 24 oz | Zalea Gourmet | $59.70 | 2026-10-27 |
| Smithfield Smoked and Caramelized Pork Shoulder Cubes 453 g / 1 lb | Smithfield | $79.70 | 2026-10-27 |
| San Clemente Seedless Green Grapes 907 g / 2 lb | San Clemente | $89.95 | 2026-10-26 |
| Jo-Sing Chow Mein Noodles 6 Units / 400 g | Jo-Sing | $42.95 | 2026-10-26 |
| Member's Selection Peach Halves 3 Units / 820 g / 28.9 oz | Member's Selection | $49.70 | 2026-10-26 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Re-Lyte Hydration Electrolyte Powder Variety Flavors 30 Units / 6.3 g / 0.22 oz |  | $306.95 | G10D03 |
