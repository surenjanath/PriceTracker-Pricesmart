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
- **Total products scraped**: 1147
- **Total value**: $126,497.29
- **Average price**: $110.29

## Database Changes
- **New products added**: 0
- **Existing products updated**: 1147
- **Price changes detected**: 54
- **Stock/availability changes**: 30
- **Discontinued products**: 3

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 179 |
|  | 137 |
| Badia | 19 |
| Swiss | 15 |
| Nestle | 11 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Refined Avocado Oil 1 L / 33.8 oz | Member's Selection | $169.95 | true |
| Member's Selection Shredded Mozzarella Cheese 453 g / 1 lb | Member's Selection | $27.95 | true |
| Member's Selection Freshly Baked Vanilla Loaf Cake | Member's Selection | $37.95 | true |
| Mrs Thinster Toasted Coconut Cookies 454 g | Mrs. Thinster's | $89.95 | true |
| Cheez-It Original, Grahams, and White Cheddar Cheez-It Gripz Variety Pack 12 Units / 25 g / 0.9 oz | CheezIt | $66.95 | true |
| Sunny Fruits Dried Organics Figs 10 Units / 50 g / 1.76 oz | Sunny Fruits | $79.95 | true |
| Califia Farms Lime and Coconut Lemonade 1.4 L / 48 oz | Califia Farms | $54.95 | true |
| Swiss Honey Mustard Sauce 2 Units / 454 g | Swiss | $42.95 | true |
| Eggo Thick & Fluffy Waffles Original & Blueberry 2 Units / 330 g / 11.6 oz | Eggo | $106.95 | true |
| Aqua Star Breaded Shrimp 1.36 kg / 3 lb | Aqua Star | $192.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1042
- **Price increases**: 478
- **Price decreases**: 532
- **Average increase**: 10.5%
- **Average decrease**: -5.6%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Member's Selection Sliced Almonds 907 g / 2 lb | $117.95 | $132.95 | $+15.00 | +12.7% | Increase |
| Frozen Bone-In Goat Carcass Case | $1290.78 | $1129.32 | $-161.46 | -12.5% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $192.48 | $192.77 | $+0.29 | +0.2% | Increase |
| Fresh Beef Striploin Steak Tray | $187.56 | $184.41 | $-3.15 | -1.7% | Decrease |
| Swiss Twists 6 Units / 300 g | $28.95 | $27.95 | $-1.00 | -3.5% | Decrease |
| Swiss Elbows 6 Units / 300 g / 10.6 oz | $28.95 | $26.95 | $-2.00 | -6.9% | Decrease |
| Papaya | $31.74 | $31.52 | $-0.22 | -0.7% | Decrease |
| Bluewater Farms Cranberry Juice 1.65 L / 56 oz | $59.95 | $50.29 | $-9.66 | -16.1% | Decrease |
| Frozen Bone In Pork Shoulder Sliced Tray | $78.87 | $78.77 | $-0.10 | -0.1% | Decrease |
| Fresh Chicken Breast Bone In Tray | $93.79 | $93.69 | $-0.10 | -0.1% | Decrease |
| Erin Farm Chicken Salami 1 kg / 2.2 lb | $46.95 | $45.95 | $-1.00 | -2.1% | Decrease |
| Fratelli Beretta Italian Style Platter 340 g / 12 oz  | $84.95 | $89.95 | $+5.00 | +5.9% | Increase |
| Philadelphia Cream Cheese 2 Units / 453 g / 16 oz | $112.95 | $89.66 | $-23.29 | -20.6% | Decrease |
| Fresh Ground Chicken Tray | $99.39 | $99.27 | $-0.12 | -0.1% | Decrease |
| Swiss Spaghetti 6 Units / 400 g | $33.95 | $30.95 | $-3.00 | -8.8% | Decrease |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $104.95 | $1999.00 | +1804.7% |
| Fresh Beef Ribeye Steak Vacuum Packed | $246.08 | $2434.41 | +889.3% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $9.70 | $69.95 | +621.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $9.70 | $57.95 | +497.4% |
| Pillsbury Cookie Dough Mix 1.3 kg / 3 lb | $19.70 | $109.95 | +458.1% |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $14.70 | $57.95 | +294.2% |
| Carrot 2.27 kg / 5 lb | $9.70 | $37.95 | +291.2% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Hunt's Diced Tomatoes 8 Units / 411 g / 14.25 oz | $1999.00 | $104.95 | -94.7% |
| Member's Selection Premium Carved Cooked Ham with Natural Juices 2 Units / 340 g / 12 oz  | $69.95 | $9.70 | -86.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $9.70 | -83.3% |
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Snack Cheese 18 Units / 28 g / 1 oz | $89.95 | $19.70 | -78.1% |
| Belgioioso Fresh Mozzarella Cheese Pearls 2 Units / 225 g / 8 oz | $57.95 | $14.70 | -74.6% |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | $52.70 | $13.77 | -73.9% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Member's Selection Pumpkin and Spice Swiss Roll Freshly Baked | Member's Selection | $35.95 | 2026-04-08 |
| Whole Striploin Fresh Vacuum Packed |  | $1217.70 | 2026-04-08 |
| Member's Selection Chilled New York Strip Steak Tray | Member's Selection | $168.78 | 2026-04-08 |
| Bombolo Biscotti Decorated Cookies with Autumn Patterns 18 Units | Bombolo Biscotti | $13.77 | 2026-04-07 |
| Member's Selection Freshly Baked Sweet and Creamy Vanilla Cake 80 to 100 Slices | Member's Selection | $399.95 | 2026-04-07 |
| Member's Selection Freshly Baked Vanilla Madeleine-Style Cake | Member's Selection | $37.95 | 2026-04-07 |
| Kirkland Signature Clusters Chocolate Coated Cookies with Caramel and Marshmallow Filling 748 g / 26.3 oz | Kirkland Signature | $139.95 | 2026-04-05 |
| Popsalot Gourmet Caramel Popcorn with Almonds 283 g / 10 oz | Popsalot Gourmet | $84.95 | 2026-04-01 |
| Jayone Yizu Citrus Flavored Sweet Crispy Rice Rolls 2 Units / 80 g | Jayone | $39.95 | 2026-04-01 |
| Seedless Red Grapes |  | $97.01 | 2026-04-01 |

## New Products Added Today
No new products added today.
