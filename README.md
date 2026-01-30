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
- **Total products scraped**: 1163
- **Total value**: $132,980.83
- **Average price**: $114.34

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1162
- **Price changes detected**: 36
- **Stock/availability changes**: 7
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 188 |
|  | 136 |
| Badia | 18 |
| Swiss | 14 |
| Kiss | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Organic Trail Mix with Cranberries 737 g / 26 oz | Member's Selection | $164.95 | true |
| Member's Selection Canola Oil Spray 2 Units 400 mL / 13.5 oz | Member's Selection | $79.95 | true |
| Izzio Artisan Naturally Fermented Sourdough Bread Sliced | Izzio | $49.95 | true |
| Bob's Red Mill Oatmeal with Protein 1.81 kg / 4 lb | Bob's Red Mill | $144.95 | true |
| Terra Creta Extra Virgin Olive Oil in Marasca 1 L / 33.81 oz | Terra Creta | $119.95 | true |
| Coffee Toppers Salted Caramel Whipped Cream 2 Units / 425 g / 15 oz | Coffee Toppers | $79.95 | true |
| Galvanina Lemon Flavor Sparkling Mineral Water 24 Units / 500 mL / 16.9 oz | Galvanina | $169.95 | true |
| Izzio Artisanal Sourdough Focaccia Bread with Rosemary, Garlic, and Olive Oil Ready to Bake | Izzio | $39.95 | true |
| Copper Kettle Dark Chocolate Truffles with Sea Salt 448 g / 16 oz | Copper Kettle | $139.95 | true |
| Diamond Shelled Walnuts 907 g / 32 oz | Diamond | $137.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1006
- **Price increases**: 435
- **Price decreases**: 535
- **Average increase**: 11.9%
- **Average decrease**: -5.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Peas and Beans Assorted Grains 5 Units / 800 g | $99.95 | $129.95 | $+30.00 | +30.0% | Increase |
| Samyang Four Cheese and Ramen Flavor Instant Noodle Soup 5 Units / 140 g | $69.95 | $61.95 | $-8.00 | -11.4% | Decrease |
| Red Grape Seedless 907 g / 2 lb | $69.95 | $99.95 | $+30.00 | +42.9% | Increase |
| Fresh Strawberry 454 g / 1 lb | $34.95 | $49.95 | $+15.00 | +42.9% | Increase |
| Pork Belly with Skin Frozen Vacuum Packaged | $188.26 | $186.11 | $-2.15 | -1.1% | Decrease |
| Frozen Lamb Shoulder Case | $1426.95 | $1488.78 | $+61.83 | +4.3% | Increase |
| Fresh Beef Eye of Round Case | $4037.01 | $4477.73 | $+440.72 | +10.9% | Increase |
| Plum 907 g / 2 lb | $82.95 | $84.95 | $+2.00 | +2.4% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $84.78 | $84.70 | $-0.08 | -0.1% | Decrease |
| Fresh Start Mauby Concentrate 3 Units / 750 mL / 25.3 oz | $34.95 | $39.95 | $+5.00 | +14.3% | Increase |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $195.00 | $194.70 | $-0.30 | -0.2% | Decrease |
| Nutrina Chilled Whole Chicken Bag | $329.60 | $328.40 | $-1.20 | -0.4% | Decrease |
| Frozen Bone In Pork Shoulder Sliced Tray | $79.52 | $79.63 | $+0.11 | +0.1% | Increase |
| Fresh Chicken Breast Bone In Tray | $96.95 | $96.86 | $-0.09 | -0.1% | Decrease |
| Red Onion 2.2 kg / 5 lb | $34.95 | $32.95 | $-2.00 | -5.7% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Carrot 2.27 kg / 5 lb | $9.70 | $37.95 | +291.2% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $29.70 | $89.95 | +202.9% |
| Hillshire Farm Ham Mix 3 Units / 454 g / 16 oz | $69.70 | $194.95 | +179.7% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $34.70 | $89.95 | +159.2% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Hillshire Farm Ham Mix 3 Units / 454 g / 16 oz | $194.95 | $69.70 | -64.2% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $109.95 | $39.70 | -63.9% |
| Pop-Tarts Snack Crunchy Poppers Filled with Strawberry and Brownie 2 Units 360 g / 12.6 oz  | $174.95 | $64.70 | -63.0% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $34.70 | -61.4% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| McCain Mac and Cheese Triangles 2 Units / 400 g / 14 oz | McCain | $59.70 | 2026-01-29 |
| Member's Selection Freshly Baked Sweet and Creamy Vanilla Cake 80 to 100 Slices | Member's Selection | $399.95 | 2026-01-28 |
| Frozen Skin On Trout Fillet Vacuum Packaged Case |  | $1869.50 | 2026-01-28 |
| Sea Best Raw Lobster Cake 762 g / 1.68 lb | Sea Best | $131.95 | 2026-01-28 |
| Muffin Town Mini Bread Cake with Cinnamon Crumbs Topping | Muffin Town | $47.70 | 2026-01-26 |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | Kozyshack | $89.95 | 2026-01-25 |
| Wellsley Farms Apple Cider 3.8 L / 128 oz | Wellsley Farms | $76.95 | 2026-01-25 |
| Gouda Cheese Block |  | $85.48 | 2026-01-22 |
| Swift Frozen Pork Ribs Kansas City Style BBQ Vacuum Packing | Swift | $1169.78 | 2026-01-22 |
| Orchard Orange Drink 24 Units / 250 mL | Orchard | $85.95 | 2026-01-21 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Welch's Sparkling Rose Non-Alcoholic 3 Units / 750 mL | Welch's | $105.95 | G10D03 |
