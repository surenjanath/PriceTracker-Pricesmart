# Analytics Database Mapping

## Overview
The Supabase `analytics` table stores the same analytics data that appears in the README, making it accessible via API queries instead of just markdown reports.

## README vs Database Mapping

### ✅ Basic Analysis (Exact Match)
| README | Database Column | Type |
|--------|----------------|------|
| Total products scraped | `total_products` | INTEGER |
| Total value | `total_value` | TEXT (string) |
| Average price | `average_price` | TEXT (string) |

### ✅ Database Changes (Matches README)
| README | Database Column | Type |
|--------|----------------|------|
| New products added | `new_products_added` | INTEGER |
| Existing products updated | `existing_products_updated` | INTEGER |
| Price changes detected | `price_changes_detected` | INTEGER |
| Stock/availability changes | `stock_availability_changes` | INTEGER |
| Discontinued products | `discontinued_products_count` | INTEGER |

### ✅ Price Change Summary (30 Days - Exact Match)
| README | Database Column | Type |
|--------|----------------|------|
| Total price changes | `total_price_changes_30d` | INTEGER |
| Price increases | `price_increases_30d` | INTEGER |
| Price decreases | `price_decreases_30d` | INTEGER |
| Average increase % | `average_increase_percentage` | TEXT (string) |
| Average decrease % | `average_decrease_percentage` | TEXT (string) |

### ✅ Top 5 Brands (Stored as JSON)
| README | Database Column | Type |
|--------|----------------|------|
| Top 5 Brands table | `top_brands_json` | TEXT (JSON array) |

**JSON Format:**
```json
[
  {"brand": "Member's Selection", "count": 190},
  {"brand": "", "count": 142},
  {"brand": "Badia", "count": 18},
  ...
]
```

### ✅ Additional Database Fields
- `snapshot_date` - Date of the analytics snapshot (DATE, UNIQUE)
- `active_products` - Count of active products (INTEGER)
- `discontinued_products` - Count of discontinued products (INTEGER)
- `new_products_today` - Products added today (INTEGER)
- `last_updated` - Last update timestamp (TIMESTAMPTZ)
- `created_at` - Creation timestamp (TIMESTAMPTZ)

## Query Examples

### Get Latest Analytics (Same as README)
```sql
SELECT 
    snapshot_date,
    total_products,
    total_value,
    average_price,
    new_products_added,
    existing_products_updated,
    price_changes_detected,
    total_price_changes_30d,
    price_increases_30d,
    price_decreases_30d,
    average_increase_percentage,
    average_decrease_percentage,
    top_brands_json
FROM analytics
ORDER BY snapshot_date DESC
LIMIT 1;
```

### Get Top Brands (Parse JSON)
```sql
SELECT 
    snapshot_date,
    jsonb_array_elements(top_brands_json::jsonb) as brand_data
FROM analytics
WHERE snapshot_date = CURRENT_DATE;
```

### Get Historical Analytics Trends
```sql
SELECT 
    snapshot_date,
    total_products,
    active_products,
    total_price_changes_30d,
    price_increases_30d,
    price_decreases_30d
FROM analytics
ORDER BY snapshot_date DESC
LIMIT 30; -- Last 30 days
```

## API Usage (Supabase Client)

```python
from supabase import create_client

supabase = create_client(url, key)

# Get latest analytics (matches README)
latest = supabase.table('analytics')\
    .select('*')\
    .order('snapshot_date', desc=True)\
    .limit(1)\
    .execute()

# Parse top brands
import json
top_brands = json.loads(latest.data[0]['top_brands_json'])
```

## Notes

1. **Daily Snapshots**: Each day gets one analytics record (unique by `snapshot_date`)
2. **String Values**: `total_value` and `average_price` are stored as strings to handle large numbers precisely
3. **Top Brands**: Stored as JSON for flexibility (can store more than 5 if needed)
4. **Stock Changes**: Currently set to 0 (would need separate tracking mechanism)
5. **Historical Data**: All analytics are preserved daily, allowing trend analysis over time

## What's NOT in Analytics Table (Available in Other Tables)

- **Recent Price Changes**: Query `price_history` table
- **Biggest Price Increases/Decreases**: Query `price_history` table with sorting
- **Recently Discontinued Products**: Query `pricesmart_products` where `is_active = 'false'`
- **New Products Added Today**: Query `pricesmart_products` where `date_created >= today`
- **Recent Products List**: Query `pricesmart_products` table

These can be queried directly from their respective tables when needed.

