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
- **Total products scraped**: 1145
- **Total value**: $128,037.83
- **Average price**: $111.82

## Database Changes
- **New products added**: 1
- **Existing products updated**: 1144
- **Price changes detected**: 55
- **Stock/availability changes**: 7
- **Discontinued products**: 5

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 189 |
|  | 142 |
| Badia | 18 |
| Swiss | 13 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Trail Mix with Cranberries, Cashews, and Walnuts 850 g / 30 oz | Member's Selection | $122.95 | true |
| Member's Selection Tropical Trail Mix with Nuts and Dried Fruit 850 g / 30 oz | Member's Selection | $119.95 | true |
| Member's Selection Mild Cheddar Cheese 907 g / 2 lb | Member's Selection | $59.95 | true |
| Hershey's Cocoa Powder 652 g / 23 oz | Hershey's | $121.95 | true |
| Pure Squeeze Assorted Flavors Sparkling Juice 12 Units / 330 mL / 11.2 oz | Pure Squeeze | $124.95 | true |
| Mariani Dried Red Fruit Mix with Cherries, Blueberries, and Strawberries 567 g / 20 oz | Mariani | $92.95 | true |
| Jackson's Sweet Potato Chips 454 g / 16 oz | Jackson's | $79.95 | true |
| Del Alba Mixed Nuts Christmas Edition 660 g / 23.3 oz | Del Alba | $96.95 | true |
| Quaker Quick Oats 2 Units /  1.13 kg / 40 oz | Quaker | $88.95 | true |
| Food With Purpose Sparkling Tea Infused with Fruit Juice - Sugar Free 12 Units / 250 mL / 8.5 oz | Food with Purpose | $114.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1416
- **Price increases**: 788
- **Price decreases**: 558
- **Average increase**: 4.9%
- **Average decrease**: -5.9%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Cranberry 907 g / 2 lb | $0.00 | $39.95 | $+39.95 | +100.0% | New |
| Frozen Imported Pork Leg Slices | $80.93 | $81.14 | $+0.21 | +0.3% | Increase |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $107.10 | $107.26 | $+0.16 | +0.1% | Increase |
| Chilled Chicken Gizzard Tray Pack | $57.12 | $57.20 | $+0.08 | +0.1% | Increase |
| Pork Belly with Skin Frozen Vacuum Packaged | $186.48 | $181.20 | $-5.28 | -2.8% | Decrease |
| Mini Sweet Peppers 454 g / 1 lb | $37.95 | $29.95 | $-8.00 | -21.1% | Decrease |
| Bosc Pear 1.36 kg / 3 lb | $74.95 | $54.95 | $-20.00 | -26.7% | Decrease |
| Baby Carrots 907 g / 2 lb | $34.95 | $29.95 | $-5.00 | -14.3% | Decrease |
| Mucci Farms Snack Cucumbers 681 g / 1.5 lb | $59.95 | $44.95 | $-15.00 | -25.0% | Decrease |
| Red Onion 2.2 kg / 5 lb | $34.95 | $29.95 | $-5.00 | -14.3% | Decrease |
| Plum 907 g / 2 lb | $74.95 | $62.95 | $-12.00 | -16.0% | Decrease |
| Fresh Melon | $49.95 | $39.95 | $-10.00 | -20.0% | Decrease |
| Wellsley Farms Apple Cider 3.8 L / 128 oz | $76.95 | $39.70 | $-37.25 | -48.4% | Decrease |
| Green Cabbage 1.3 kg / 2.9 lb | $34.95 | $24.95 | $-10.00 | -28.6% | Decrease |
| Fresh Red Apples 1.36 kg / 3 lb | $57.95 | $42.95 | $-15.00 | -25.9% | Decrease |

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
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $109.95 | $39.70 | -63.9% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $34.70 | -61.4% |
| Black Seedless Grapes 907 g / 2 lb | $64.95 | $29.70 | -54.3% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Green Seedless Grapes 907 g / 2 lb | $62.95 | $29.70 | -52.8% |
| Leclerc Summer Cookies with Raspberry and Berry Flavor 2 Units / 300 g | $41.70 | $19.70 | -52.8% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Brussels Sprouts 454 g / 1 lb |  | $34.95 | 2025-11-14 |
| Belgioioso Fresh Mozzarella Pearls 453 g / 1 lb | Belgioioso | $57.95 | 2025-11-14 |
| Fresh Halloween Pumpkin |  | $49.70 | 2025-11-14 |
| Baby Bottle Pop Assorted Flavor Sweet Powder Candies 20 Units / 24 g / 0.85 oz | Baby Bottle Pop | $99.70 | 2025-11-14 |
| Pink Lady Apples 1.36 kg / 3 lb |  | $67.95 | 2025-11-14 |
| Island Pride Sardines in Tomato Sauce, Oil and Brine 4 Units / 425 g | Island Pride | $39.95 | 2025-11-13 |
| Takis Fuego Tortilla Chips Snack Hot Chili Pepper & Lime 30.75 oz | Takis | $159.95 | 2025-11-13 |
| Lava Bits Chocolate Filled Cookies 6 Units / 150 g | Lava Bits | $24.70 | 2025-11-13 |
| Red Potato 4.5 kg / 10 lb |  | $69.95 | 2025-11-13 |
| Nanak Gulabjamun 12 Units 908 g / 2 lb | Nanak | $79.95 | 2025-11-13 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Cranberry 907 g / 2 lb |  | $39.95 | G10D03 |
