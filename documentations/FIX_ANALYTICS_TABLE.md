# Fix Analytics Table Issue

## Problem
Error: `column "avg_price" of relation "analytics" does not exist`

This error occurs because:
1. The analytics table might have an old schema with different column names
2. There might be database triggers or views referencing the old column names

## Solution

Run the updated `create_analytics_table.sql` script in Supabase SQL Editor. The script now:
1. Drops any triggers/functions/views that reference analytics
2. Drops and recreates the analytics table with correct schema
3. Uses `snapshot_date` instead of `date` (avoids reserved word conflict)
4. Uses `average_price` (not `avg_price`)

## Steps

1. Go to Supabase Dashboard → SQL Editor
2. Copy the entire contents of `create_analytics_table.sql`
3. Paste and execute it
4. Run the sync script again: `python supabase_sync.py`

## Column Name Changes

- ❌ Old: `date` → ✅ New: `snapshot_date`
- ❌ Old: `avg_price` → ✅ New: `average_price`

The sync script has been updated to use the correct column names.

