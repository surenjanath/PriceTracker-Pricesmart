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
- **Total value**: $129,526.50
- **Average price**: $112.05

## Database Changes
- **New products added**: 2
- **Existing products updated**: 1154
- **Price changes detected**: 79
- **Stock/availability changes**: 16
- **Discontinued products**: 4

## Top 5 Brands

| Brand | Count |
|-------|-------|
| Member's Selection | 186 |
|  | 147 |
| Badia | 18 |
| Swiss | 14 |
| Kirkland Signature | 12 |

## Recent Products

| Title | Brand | Price (TTD) | Availability |
|-------|-------|-------------|--------------|
| Food With Purpose Sparkling Tea Infused with Fruit Juice - Sugar Free 12 Units / 250 mL / 8.5 oz | Food with Purpose | $119.95 | true |
| Crazy Monkey Baking Granola Snacks with Dark Chocolate 680 g / 1.5 lb | Crazy Monkey Baking | $119.95 | true |
| Jackson's Sweet Potato Chips 454 g / 16 oz | Jackson's | $82.95 | true |
| Mariani Dried Red Fruit Mix with Cherries, Blueberries, and Strawberries 567 g / 20 oz | Mariani | $90.95 | true |
| Helado Mexico Ice Cream Bars 24 Units / 81 mL / 2.74 oz | Helado México | $171.95 | true |
| Daisy Cottage Cheese 454 g / 16 oz  | Daisy | $56.95 | true |
| Marie Callender's Italian Meat Lasagna 879 g / 1.94 lb | Marie Callender's | $83.95 | true |
| Nescafé Gold Instant Coffee 190 g | Nescafé | $104.95 | true |
| Pepe's Nature´s Pride Pack of Peas and Dry Legumes 5 Units / 1 kg | Pepe's Nature's Pride | $129.95 | true |
| Chuckanut Bay Chocalate Covered Cheesecake Bites 634 g / 1.4 lb | Chuckanut Bay | $139.95 | true |

# PriceSmart Price Analysis Report

## Price Change Summary (Last 30 Days)
- **Total price changes**: 1331
- **Price increases**: 744
- **Price decreases**: 521
- **Average increase**: 5.9%
- **Average decrease**: -5.9%

## Recent Price Changes

| Product | Old Price | New Price | Change | % Change | Type |
|---------|-----------|-----------|--------|----------|------|
| Papaya | $31.77 | $32.41 | $+0.64 | +2.0% | Increase |
| Fine Choice Fresh Marinated Chicken Tray | $93.77 | $93.68 | $-0.09 | -0.1% | Decrease |
| Coke Sprite Schweppes  Assorted Sodas 24 Units / 237 mL / 8.34 oz | $74.95 | $88.95 | $+14.00 | +18.7% | Increase |
| Rockit Apple 1.36 kg / 3 lb | $69.95 | $77.95 | $+8.00 | +11.4% | Increase |
| McCain Super Potato Wedges 2 kg / 4.4 lb | $65.95 | $77.95 | $+12.00 | +18.2% | Increase |
| Aqua Star Breaded Shrimp 680 g / 1.5 lb | $0.00 | $92.95 | $+92.95 | +100.0% | New |
| Cherries | $78.38 | $75.18 | $-3.20 | -4.1% | Decrease |
| Chilled Boneless Beef Eye of Round Steak Tray Pack | $204.70 | $205.65 | $+0.95 | +0.5% | Increase |
| Chilled Chicken Gizzard Tray Pack | $57.05 | $56.98 | $-0.07 | -0.1% | Decrease |
| Papaya | $0.00 | $32.63 | $+32.63 | +100.0% | New |
| Tostitos Scoops 411 g | $49.95 | $41.95 | $-8.00 | -16.0% | Decrease |
| Frozen Imported Pork Leg Slices | $81.68 | $83.08 | $+1.40 | +1.7% | Increase |
| Apple Jacks Cereal de Manzana y Canela 1.03 kg / 36.5 oz | $79.45 | $98.95 | $+19.50 | +24.5% | Increase |
| Caphe Fia Gourmet Garlic and Parmesan Cheese Bread 12 Units | $37.95 | $30.95 | $-7.00 | -18.4% | Decrease |
| Swiss Crunchy Peanut Butter 1.3 kg | $35.95 | $42.95 | $+7.00 | +19.5% | Increase |

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
| Minute Maid Assorted 24 Units / 250 mL / 8.5 oz | Minute Maid | $82.95 | 2025-11-30 |
| Stamina Energy Carbonated Energy Drink 12 Units / 330 mL / 11.16 oz | Stamina Energy | $55.95 | 2025-11-30 |
| Kraft Macaroni & Cheese Deluxe 3 Units 397 g  / 14 oz | Kraft | $49.70 | 2025-11-30 |
| S&W Thick and Rich Tomato Paste 3.15 kg / 6.9 lb | S&W | $97.95 | 2025-11-30 |
| French Fries 2.5 kg / 5.5 lb |  | $49.95 | 2025-11-29 |
| Member's Selection Freshly Baked Oatmeal Cookies 24 Units | Member's Selection | $60.95 | 2025-11-28 |
| Member's Selection Freshly Baked Chocolate Chip Cookies 24 Units | Member's Selection | $60.95 | 2025-11-28 |
| Stuffed Foods Lobster Ravioli 680 g / 24 oz | Stuffed Foods | $99.95 | 2025-11-27 |
| Califia Farms Toasted Coconut Almond Milk 1.4 L / 48 oz | Califia Farms | $54.95 | 2025-11-27 |
| Lucozade Carbonated Energy Drink 12 Units / 250 mL | Lucozade | $79.70 | 2025-11-26 |

## New Products Added Today

| Product | Brand | Price | Category |
|---------|-------|-------|----------|
| Aqua Star Breaded Shrimp 680 g / 1.5 lb | Aqua Star | $92.95 | G10D03 |
| Papaya |  | $32.63 | G10D03 |
