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
- **Total products scraped**: 1144
- **Total value**: $129,069.24
- **Average price**: $112.82

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1144
- **Price changes detected**: 25
- **Stock/availability changes**: 37
- **Discontinued products**: 1

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 190 |
|  | 144 |
| Badia | 18 |
| Swiss | 13 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Pure Squeeze Assorted Flavors Sparkling Juice 12 Units / 330 mL / 11.2 oz | Pure Squeeze | $124.95 | true |
| Fratelli Beretta Italian Style Platter 340 g / 12 oz  | Fratelli Beretta | $77.95 | true |
| Bella Contadina Italian Antipasto Mix 600 g / 21 oz | Bella Contadina | $77.95 | true |
| Member's Selection Shredded Mozzarella Cheese 2.26 kg / 5 lb | Member's Selection | $125.95 | true |
| Member's Selection Frozen Boneless Salmon Portions with Skin 680 g / 1.5 lb | Member's Selection | $174.95 | true |
| Member's Selection Tuna in Water 6 Units / 136 g / 6 oz | Member's Selection | $63.95 | true |
| Member's Selection Straight Cut Fry 10 kg / 22 lb | Member's Selection | $162.95 | true |
| Member's Selection Cold Extracted Extra Virgin Olive Oil 2 L | Member's Selection | $134.95 | true |
| Member's Selection Semi-sweet Chocolate Chips 2.04 kg / 72 oz | Member's Selection | $294.95 | true |
| Member's Selection Premium Smoked Turkey Breast 2 Units / 340 g / 12 oz | Member's Selection | $83.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1415
- **Price increases**: 793
- **Price decreases**: 550
- **Average increase**: 5.1%
- **Average decrease**: -5.2%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Green pepper | $39.09 | $34.73 | $-4.36 | -11.2% | Decrease |
| Frozen Imported Pork Leg Slices | $86.00 | $84.59 | $-1.41 | -1.6% | Decrease |
| Frozen Lamb Leg Whole Vacuum Packed | $352.97 | $363.04 | $+10.07 | +2.9% | Increase |
| Fresh Seasoned BBQ Chicken Quarters Bag | $95.47 | $95.65 | $+0.18 | +0.2% | Increase |
| Rockit Apple 1.36 kg / 3 lb | $77.95 | $69.95 | $-8.00 | -10.3% | Decrease |
| Fresh Chicken Mixed Parts Tray | $95.28 | $95.39 | $+0.11 | +0.1% | Increase |
| Fresh Whole Chicken for Frying Bag | $262.66 | $262.51 | $-0.15 | -0.1% | Decrease |
| Pork Chop with Bone Frozen Tray | $85.69 | $85.57 | $-0.12 | -0.1% | Decrease |
| Frozen Boneless Skinless Chicken Breast Tray | $149.86 | $150.94 | $+1.08 | +0.7% | Increase |
| Whole Rack Frozen Baby Back Ribs Vacuum Packaged | $155.34 | $155.72 | $+0.38 | +0.2% | Increase |
| Frozen Bone-In Pork Spare Rib Vacuum Packaged | $150.58 | $150.20 | $-0.38 | -0.3% | Decrease |
| Fresh Chicken Breast Bone In Tray | $94.37 | $94.27 | $-0.10 | -0.1% | Decrease |
| Fresh Chicken Leg Quarters Tray | $92.21 | $92.01 | $-0.20 | -0.2% | Decrease |
| Frozen Whole Boneless Pork Tenderloin Vacuum Packaged | $75.84 | $75.72 | $-0.12 | -0.2% | Decrease |
| Frozen Lamb Shoulder Chops Tray | $120.46 | $120.29 | $-0.17 | -0.1% | Decrease |

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
| Food with Purpose Rice and 7 Ancient Grains 1.1 kg / 2.4 lb | Food with Purpose | $59.70 | 2025-11-04 |
| Tropicland Blueberries 1.36 kg / 48 oz | Tropicland | $87.95 | 2025-11-03 |
| Kellogg's Family Favorites Mix Pack 40 Units | Kellogg's | $97.70 | 2025-11-03 |
| Fresh Cantaloupe Melon |  | $39.95 | 2025-11-03 |
| Select Harvest Sweet and Smoked Barbecue Flavor Roasted Almonds 680 g / 1.5 lb | Select Harvest | $79.95 | 2025-10-30 |
| Blueberries 170 g / 6 oz |  | $42.95 | 2025-10-30 |
| Toblerone Christmas Chocolate Bar 360 g | Toblerone | $81.95 | 2025-10-28 |
| Leclerc Summer Cookies with Raspberry and Berry Flavor 2 Units / 300 g | Leclerc | $19.70 | 2025-10-28 |
| Nesquik Chocolate Drink 12 Units / 200 mL | Nesquik | $69.95 | 2025-10-28 |
| Señor Rico Three Milks Flan 12 Units / 113 g / 4 oz | Señor Rico | $148.95 | 2025-10-27 |

## New Products Added Today
No new products added today.
