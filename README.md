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

This project has recently gained unexpected attention. It was created for personal, educational purposes ONLY.

* **DO NOT ABUSE THIS SCRIPT:** Do not run it excessively or use it for commercial purposes.
* **RESPECT THE WEBSITE:** Scraping places a load on a website's servers. This script includes a 10-second delay between requests to be respectful. Please do not remove it.
* **USE AT YOUR OWN RISK:** The user is solely responsible for their use of this script. I (the author) am not responsible for any misuse, server overloads, IP bans, or any legal action that may result from its use. This project is provided as-is for educational demonstration.




## Analysis Results

<!--START_SECTION:analysis-->
{{analysis_placeholder}}
# PriceSmart Products Analysis Report

## Basic Analysis
- **Total products scraped**: 1137
- **Total value**: $127,662.55
- **Average price**: $112.28

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1137
- **Price changes detected**: 24
- **Stock/availability changes**: 16
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 188 |
|  | 143 |
| Badia | 18 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Fratelli Beretta Italian Style Platter 340 g / 12 oz  | Fratelli Beretta | $77.95 | true |
| Bella Contadina Italian Antipasto Mix 600 g / 21 oz | Bella Contadina | $77.95 | true |
| Pure Squeeze Assorted Flavors Sparkling Juice 12 Units / 330 mL / 11.2 oz | Pure Squeeze | $119.95 | true |
| Member's Selection Shredded Mozzarella Cheese 2.26 kg / 5 lb | Member's Selection | $126.95 | true |
| Member's Selection Frozen Boneless Salmon Portions with Skin 680 g / 1.5 lb | Member's Selection | $176.95 | true |
| Member's Selection Straight Cut Fry 10 kg / 22 lb | Member's Selection | $162.95 | true |
| Member's Selection Premium Smoked Turkey Breast 2 Units / 340 g / 12 oz | Member's Selection | $81.95 | true |
| Member's Selection Cold Extracted Extra Virgin Olive Oil 2 L | Member's Selection | $134.95 | true |
| Member's Selection Semi-sweet Chocolate Chips 2.04 kg / 72 oz | Member's Selection | $284.95 | true |
| Member's Selection Tuna in Water 6 Units / 136 g / 6 oz | Member's Selection | $63.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1309
- **Price increases**: 726
- **Price decreases**: 499
- **Average increase**: 5.1%
- **Average decrease**: -5.2%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Frozen Lamb Shoulder Case | $1244.44 | $1253.54 | $+9.10 | +0.7% | Increase |
| Pork Leg Frozen  | $66.33 | $66.63 | $+0.30 | +0.5% | Increase |
| Chilled Chicken Gizzard Tray Pack | $57.05 | $56.98 | $-0.07 | -0.1% | Decrease |
| Pork Belly with Skin Frozen Vacuum Packaged | $184.28 | $185.82 | $+1.54 | +0.8% | Increase |
| Nutrina Chilled Whole Chicken Bag | $320.02 | $320.17 | $+0.15 | +0.0% | Increase |
| LAY'S Classic Toasted Chips 425.2 g / 15 oz | $19.70 | $39.95 | $+20.25 | +102.8% | Increase |
| Fresh Whole Chicken 2 Units | $105.27 | $104.92 | $-0.35 | -0.3% | Decrease |
| Frozen Boneless Skinless Chicken Breast Tray | $181.89 | $180.76 | $-1.13 | -0.6% | Decrease |
| Whole Rack Frozen Baby Back Ribs Vacuum Packaged | $151.22 | $151.79 | $+0.57 | +0.4% | Increase |
| Fresh Ground Chicken Meat Bag | $279.47 | $278.41 | $-1.06 | -0.4% | Decrease |
| Frozen Whole Boneless Pork Tenderloin Vacuum Packaged | $75.41 | $75.29 | $-0.12 | -0.2% | Decrease |
| Fine Choice Fresh Marinated Chicken Tray | $92.51 | $92.69 | $+0.18 | +0.2% | Increase |
| Frozen Bone-In Pork Spare Rib Vacuum Packaged | $158.13 | $157.50 | $-0.63 | -0.4% | Decrease |
| Fresh Chicken Breast Bone In Tray | $95.71 | $95.61 | $-0.10 | -0.1% | Decrease |
| Member's Selection Frozen Bone-In Lamb Stew Bag | $86.77 | $86.90 | $+0.13 | +0.1% | Increase |

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
| Nature Valley Wafers Crispy and Creamy Bars 20 Units / 36 g / 1.3 oz | Nature Valley | $139.95 | 2025-10-24 |
| Red Grapes with Seeds 907 g / 2 lb |  | $59.45 | 2025-10-24 |
| Setton Farms Dark Chocolate Covered Pistachios and Cranberries 680 g / 24 oz | Setton Farms | $129.95 | 2025-10-24 |
| Member's Selection Freshly Made Fried Chicken 8 Pieces | Member's Selection | $105.00 | 2025-10-23 |
| Upper Crust Bakery Mini Soft and Creamy Brownie Pastries 32 Units | Upper Crust Bakery | $102.95 | 2025-10-23 |
| Post Cereal Fruity Pebbles 1.07 kg / 38 oz | Post | $75.45 | 2025-10-22 |
| Member's Selection Salad Tomato 1.5 kg / 3.5 lb | Member's Selection | $32.57 | 2025-10-22 |
| Member's Selection Frozen Skin On Boneless Trout Fillet Vacuum Packaged Bag | Member's Selection | $207.41 | 2025-10-22 |
| Fresh Regular Tomato |  | $33.61 | 2025-10-20 |
| Russet Potato 2.2 kg / 5 lb |  | $22.95 | 2025-10-20 |

## New Products Added Today
No new products added today.
