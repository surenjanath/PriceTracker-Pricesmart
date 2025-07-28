# PriceSmart Products Web Scraper

This is a Python web scraper designed to fetch product data from PriceSmart's API at [https://www.pricesmart.com](https://www.pricesmart.com) and store them in a SQLite database. It utilizes asyncio and aiohttp for asynchronous API calls and SQLAlchemy for database operations.

## About PriceSmart

PriceSmart is a membership-based warehouse club operator in the Caribbean and Central America. This scraper focuses on extracting product information from their Trinidad and Tobago (TT) store, including groceries, electronics, household items, and more.

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

## Analysis Results

<!--START_SECTION:analysis-->
{{analysis_placeholder}}
# PriceSmart Products Analysis Report

## Basic Analysis
- **Total products scraped**: 1085
- **Total value**: $116,806.23
- **Average price**: $107.66

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1085
- **Price changes detected**: 0
- **Stock/availability changes**: 0
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 180 |
|  | 123 |
| Badia | 15 |
| Swiss | 14 |
| Kirkland Signature | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Terra Creta Greek Extra Virgin Olive Oil 500 mL / 16.9 oz | Terra Creta | $79.95 | true |
| Galbani Galbani Mozzarella Cheese 907 g / 32 oz | Galbani | $59.95 | true |
| Sunberry Farms Organic Mango Nectar Juice - Gluten Free 3.78 L / 128 oz | Sunberry Farms | $84.95 | true |
| Chobani Greek Yogurt Vanilla 1.13 kg / 40 oz | Chobani | $85.95 | true |
| Creamery Novelties Neapolitan Ice Cream 3.78 L / 127.8 oz | Creamery Novelties | $49.95 | true |
| Califia Farms Matcha Latte Almond Milk 1.4 L / 48 oz | Califia Farms | $72.95 | true |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | Kozyshack | $87.95 | true |
| Sunny D Tangy Original Orange Flavor Citrus Drink 2 Units / 1.89 L | SunnyD | $59.95 | true |
| Member's Selection Frozen Boneless Salmon Portions with Skin 680 g / 1.5 lb | Member's Selection | $169.95 | true |
| Member's Selection Cold Extracted Extra Virgin Olive Oil 2 L | Member's Selection | $134.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1085
- **Price increases**: 0
- **Price decreases**: 0
- **Average increase**: 0.0%
- **Average decrease**: 0.0%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Dare Vinta Crackers with Cereals and Seeds 2 Units / 200 g | $0.00 | $19.70 | $+19.70 | +100.0% | New |
| Svelty Skimmed Milk 6 Units / 1 L | $0.00 | $94.95 | $+94.95 | +100.0% | New |
| Jayone Yizu Citrus Flavored Sweet Crispy Rice Rolls 2 Units / 80 g | $0.00 | $39.95 | $+39.95 | +100.0% | New |
| Señor Rico Three Milks Flan 12 Units / 113 g / 4 oz | $0.00 | $148.95 | $+148.95 | +100.0% | New |
| Apple & Eve Organic Orange Carrot Juice 2 Units / 2.84 L / 96 oz | $0.00 | $79.70 | $+79.70 | +100.0% | New |
| RW Garcia Sweet Potato Gluten-Free Crackers 2 Units / 425 g / 15 oz | $0.00 | $106.95 | $+106.95 | +100.0% | New |
| Jamaican Mount Peak Golden Turmeric Latte Coffee with Milk 144 g / 5 oz | $0.00 | $89.95 | $+89.95 | +100.0% | New |
| Florida's Natural Lemonade 2 Units 1.75 L / 59 oz | $0.00 | $89.95 | $+89.95 | +100.0% | New |
| Celorrio Spanish Tomato Sauce 6 Units / 400 g / 14 oz | $0.00 | $29.70 | $+29.70 | +100.0% | New |
| Chef's Quality Crinkle Cut Fries 2.5kg / 5.5 lb | $0.00 | $49.95 | $+49.95 | +100.0% | New |
| Schweppes Chaser Assorted Flavor Soft Drink 24 Units / 237 mL | $0.00 | $84.95 | $+84.95 | +100.0% | New |
| Lay's Salt and Vinegar Potato Chips 184 g / 6.49 oz | $0.00 | $33.95 | $+33.95 | +100.0% | New |
| YoguRico Mango Low Fat Drinkable Yogurt 1.68 L / 57 oz | $0.00 | $52.95 | $+52.95 | +100.0% | New |
| Best Fruit Lover's Sweet and Hot Flavored Prunes 453g | $0.00 | $64.95 | $+64.95 | +100.0% | New |
| Dare Viva Puffs Strawberry Cookies 2 Units / 300 g | $0.00 | $49.95 | $+49.95 | +100.0% | New |

## Biggest Price Increases (All Time)
No price increases recorded.

## Biggest Price Decreases (All Time)
No price decreases recorded.

## Recently Discontinued Products
No discontinued products.

## New Products Added Today
No new products added today.
