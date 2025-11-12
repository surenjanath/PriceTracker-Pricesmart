# Supabase Sync Script

This script (`supabase_sync.py`) reads data from the SQLite database (populated by the scraper) and syncs it to Supabase.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r supabase_sync_requirements.txt
   ```

2. Make sure the scraper has run first to populate the SQLite database:
   ```bash
   python pricesmart_scraper.py
   ```

3. Run the sync script:
   ```bash
   python supabase_sync.py
   ```

## How It Works

1. **Reads from SQLite**: The script connects to the SQLite database created by `pricesmart_scraper.py`
2. **Converts Data Format**: Converts column names from mixed case (e.g., `fractionDigits`, `price_TT`) to lowercase (e.g., `fractiondigits`, `price_tt`) to match Supabase schema
3. **Syncs to Supabase**: Uses Supabase REST API to upsert data into the `pricesmart_products` and `price_history` tables
4. **Batch Processing**: Processes data in batches of 100 records for efficiency

## Features

- **Upsert Logic**: Uses `on_conflict='pid'` to update existing products or insert new ones
- **Error Handling**: Continues processing even if individual records fail
- **Progress Reporting**: Shows progress and summary statistics
- **Data Type Conversion**: Handles conversion between SQLite and Supabase data types

## Configuration

The Supabase credentials are hardcoded in the script:
- `SUPABASE_URL`: https://roqczhmpqsyymzvfebmh.supabase.co
- `SUPABASE_SERVICE_ROLE_KEY`: (configured in script)

## Workflow

1. Run the scraper: `python pricesmart_scraper.py`
   - This populates the local SQLite database with scraped data
   - All analysis is performed by the scraper

2. Run the sync script: `python supabase_sync.py`
   - This reads from SQLite and pushes to Supabase
   - No modifications to the scraper are needed

## Notes

- The scraper remains unchanged and continues to work with SQLite
- The sync script is a separate utility that bridges SQLite and Supabase
- All analysis is done in the scraper; the sync script only transfers the results

