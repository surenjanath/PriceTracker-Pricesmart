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
- **Total products scraped**: 1130
- **Total value**: $125,290.28
- **Average price**: $110.88

## Database Changes
- **New products added**: 5
- **Existing products updated**: 1125
- **Price changes detected**: 67
- **Stock/availability changes**: 8
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 175 |
|  | 133 |
| Badia | 17 |
| Swiss | 14 |
| Brunswick | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Bombolo Biscotti Assorted Decorated Cookies with Colorful Icing Summer Edition | Bombolo Biscotti | $75.95 | true |
| Crispy Just Baked Mini Naan Bread Bites Baked and Crunchy Snack Style | Crispy Just Baked | $44.95 | true |
| Nature Valley Cinnamon Biscuits with Almond Butter Filling 30 Units 38 g / 1.35 oz | Nature Valley | $138.95 | true |
| Joyburst Sparkling Energy Drink - No Added Sugar 12 Units / 355 mL / 12 oz | Joyburst | $132.95 | true |
| Nature Valley Strawberry Wafer Bars with Oat Butter 20 Units 36 g / 1.3 oz | Nature Valley | $129.95 | true |
| Egregio Organic Extra Virgin Olive Oil 500 mL / 16.9 oz | Egregio | $109.95 | true |
| Jimmy Dean Croissant Sausage, Egg & Cheese Sandwiches 1.53 kg / 3.38 lb | Jimmy Dean | $162.95 | true |
| Virginia Brand Lemon and Garlic Salad Dressing 1 L / 33.8 oz | Virginia Brand | $52.95 | true |
| Häagen-Dazs Assorted Mini Cups Ice Cream 4 Units / 95 mL / 0.32 oz | Haagen Dazs | $54.95 | true |
| Snack Pack Chocolate and Vanilla Pudding 36 Units / 92 g / 3 oz | Snack Pack | $160.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1092
- **Price increases**: 570
- **Price decreases**: 494
- **Average increase**: 7.1%
- **Average decrease**: -5.8%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Banner Farms Straight-Cut French Fries  | $0.00 | $305.95 | $+305.95 | +100.0% | New |
| Dare Chocolate Fudge Cookies 2 Units / 290 g | $54.95 | $63.95 | $+9.00 | +16.4% | Increase |
| Campoverde Spinach, Mango, Apple and Pineapple Mix 907 g / 2 lb | $114.95 | $112.95 | $-2.00 | -1.7% | Decrease |
| Land O' Frost Oven Roasted Chicken 566 g / 1.25 lb | $63.95 | $64.95 | $+1.00 | +1.6% | Increase |
| Island Pride Strawberry Jam 3 Units / 380 g | $0.00 | $44.95 | $+44.95 | +100.0% | New |
| Nescafé Ice Instant Coffee 2 Units / 100 g / 3.5 oz + Glass | $0.00 | $86.95 | $+86.95 | +100.0% | New |
| Kiss Assorted Flavor Glazed Cream-Filled Pastries 8 Units / 75 g | $0.00 | $31.95 | $+31.95 | +100.0% | New |
| Oreo Cookies and Cream Flavor Sandwich Cookies 24 Units / 36 g / 1.26 oz | $0.00 | $58.95 | $+58.95 | +100.0% | New |
| Frozen Lamb Leg Whole Boneless Tray Pack | $342.51 | $344.72 | $+2.21 | +0.6% | Increase |
| Fresh Whole Chicken for Frying Bag | $282.71 | $282.55 | $-0.16 | -0.1% | Decrease |
| Frozen Skinless Boneless Beef Shoulder Clod Steaks Tray | $105.95 | $105.64 | $-0.31 | -0.3% | Decrease |
| Fresh Beef Ribeye Steak Vacuum Packed | $2640.29 | $2768.48 | $+128.19 | +4.9% | Increase |
| Fresh Bone-in Chicken Thighs Tray | $68.51 | $68.44 | $-0.07 | -0.1% | Decrease |
| Frozen Bone In Pork Shoulder Sliced Tray | $75.30 | $75.10 | $-0.20 | -0.3% | Decrease |
| Ocean Delight Frozen Swai Fillet Skinless Bag 907 g / 2 lb | $54.95 | $53.95 | $-1.00 | -1.8% | Decrease |

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
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Garden Foods Mixed Vegetables 1.36 kg / 3 lb | Garden Foods | $54.95 | 2026-06-17 |
| Il Boero Chocolates Filled with Cherry and Liquor 1 kg / 35.2 oz | Il Boero | $99.70 | 2026-06-15 |
| Pure Squeeze Assorted Flavors Sparkling Juice 12 Units / 330 mL / 11.2 oz | Pure Squeeze | $52.70 | 2026-06-15 |
| Swiss Sorrel Drink 3 Units / 750 mL / 25.36 oz | Swiss | $29.70 | 2026-06-14 |
| Fruit Nation Preservative-Free Mango Nectar 36 Units / 200 mL / 6.7 oz | Fruit Nation | $99.70 | 2026-06-14 |
| Sincerely Brigitte Trio Cheese with Guava 567 g / 20 oz | Sincerely  Brigitte | $109.95 | 2026-06-14 |
| Tetley Super Tea Boost Raspberry & Blueberry Tea 3 Units / 40 g  | Tetley | $69.70 | 2026-06-14 |
| Mowi Sweet Frozen Bourbon Salmon Portions 710 g / 1.56 lb | Mowi | $197.95 | 2026-06-12 |
| Black Seedless Grapes 907 g / 2 lb |  | $69.95 | 2026-06-11 |
| Member's Selection Freshly Baked Sweet and Creamy Vanilla Cake 80 to 100 Slices | Member's Selection | $399.95 | 2026-06-11 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Banner Farms Straight-Cut French Fries  | Banner Farms | $305.95 | G10D03 |
| Island Pride Strawberry Jam 3 Units / 380 g | Island Pride | $44.95 | G10D03 |
| Nescafé Ice Instant Coffee 2 Units / 100 g / 3.5 oz + Glass | Nescafé | $86.95 | G10D03 |
| Kiss Assorted Flavor Glazed Cream-Filled Pastries 8 Units / 75 g | Kiss | $31.95 | G10D03 |
| Oreo Cookies and Cream Flavor Sandwich Cookies 24 Units / 36 g / 1.26 oz | Oreo | $58.95 | G10D03 |
