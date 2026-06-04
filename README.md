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
- **Total products scraped**: 1134
- **Total value**: $124,722.48
- **Average price**: $109.98

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1132
- **Price changes detected**: 62
- **Stock/availability changes**: 13
- **Discontinued products**: 3

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 176 |
|  | 132 |
| Badia | 17 |
| Swiss | 15 |
| Brunswick | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Jimmy Dean Croissant Sausage, Egg & Cheese Sandwiches 1.53 kg / 3.38 lb | Jimmy Dean | $162.95 | true |
| Joyburst Sparkling Energy Drink - No Added Sugar 12 Units / 355 mL / 12 oz | Joyburst | $136.95 | true |
| Nature Valley Strawberry Wafer Bars with Oat Butter 20 Units 36 g / 1.3 oz | Nature Valley | $132.95 | true |
| Egregio Organic Extra Virgin Olive Oil 500 mL / 16.9 oz | Egregio | $114.95 | true |
| Butterball Turkey Sausage 3 Units / 369 g / 13 oz | Butterball | $129.95 | true |
| Häagen-Dazs Assorted Mini Cups Ice Cream 4 Units / 95 mL / 0.32 oz | Haagen Dazs | $54.95 | true |
| Snack Pack Chocolate and Vanilla Pudding 36 Units / 92 g / 3 oz | Snack Pack | $160.95 | true |
| Crispy Just Baked Mini Naan Bread Bites Baked and Crunchy Snack Style | Crispy Just Baked | $44.95 | true |
| Nature Valley Cinnamon Biscuits with Almond Butter Filling 30 Units 38 g / 1.35 oz | Nature Valley | $138.95 | true |
| Virginia Brand Lemon and Garlic Salad Dressing 1 L / 33.8 oz | Virginia Brand | $52.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1169
- **Price increases**: 595
- **Price decreases**: 541
- **Average increase**: 6.4%
- **Average decrease**: -5.4%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Cavendish Farms Hash Browns 1.2 kg / 2.6 lb | $56.95 | $55.95 | $-1.00 | -1.8% | Decrease |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $137.95 | $134.95 | $-3.00 | -2.2% | Decrease |
| Oscar Mayer Turkey Bacon 3 Units / 340 g / 12 oz | $139.95 | $142.95 | $+3.00 | +2.1% | Increase |
| Watermelon 1 kg / 2.2 lb | $76.27 | $76.02 | $-0.25 | -0.3% | Decrease |
| Catalina Ham Croquettes 1.3 kg / 47 oz | $74.95 | $82.95 | $+8.00 | +10.7% | Increase |
| Frozen Lamb Leg Whole Vacuum Packed | $392.41 | $394.14 | $+1.73 | +0.4% | Increase |
| Philadelphia Strawberry Cream Cheese 2 Units / 212 g / 7.5 oz | $0.00 | $79.95 | $+79.95 | +100.0% | New |
| Fratelli Beretta Italian Style Platter 340 g / 12 oz  | $82.95 | $81.95 | $-1.00 | -1.2% | Decrease |
| Gouda Cheese Block | $90.10 | $89.97 | $-0.13 | -0.1% | Decrease |
| Frozen Bone In Pork Shoulder Sliced Tray | $77.31 | $77.52 | $+0.21 | +0.3% | Increase |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $153.65 | $152.30 | $-1.35 | -0.9% | Decrease |
| Silk Chocolate Almond 1.89 L / 64 oz | $56.95 | $55.95 | $-1.00 | -1.8% | Decrease |
| Fresh Bone-in Chicken Thighs Tray | $68.78 | $68.71 | $-0.07 | -0.1% | Decrease |
| Wrigley's Extra Spearmint Sugar-Free Gum 10 Packs 37.5 g / 1.32 oz | $0.00 | $102.95 | $+102.95 | +100.0% | New |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $221.12 | $222.52 | $+1.40 | +0.6% | Increase |

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
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |

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
|  Best Fruit Ripe Dehydrated Mangoes 4 Units / 100 g | Best Fruit | $82.70 | 2026-06-03 |
| Philly Gourmet Pure Beef Sliced Steaks 1 kg / 2.4 lb | Philly Gourmet | $96.95 | 2026-06-03 |
| Frozen Imported Pork Leg Slices |  | $70.14 | 2026-06-03 |
| Heinz Tomato Ketchup 12 Units / 591.5 mL / 20 oz | Heinz | $249.95 | 2026-06-02 |
| Wellsley Farms Spinach & Cheese Spanakopita 822 g / 1.8 lb | Wellsley Farms | $139.95 | 2026-06-01 |
| Mrs. Field's Chocolate Chip Cookie 20 Units / 59 g  / 2.1 oz  | Mrs. Fields | $114.95 | 2026-06-01 |
| Green pepper |  | $59.19 | 2026-06-01 |
| Frozen Skinless Boneless Beef Shoulder Clod Case |  | $1443.44 | 2026-06-01 |
| Frozen Bone-In Pork Shoulder Vacuum Packed |  | $194.41 | 2026-06-01 |
| Nongshim Shin Gold with Chicken Broth Flavor 4 Units / 130 g / 4.58 oz | Nongshim | $67.95 | 2026-05-31 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Philadelphia Strawberry Cream Cheese 2 Units / 212 g / 7.5 oz | Philadelphia | $79.95 | G10D03 |
| Wrigley's Extra Spearmint Sugar-Free Gum 10 Packs 37.5 g / 1.32 oz | Wrigley's | $102.95 | G10D03 |
