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
- **Total products scraped**: 1143
- **Total value**: $126,522.90
- **Average price**: $110.69

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1143
- **Price changes detected**: 33
- **Stock/availability changes**: 8
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 181 |
|  | 134 |
| Badia | 19 |
| Swiss | 15 |
| Brunswick | 10 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Shredded Mozzarella Cheese 453 g / 1 lb | Member's Selection | $27.95 | true |
| Member's Selection Refined Avocado Oil 1 L / 33.8 oz | Member's Selection | $169.95 | true |
| Member's Selection Freshly Baked Vanilla Loaf Cake | Member's Selection | $37.95 | true |
| Cheez-It Original, Grahams, and White Cheddar Cheez-It Gripz Variety Pack 12 Units / 25 g / 0.9 oz | CheezIt | $66.95 | true |
| Mrs Thinster Toasted Coconut Cookies 454 g | Mrs. Thinster's | $89.95 | true |
| Eggo Thick & Fluffy Waffles Original & Blueberry 2 Units / 330 g / 11.6 oz | Eggo | $106.95 | true |
| Califia Farms Lime and Coconut Lemonade 1.4 L / 48 oz | Califia Farms | $54.95 | true |
| Spirella Prosciutto with Mozzarella 454 g / 16 oz |  | $114.95 | true |
| Sunny Fruits Dried Organics Figs 10 Units / 50 g / 1.76 oz | Sunny Fruits | $79.95 | true |
| Swiss Honey Mustard Sauce 2 Units / 454 g | Swiss | $42.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1073
- **Price increases**: 509
- **Price decreases**: 534
- **Average increase**: 7.2%
- **Average decrease**: -5.9%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Frozen Lamb Leg Whole Boneless Tray Pack | $359.44 | $360.91 | $+1.47 | +0.4% | Increase |
| Crix Steelpan Original Cookies in Collectible Tin 768 g | $59.95 | $51.95 | $-8.00 | -13.3% | Decrease |
| Frozen Pork Belly Skin On Sliced Tray  | $116.83 | $116.59 | $-0.24 | -0.2% | Decrease |
| Chilled Chicken Gizzard Tray Pack | $38.92 | $39.05 | $+0.13 | +0.3% | Increase |
| Papaya | $31.71 | $31.84 | $+0.13 | +0.4% | Increase |
| Iceberg Lettuce Unit | $21.95 | $22.95 | $+1.00 | +4.6% | Increase |
| Mini Sweet Peppers 454 g / 1 lb | $39.95 | $44.95 | $+5.00 | +12.5% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $65.39 | $66.20 | $+0.81 | +1.2% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $163.11 | $162.16 | $-0.95 | -0.6% | Decrease |
| Frozen Whole Boneless Pork Tenderloin Vacuum Packaged | $72.78 | $72.90 | $+0.12 | +0.2% | Increase |
| Fresh Chicken Breast Bone In Tray | $87.74 | $88.28 | $+0.54 | +0.6% | Increase |
| Ribeye Choice Fillet Fresh Tray | $298.86 | $296.76 | $-2.10 | -0.7% | Decrease |
| Fine Choice Fresh Marinated Chicken Tray | $81.59 | $81.89 | $+0.30 | +0.4% | Increase |
| Frozen Lamb Shoulder Chops Tray | $121.37 | $121.20 | $-0.17 | -0.1% | Decrease |
| Cauliflower 1 Unit | $44.95 | $39.95 | $-5.00 | -11.1% | Decrease |

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
| Par Excellence Long Grain White Jasmine Rice 4 kg | Par Excellence | $69.95 | 2026-04-15 |
| Solo Ginger Refreshing Drink 8 Units / 1.5 L / 51 oz | Solo | $44.95 | 2026-04-15 |
| Dietz & Watson Chef Carved Ham 1.36 kg / 3 lb | Dietz and Watson | $165.95 | 2026-04-15 |
| Peardrax Sparkling Pear Drink 3 units/ 1 lt | Peardrax | $68.95 | 2026-04-15 |
| Oleoestepa Hojiblanca Extra Virgin Olive Oil 1 L / 34 oz  | Oleoestepa | $114.95 | 2026-04-15 |
| Nescafé Classic Instant Coffee 190 g + Mug | Nescafé | $66.95 | 2026-04-15 |
| Eve Red Kidney Beans 6 Units / 400 g / 14 oz | Eve | $54.95 | 2026-04-15 |
| Ankara Tricolor Pasta 4 Units / 350 g | Ankara | $33.95 | 2026-04-15 |
| Fresh Grape Tomatoes 907 g / 2 lb |  | $67.95 | 2026-04-15 |
| Member's Selection Frozen Bone-In Pork Leg Vacuum Packed | Member's Selection | $455.82 | 2026-04-15 |

## New Products Added Today
No new products added today.
