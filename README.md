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
- **Total products scraped**: 1156
- **Total value**: $126,545.30
- **Average price**: $109.47

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1156
- **Price changes detected**: 71
- **Stock/availability changes**: 16
- **Discontinued products**: 4

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 176 |
|  | 141 |
| Swiss | 15 |
| Badia | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Crisp Ups Quesadillas Shredded Chicken & Cheese 925 g / 2 lb | Crisp Ups | $199.95 | true |
| Member’s Selection All-Natural Greek Nonfat Plain Yogurt 907 g / 2 lb  | Member's Selection | $49.95 | true |
| Athena Sweet Athena Ambassador's Cut Handmade Baklava Pastry 709 g / 25 oz | Athena Sweet Athena | $164.95 | true |
| Florida's Natural Peach and Mango Juice 2 Units / 1.75 L / 59 oz  | Florida's Natural | $119.95 | true |
| Member's Selection Extra Virgin Olive Oil 750 mL / 25.36 oz | Member's Selection | $69.95 | true |
| Karibbean Flavours Spicy Jerk Seasoning 2 Units / 283 g | Karibbean Flavours | $34.95 | true |
| SamTrade Chickpea Penne Pasta 2 Units / 227 g | Sam Trade | $69.95 | true |
| Vital Organics Green Organic Cold Press Green Juice 1 L | Vital Organics | $62.95 | true |
| Fresh Start Mauby Concentrate Made with Bark 4 Units / 750 mL / 25.36 oz | Fresh Start | $57.95 | true |
| Karibbean Flavours Whole Cloves 327 g | Karibbean Flavours | $79.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1070
- **Price increases**: 532
- **Price decreases**: 488
- **Average increase**: 8.7%
- **Average decrease**: -5.6%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Fresh Bone-in Chicken Thighs Tray | $69.73 | $70.48 | $+0.75 | +1.1% | Increase |
| Hershey's Cocoa Powder 652 g / 23 oz | $101.95 | $125.95 | $+24.00 | +23.5% | Increase |
| Bertie's Scorpion Pepper Sauce 750 mL / 25 oz | $86.95 | $72.95 | $-14.00 | -16.1% | Decrease |
| Frozen Imported Pork Leg Slices | $92.02 | $91.91 | $-0.11 | -0.1% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $189.49 | $188.93 | $-0.56 | -0.3% | Decrease |
| Papaya | $39.30 | $39.24 | $-0.06 | -0.2% | Decrease |
| Better Living Nuts, Seeds and Dehydrated Fruit Mix 1.3 kg | $87.95 | $74.45 | $-13.50 | -15.3% | Decrease |
| Member's Selection Frozen Bone-In Lamb Stew Bag | $97.47 | $97.32 | $-0.15 | -0.2% | Decrease |
| Pork Leg Frozen  | $63.64 | $63.54 | $-0.10 | -0.2% | Decrease |
| Frozen Lamb Leg Whole Boneless Tray Pack | $320.88 | $313.87 | $-7.01 | -2.2% | Decrease |
| Pascual Greek Yogurt 8 Units / 125 g / 4.4 oz | $59.95 | $50.95 | $-9.00 | -15.0% | Decrease |
| Member's Selection Frozen Skinless Boneless Beef Shoulder Clod Roast Tray Pack | $160.86 | $161.90 | $+1.04 | +0.6% | Increase |
| Member's Selection Frozen Bone-In Goat Stew Bag | $107.94 | $134.93 | $+26.99 | +25.0% | Increase |
| Member's Selection Frozen Boneless Pork Loin Roast Tray | $91.60 | $91.29 | $-0.31 | -0.3% | Decrease |
| Busta Assorted Soft Drinks 24 Units / 370 mL / 12.5 oz | $43.95 | $36.95 | $-7.00 | -15.9% | Decrease |

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
| Crix Steelpan Original Cookies in Collectible Tin 768 g | Crix | $42.70 | 2026-11-15 |
| Welch's Concord Grape Fruit Juice 1.75 L / 59 oz | Welch's | $24.70 | 2026-11-15 |
|  Gouda Cheese 20 kg / 44 lb |  | $1214.95 | 2026-11-15 |
| Member’s Selection Freshly Prepared Holiday Cake | Member's Selection | $89.95 | 2026-11-15 |
| Kit Kat Milk Chocolate Wafer 12 Units / 20.7 g | Kit Kat | $34.95 | 2026-11-14 |
| Philadelphia Strawberry Cream Cheese 2 Units / 212 g / 7.5 oz | Philadelphia | $49.70 | 2026-11-13 |
| Chobani Greek Yogurt 907 g / 32 oz | Chobani | $69.95 | 2026-11-13 |
| El Exquisito Sabor Traditional Tiramisu with Ladyfingers and Mascarpone | El Exquisito Sabor | $25.70 | 2026-11-13 |
| Member’s Selection All-Natural Greek Nonfat Plain Yogurt 907 g / 2 lb  | Member's Selection | $49.95 | 2026-11-13 |
| Member's Selection Frozen Bone-In Beef Feet Sliced, Tray | Member's Selection | $134.56 | 2026-11-12 |

## New Products Added Today
No new products added today.
