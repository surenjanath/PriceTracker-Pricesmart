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
- **Total products scraped**: 1173
- **Total value**: $134,489.99
- **Average price**: $114.65

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1172
- **Price changes detected**: 26
- **Stock/availability changes**: 8
- **Discontinued products**: 2

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 174 |
|  | 144 |
| Swiss | 16 |
| Badia | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Carmencita Mediterranean Spice Mix with Grinder 190 g / 6.7 oz | Carmencita | $48.95 | true |
| Krusteaz Cinnamon Swirl Crumb Cake & Muffin Mix with Toppings 3 Units / 411 g / 14.5 oz | Krusteaz | $94.95 | true |
| Carmencita Himalayan Pink Salt with Grinder 370 g / 13 oz | Carmencita | $41.45 | true |
| Member's Selection Extra Virgin Olive Oil 750 mL / 25.36 oz | Member's Selection | $69.95 | true |
| Chief Ground Split Peas for Soups and Dhal 1.2 kg | Chief | $36.95 | true |
| aribbean Flavours Creamy Egg-Free Mayonnaise 3 Units / 330 mL | Karibbean Flavours | $52.95 | true |
| Carretilla Quinoa Salad with Chili Dressing Ready to Eat 4 Units 230 g / 8.8 oz | Carretilla | $129.95 | true |
| Delve Dip Variety Pack 3 Units / 170 g / 6 oz | Delve | $109.95 | true |
| Rip Van Dark Chocolate Vegan Wafer Cookies 24 Units / 22 g / 0.78 oz | Rip Van | $146.95 | true |
| Poppycock Gourmet Caramel Popcorn with Cashews 850 g / 30 oz | Poppycock | $169.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1233
- **Price increases**: 684
- **Price decreases**: 496
- **Average increase**: 8.9%
- **Average decrease**: -6.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Papaya | $37.77 | $37.74 | $-0.03 | -0.1% | Decrease |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $44.70 | $114.95 | $+70.25 | +157.2% | Increase |
| Sunshine Snacks SunMix Assorted Nut Bars 24 Units / 37 g / 1.31 oz | $0.00 | $114.95 | $+114.95 | +100.0% | New |
| Tostitos Santa Elena Chips 430 g  / 15.17 oz | $32.95 | $39.95 | $+7.00 | +21.2% | Increase |
| Frozen Lamb Leg Whole Boneless Tray Pack | $353.55 | $342.51 | $-11.04 | -3.1% | Decrease |
| Stahl Meyer Whole Smoked Frozen Turkey Thigh | $156.46 | $149.44 | $-7.02 | -4.5% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $145.74 | $149.73 | $+3.99 | +2.7% | Increase |
| Member's Selection Chilled Boneless Beef Eye of Round Roast, Tray | $241.88 | $242.45 | $+0.57 | +0.2% | Increase |
| Fresh Boneless Beef Eye of Round Whole Piece Vacuum Packaged | $415.33 | $414.58 | $-0.75 | -0.2% | Decrease |
| Member's Selection Frozen Bone-In Lamb Stew Bag | $95.55 | $95.41 | $-0.14 | -0.1% | Decrease |
| Gouda Cheese Block | $90.92 | $91.05 | $+0.13 | +0.1% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Case | $1608.85 | $1654.85 | $+46.00 | +2.9% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $112.22 | $116.51 | $+4.29 | +3.8% | Increase |
| Nutrina Chilled Whole Chicken Bag | $344.59 | $344.76 | $+0.17 | +0.0% | Increase |
| Frozen Bone In Pork Shoulder Sliced Tray | $75.40 | $75.29 | $-0.11 | -0.1% | Decrease |

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
| SeaPak Garlic Butter Shrimp 680 g / 1.5 lb | SeaPak | $69.70 | 2026-10-23 |
| Frozen Boneless Pork Loin Vacuum Packaged |  | $264.33 | 2026-10-23 |
| Apple & Eve Organic Orange Carrot Juice 2 Units / 2.84 L / 96 oz | Apple & Eve | $70.70 | 2026-10-22 |
| Polly-O String Cheese Mozzarella & Cheddar 24 Units | Polly-O | $59.70 | 2026-10-22 |
| Reny Picot Camembert Cheese 397 g / 14 oz | Reny Picot | $69.95 | 2026-10-22 |
| Farmer Joe's Pineapple Tid Bits 3 060 g | Farmer Joe's | $69.95 | 2026-10-21 |
| Nescafé Ice Instant Coffee 2 Units / 100 g / 3.5 oz + Glass | Nescafé | $86.95 | 2026-10-21 |
| Dasani Water 24 Units / 500 mL / 17 oz | Dasani | $29.95 | 2026-10-21 |
| Nature's Heart Extra Creamy Vanilla Flavor Almond Drink 3 Units / 946 mL | Nature's Heart | $59.95 | 2026-10-21 |
| Sprite Zero Sugar Soda in Cans 12 Units / 355 mL / 12 oz | Sprite | $49.95 | 2026-10-21 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Sunshine Snacks SunMix Assorted Nut Bars 24 Units / 37 g / 1.31 oz | Sunshine Snacks | $114.95 | G10D03 |
