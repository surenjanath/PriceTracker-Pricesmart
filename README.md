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
- **Total products scraped**: 1095
- **Total value**: $117,847.84
- **Average price**: $107.62

## Database Changes
- **New products added**: 7
- **Existing products updated**: 1088
- **Price changes detected**: 16
- **Stock/availability changes**: 10
- **Discontinued products**: 0

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 182 |
|  | 137 |
| Badia | 19 |
| Swiss | 13 |
| Kiss | 13 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Member's Selection Thai Jasmine Long Grain Rice 9.07 kg / 20 lb | Member's Selection | $149.95 | true |
| Nilo Soursop Juice 12 Units / 320 mL / 10.82 oz | Nilo | $129.95 | true |
| Loc Maria Biscuits Assorted French Cookies Butter and Salted Caramel 441 g / 15.6 oz | Loc Maria Biscuits | $156.95 | true |
| Karnis Hummus Mix 3 Units / 226 g / 7.97 oz | Karnis | $82.95 | true |
| Nesquick Liquid Milk Drink with Cocoa Flavor 12 Units / 250 mL | Nesquik | $77.95 | true |
| Kellogg’s Assorted Cereals Corn Pops, Froot Loops & Apple Jacks 3 Bags / 1.05 kg / 37.3 oz | Kellogg's | $106.95 | true |
| Dewlands Passion Fruit and Apple Juice 3 Units / 1 L | Dewlands | $59.95 | true |
| Badia Mojo Rub Citrus Blend 680.4 g / 24 oz  | Badia | $89.95 | true |
| Idahoan Classic Instant Mashed Potatoes 1.47 kg / 3.25 lb | Idahoan | $109.95 | true |
| Annie's Organic Macaroni and Cheese Variety Pack 12 Units / 170 g | Annies | $239.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1275
- **Price increases**: 660
- **Price decreases**: 551
- **Average increase**: 6.5%
- **Average decrease**: -3.9%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Libby´s Corned Beef 3 Units / 340 g | $0.00 | $109.95 | $+109.95 | +100.0% | New |
| Kellogg's Chocolatey Chip Waffles 2 Pack / 349 g / 12.3 oz | $0.00 | $97.95 | $+97.95 | +100.0% | New |
| Member's Selection Frozen Sliced Turkey Wings, Bag | $148.45 | $148.35 | $-0.10 | -0.1% | Decrease |
| Member's Selection Mayonnaise 12 Units / 591 mL / 20 oz | $0.00 | $334.95 | $+334.95 | +100.0% | New |
| Frozen Bone In Pork Shoulder Sliced Tray | $70.43 | $70.33 | $-0.10 | -0.1% | Decrease |
| Bartlett Pear 1.3 kg / 3 lb | $0.00 | $72.95 | $+72.95 | +100.0% | New |
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | $+70.25 | +356.6% | Increase |
| Edwards Signatures Pecan Pie 907g / 2 lb | $0.00 | $69.95 | $+69.95 | +100.0% | New |
| Pier 33 Coho Salmon Steak Frozen, Skin on 1 kg / 2.2 lb | $0.00 | $224.95 | $+224.95 | +100.0% | New |
| Frozen Sliced Turkey Drumsticks | $98.45 | $154.75 | $+56.30 | +57.2% | Increase |
| Fresh Chicken Mixed Parts Tray | $84.07 | $84.18 | $+0.11 | +0.1% | Increase |
| Fresh Chicken Wings Tray | $92.68 | $92.57 | $-0.11 | -0.1% | Decrease |
| Fresh Ground Chicken Meat Bag | $262.42 | $261.57 | $-0.85 | -0.3% | Decrease |
| Butterball Frozen Natural Ground Turkey Vacuum Packed 3 Units / 453 g / 16 oz | $119.95 | $122.95 | $+3.00 | +2.5% | Increase |
| Frozen Bone-In Pork Spare Rib Vacuum Packaged | $140.18 | $140.42 | $+0.24 | +0.2% | Increase |

## Biggest Price Increases (All Time)

| Product | Old Price | New Price | % Increase |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $19.70 | $89.95 | +356.6% |
| Frozen Boneless Pork Loin Vacuum Packaged | $56.90 | $253.53 | +345.6% |
| Sabra Classic Hummus 850 g / 30 oz | $24.70 | $79.95 | +223.7% |
| Avocado 2 Units | $9.70 | $29.95 | +208.8% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $29.70 | $89.95 | +202.9% |
| Nestos Capers in Brine 2 Units / 350 g / 12.4 oz | $29.70 | $64.95 | +118.7% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $59.70 | $129.95 | +117.7% |
| Purple Cabbage Unit | $14.70 | $29.95 | +103.7% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $39.70 | $79.95 | +101.4% |
| Frito Lay Assortment Box 24 Units | $49.70 | $99.95 | +101.1% |

## Biggest Price Decreases (All Time)

| Product | Old Price | New Price | % Decrease |
|---------|-----------|-----------|------------|
| Tropical Frying Cheese 907 g / 32 oz | $89.95 | $19.70 | -78.1% |
| Sabra Classic Hummus 850 g / 30 oz | $79.95 | $24.70 | -69.1% |
| Avocado 2 Units | $29.95 | $9.70 | -67.6% |
| Kozyshack Cinnamon Rice Pudding 1.36 kg / 3 lb | $87.95 | $29.70 | -66.2% |
| Curly's Baby Back Pork Ribs 680 g / 24 oz | $129.95 | $59.70 | -54.1% |
| Purple Cabbage Unit | $29.95 | $14.70 | -50.9% |
|  Eggplant 793 g / 1.75 lb | $59.95 | $29.70 | -50.5% |
| Activia Low Fat Yogurt 12 Units / 113 g / 4 oz | $79.95 | $39.70 | -50.3% |
| Frito Lay Assortment Box 24 Units | $99.95 | $49.70 | -50.3% |
| Angie's Boom Chicka Pop Sweet and Salty Popcorn 652 g / 23 oz | $99.95 | $49.70 | -50.3% |

## Recently Discontinued Products

| Product | Brand | Last Known Price | Discontinued Date |
|---------|-------|------------------|-------------------|
| Hoody's Keto Matcha Trail Mix 907 g / 32 oz  | Hoody's | $114.70 | 2025-09-12 |
| Chobani Zero Sugar Yogurt 16 Units /  150 g / 5.3 oz | Chobani | $164.95 | 2025-09-11 |
| Ocean Delight Frozen Panko Breaded Squid Rings 680 g / 1.5 lb | Ocean Delight | $79.95 | 2025-09-11 |
| Uno Calzone Steak and Cheese 8 Units / 106 g / 3.7 oz | UNO | $134.95 | 2025-09-10 |
| Royal Asia Coconut Shrimp with Sweet Thai Chili Sauce 907 g / 2 lb | Royal Asia | $169.95 | 2025-09-08 |
| Tropicland Organic Sweet Potato Fries 1.8 kg / 4 lb | Tropicland | $114.95 | 2025-09-08 |
| Florida's Natural Orange Juice 2.63 L / 89 oz | Florida's Natural | $87.95 | 2025-09-05 |
| Kretcshmer Wheat Germ Honey 2 units / 311 g | Kretcshmer | $75.95 | 2025-09-04 |
| Sundays Assorted Ice Creams 16 Units / 90 mL / 3 oz | Sundays | $79.95 | 2025-09-04 |
| Ankara Shell Pasta 4 Units / 500 g | Ankara | $35.70 | 2025-09-04 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Libby´s Corned Beef 3 Units / 340 g | Libby's | $109.95 | G10D03 |
| Kellogg's Chocolatey Chip Waffles 2 Pack / 349 g / 12.3 oz | Kellogg's | $97.95 | G10D03 |
| Member's Selection Mayonnaise 12 Units / 591 mL / 20 oz | Member's Selection | $334.95 | G10D03 |
| Bartlett Pear 1.3 kg / 3 lb |  | $72.95 | G10D03 |
| Edwards Signatures Pecan Pie 907g / 2 lb | Edward's | $69.95 | G10D03 |
| Pier 33 Coho Salmon Steak Frozen, Skin on 1 kg / 2.2 lb | Pier 33 | $224.95 | G10D03 |
| Blue Ribbon Classic Vanilla Sandwich Ice Cream 16 Units / 99 g / 3.5 oz | Blue Ribbon | $59.95 | G10D03 |
