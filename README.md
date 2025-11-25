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
- **Total products scraped**: 1150
- **Total value**: $128,834.62
- **Average price**: $112.03

## Database Changes
- **New products added**: 3
- **Existing products updated**: 1147
- **Price changes detected**: 21
- **Stock/availability changes**: 23
- **Discontinued products**: 2

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 187 |
|  | 144 |
| Badia | 18 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Food With Purpose Sparkling Tea Infused with Fruit Juice - Sugar Free 12 Units / 250 mL / 8.5 oz | Food with Purpose | $114.95 | true |
| Mariani Dried Red Fruit Mix with Cherries, Blueberries, and Strawberries 567 g / 20 oz | Mariani | $92.95 | true |
| Jackson's Sweet Potato Chips 454 g / 16 oz | Jackson's | $82.95 | true |
| Crazy Monkey Baking Granola Snacks with Dark Chocolate 680 g / 1.5 lb | Crazy Monkey Baking | $119.95 | true |
| Nescafé Gold Instant Coffee 190 g | Nescafé | $104.95 | true |
| Pepe's Nature´s Pride Pack of Peas and Dry Legumes 5 Units / 1 kg | Pepe's Nature's Pride | $129.95 | true |
| President Brie Cheese 555 g / 1.2 lb | President | $77.95 | true |
| Chuckanut Bay Chocalate Covered Cheesecake Bites 634 g / 1.4 lb | Chuckanut Bay | $139.95 | true |
| Badia Mojo Rub Citrus Blend 680.4 g / 24 oz  | Badia | $89.95 | true |
| Daisy Cottage Cheese 454 g / 16 oz  | Daisy | $56.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1294
- **Price increases**: 708
- **Price decreases**: 527
- **Average increase**: 5.2%
- **Average decrease**: -5.6%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Salad Tomato 1.5 kg / 3.5 lb | $28.95 | $27.95 | $-1.00 | -3.5% | Decrease |
| Mixed Tomato Cherry 907 g / 2 lb | $57.95 | $49.95 | $-8.00 | -13.8% | Decrease |
| Reny Picot Brie Cheese with Almond Slices 227 g / 8 oz | $0.00 | $89.95 | $+89.95 | +100.0% | New |
| Fresh Grape Tomatoes 907 g / 2 lb | $44.95 | $42.95 | $-2.00 | -4.4% | Decrease |
| Nestlé Chocolate-Flavored Powder Drink with Mini Marshmallows 16 Units / 24.2 g / 0.85 oz | $0.00 | $49.95 | $+49.95 | +100.0% | New |
| Member's Selection Iced Coffee Mocha Drink 12 Units / 296 mL / 10 oz | $0.00 | $154.95 | $+154.95 | +100.0% | New |
| Mucci Farms Snack Cucumbers 681 g / 1.5 lb | $69.95 | $59.95 | $-10.00 | -14.3% | Decrease |
| Fresh Bone-in Chicken Thighs Tray | $81.60 | $81.43 | $-0.17 | -0.2% | Decrease |
| Fresh Seasoned BBQ Chicken Quarters Bag | $94.93 | $94.75 | $-0.18 | -0.2% | Decrease |
| Central Farms Frozen Whole Duck Cut Up Vacuum Packaged 2.3 Kg / 5 lb | $134.95 | $139.95 | $+5.00 | +3.7% | Increase |
| Fine Choice Fresh Marinated Chicken Tray | $94.31 | $94.22 | $-0.09 | -0.1% | Decrease |
| Fresh Whole Chicken for Frying Bag | $267.30 | $265.51 | $-1.79 | -0.7% | Decrease |
| Pork Chop with Bone Frozen Tray | $84.10 | $84.23 | $+0.13 | +0.2% | Increase |
| Frozen Lamb Shoulder Chops Tray | $130.57 | $130.39 | $-0.18 | -0.1% | Decrease |
| Iceberg Lettuce Unit | $39.95 | $37.95 | $-2.00 | -5.0% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $29.70 | $89.95 | +202.9% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $34.70 | $89.95 | +159.2% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Black Seedless Grapes 907 g / 2 lb | $29.70 | $64.95 | +118.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $109.95 | $39.70 | -63.9% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $34.70 | -61.4% |
| Black Seedless Grapes 907 g / 2 lb | $64.95 | $29.70 | -54.3% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Green Seedless Grapes 907 g / 2 lb | $62.95 | $29.70 | -52.8% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| KC Candy Sweet Lollipops Filled with Bubblegum - Ideal for Parties 120 Units / 1800 g | KC Candy | $74.95 | 2025-11-24 |
| Member's Selection Shredded Mozzarella Cheese 5 Units / 453 g / 1 lb | Member's Selection | $144.95 | 2025-11-24 |
| Mott's 100% Natural Apple Juice 1.89 L | Mott's | $45.95 | 2025-11-23 |
| Crix Steelpan Original Cookies in Collectible Tin 768 g | Crix | $59.95 | 2025-11-23 |
| Klim Powdered Milk 1.6 kg / 56.4 oz | Klim | $109.95 | 2025-11-20 |
| Bumble Bee Solid White Albacore in Water 4 Units / 142 g / 5 oz | Bumble Bee | $43.95 | 2025-11-20 |
| Nongshim Korean Instant Ramen Soup Original Flavor 6 Units / 75 g | Nongshim | $79.95 | 2025-11-19 |
| Member’s Selection Coconut Swiss Roll  | Member's Selection | $31.95 | 2025-11-19 |
| Member's Selection Thai Hom Mali Jasmine Rice 9.07 kg / 20 lb | Member's Selection | $139.95 | 2025-11-19 |
| Gouda Cheese Block |  | $86.98 | 2025-11-19 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Reny Picot Brie Cheese with Almond Slices 227 g / 8 oz | Reny Picot | $89.95 | G10D03 |
| Nestlé Chocolate-Flavored Powder Drink with Mini Marshmallows 16 Units / 24.2 g / 0.85 oz | Nestle | $49.95 | G10D03 |
| Member's Selection Iced Coffee Mocha Drink 12 Units / 296 mL / 10 oz | Member's Selection | $154.95 | G10D03 |
