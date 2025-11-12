# Supabase Sync Improvements

## Overview
Enhanced the sync script to ensure data integrity and add analytics capabilities.

## Key Improvements

### 1. Price History Product Linking ✅
- **Problem**: Price history records could reference products that don't exist in Supabase
- **Solution**: 
  - Before syncing price history, the script checks all referenced product PIDs
  - If a product is missing, it:
    1. First checks SQLite database for the product
    2. If found in SQLite, syncs it to Supabase
    3. If not found anywhere, creates a minimal product record with:
       - PID
       - Title: "Product {PID} (Historical)"
       - is_active: false (marked as inactive since full data isn't available)
       - Timestamps

### 2. Analytics Table Support ✅
- **New Feature**: Calculates and syncs analytics to Supabase
- **Analytics Calculated**:
  - Total products count
  - Active products count
  - Discontinued products count
  - Total inventory value
  - Average product price
  - Price changes (last 30 days)
  - Price increases/decreases count
  - Average increase/decrease percentages
  - New products added today

### 3. Database Password Configuration ✅
- Added `SUPABASE_DB_PASSWORD` configuration
- Password: `h4rLhy3iK9gTd1YI`
- Can be used for direct PostgreSQL connections if needed

## Setup Instructions

### Step 1: Create Analytics Table in Supabase
Run the SQL script `create_analytics_table.sql` in Supabase SQL Editor:
1. Go to Supabase Dashboard
2. Navigate to SQL Editor
3. Copy and paste the contents of `create_analytics_table.sql`
4. Execute the script

### Step 2: Run the Sync Script
```bash
python supabase_sync.py
```

The script now performs 3 steps:
1. **Sync Products**: Syncs all products from SQLite to Supabase
2. **Sync Price History**: 
   - Ensures all referenced products exist
   - Creates missing products automatically
   - Syncs all price history records
3. **Calculate & Sync Analytics**: Calculates statistics and updates analytics table

## Analytics Table Schema

The `analytics` table stores daily snapshots with:
- `date` (DATE, UNIQUE) - The date of the snapshot
- `total_products` (INTEGER) - Total number of products
- `active_products` (INTEGER) - Active products count
- `discontinued_products` (INTEGER) - Discontinued products count
- `total_value` (TEXT) - Total inventory value
- `average_price` (TEXT) - Average product price
- `total_price_changes_30d` (INTEGER) - Price changes in last 30 days
- `price_increases_30d` (INTEGER) - Price increases count
- `price_decreases_30d` (INTEGER) - Price decreases count
- `average_increase_percentage` (TEXT) - Average increase %
- `average_decrease_percentage` (TEXT) - Average decrease %
- `new_products_today` (INTEGER) - New products added today
- `last_updated` (TIMESTAMPTZ) - Last update timestamp
- `created_at` (TIMESTAMPTZ) - Creation timestamp

## Data Integrity Guarantees

✅ **All price history records are linked to products**
- Missing products are automatically created
- Products are checked in both SQLite and Supabase before creation

✅ **Consistent data structure**
- All products have the same keys (even if None)
- Prevents "All object keys must match" errors

✅ **Unicode support**
- Handles special characters in product titles
- Windows console encoding fixed

## Error Handling

- If analytics table doesn't exist, the script will:
  1. Try upsert first (if table exists)
  2. Fall back to insert (if table exists but no conflict)
  3. Log error if table doesn't exist (user needs to create it)

- If product creation fails, the script continues with other products
- Individual record failures don't stop batch processing

## Notes

- The analytics table uses `date` as a unique constraint, so each day gets one record
- Historical products are marked as `is_active: false` since we don't have full data
- All price values in analytics are stored as strings to handle large numbers and decimals precisely

