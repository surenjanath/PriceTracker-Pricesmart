# PriceSmart Mobile App API Documentation

## Overview
This documentation describes how to access PriceSmart product data and analytics from Supabase in your mobile app.

## Base Configuration

### Supabase Endpoint
```
https://your-project-id.supabase.co
```
**Note**: Replace with your actual Supabase project URL from the dashboard.

### Authentication
Use your Supabase **anon key** (public key) for client-side requests. The service role key should only be used server-side.

---

## Tables Available

### 1. `pricesmart_products`
Contains all product information.

### 2. `price_history`
Contains historical price changes for products.

### 3. `analytics`
Contains daily analytics snapshots matching the README structure.

---

## API Endpoints & Queries

### 1. Get Latest Analytics (Main Dashboard)

**Use Case**: Display main analytics dashboard matching README data.

**Query**:
```javascript
// JavaScript/TypeScript (Supabase JS Client)
const { data, error } = await supabase
  .from('analytics')
  .select('*')
  .order('snapshot_date', { ascending: false })
  .limit(1)
  .single();
```

**Response Structure**:
```json
{
  "id": 1,
  "snapshot_date": "2025-11-12",
  "total_products": 1345,
  "total_value": "129165.51",
  "average_price": "112.42",
  "active_products": 1149,
  "discontinued_products": 196,
  "new_products_added": 1,
  "existing_products_updated": 1344,
  "price_changes_detected": 23,
  "stock_availability_changes": 0,
  "discontinued_products_count": 196,
  "total_price_changes_30d": 1370,
  "price_increases_30d": 776,
  "price_decreases_30d": 527,
  "average_increase_percentage": "4.9",
  "average_decrease_percentage": "-5.0",
  "new_products_today": 1,
  "top_brands_json": "[{\"brand\":\"Member's Selection\",\"count\":190},{\"brand\":\"\",\"count\":142}]",
  "last_updated": "2025-11-12T13:34:33.908764+00:00",
  "created_at": "2025-11-12T17:32:42.517856+00:00"
}
```

**Display Example**:
```javascript
// Parse and display
const analytics = data;
const topBrands = JSON.parse(analytics.top_brands_json);

console.log(`Total Products: ${analytics.total_products}`);
console.log(`Total Value: $${parseFloat(analytics.total_value).toLocaleString()}`);
console.log(`Average Price: $${parseFloat(analytics.average_price).toFixed(2)}`);
console.log(`Price Changes (30d): ${analytics.total_price_changes_30d}`);
console.log(`Top Brand: ${topBrands[0].brand} (${topBrands[0].count} products)`);
```

---

### 2. Get Historical Analytics Trends

**Use Case**: Display trend charts/graphs showing analytics over time.

**Query**:
```javascript
// Get last 30 days of analytics
const { data, error } = await supabase
  .from('analytics')
  .select('snapshot_date, total_products, active_products, total_price_changes_30d, price_increases_30d, price_decreases_30d')
  .order('snapshot_date', { ascending: false })
  .limit(30);
```

**Response**: Array of analytics records for trend visualization.

---

### 3. Get All Products

**Use Case**: Display product list/search.

**Query**:
```javascript
// Get all active products
const { data, error } = await supabase
  .from('pricesmart_products')
  .select('*')
  .eq('is_active', 'true')
  .order('title', { ascending: true });
```

**Filter by Category**:
```javascript
const { data, error } = await supabase
  .from('pricesmart_products')
  .select('*')
  .eq('is_active', 'true')
  .eq('category', 'G10D03')
  .order('title', { ascending: true });
```

**Search by Title**:
```javascript
const { data, error } = await supabase
  .from('pricesmart_products')
  .select('*')
  .eq('is_active', 'true')
  .ilike('title', `%${searchTerm}%`)
  .order('title', { ascending: true });
```

---

### 4. Get Product Details

**Use Case**: Display individual product page.

**Query**:
```javascript
// Get product by PID
const { data, error } = await supabase
  .from('pricesmart_products')
  .select('*')
  .eq('pid', '485504')
  .single();
```

**Response**: Single product object with all fields.

---

### 5. Get Price History for a Product

**Use Case**: Display price change chart for a product.

**Query**:
```javascript
// Get price history for a product
const { data, error } = await supabase
  .from('price_history')
  .select('*')
  .eq('product_pid', '485504')
  .order('timestamp', { ascending: false })
  .limit(100);
```

**Response**: Array of price history records showing price changes over time.

---

### 6. Get Recent Price Changes

**Use Case**: Display "Recent Price Changes" section.

**Query**:
```javascript
// Get recent price changes (last 30 days)
const { data, error } = await supabase
  .from('price_history')
  .select(`
    *,
    pricesmart_products (
      title,
      brand,
      thumb_image
    )
  `)
  .gte('timestamp', new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString())
  .order('timestamp', { ascending: false })
  .limit(50);
```

**Response**: Price changes with product details joined.

---

### 7. Get Top Brands

**Use Case**: Display brand statistics.

**Query**:
```javascript
// Get latest analytics and parse top brands
const { data, error } = await supabase
  .from('analytics')
  .select('top_brands_json')
  .order('snapshot_date', { ascending: false })
  .limit(1)
  .single();

const topBrands = JSON.parse(data.top_brands_json);
// topBrands is an array: [{brand: "Name", count: 123}, ...]
```

---

### 8. Get Biggest Price Increases/Decreases

**Use Case**: Display "Biggest Price Changes" section.

**Query**:
```javascript
// Biggest increases (all time)
const { data, error } = await supabase
  .from('price_history')
  .select(`
    *,
    pricesmart_products (
      title,
      brand
    )
  `)
  .eq('change_type', 'increase')
  .order('price_change_percentage', { ascending: false })
  .limit(10);

// Biggest decreases (all time)
const { data, error } = await supabase
  .from('price_history')
  .select(`
    *,
    pricesmart_products (
      title,
      brand
    )
  `)
  .eq('change_type', 'decrease')
  .order('price_change_percentage', { ascending: true })
  .limit(10);
```

---

### 9. Get New Products Today

**Use Case**: Display "New Products" section.

**Query**:
```javascript
const today = new Date().toISOString().split('T')[0];
const { data, error } = await supabase
  .from('pricesmart_products')
  .select('*')
  .gte('date_created', today)
  .eq('is_active', 'true')
  .order('date_created', { ascending: false });
```

---

### 10. Get Discontinued Products

**Use Case**: Display "Recently Discontinued" section.

**Query**:
```javascript
const { data, error } = await supabase
  .from('pricesmart_products')
  .select('*')
  .eq('is_active', 'false')
  .order('last_updated', { ascending: false })
  .limit(20);
```

---

## Mobile App Setup

### React Native / Expo

**Install Supabase Client**:
```bash
npm install @supabase/supabase-js
```

**Initialize Client**:
```javascript
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.EXPO_PUBLIC_SUPABASE_URL;
const supabaseAnonKey = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY;

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
```

**Environment Variables** (`.env`):
```
EXPO_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
EXPO_PUBLIC_SUPABASE_ANON_KEY=your_anon_key_here
```

### Flutter / Dart

**Install Supabase Client**:
```yaml
# pubspec.yaml
dependencies:
  supabase_flutter: ^2.0.0
```

**Initialize Client**:
```dart
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

// Load environment variables from .env file
await dotenv.load(fileName: ".env");

await Supabase.initialize(
  url: dotenv.env['SUPABASE_URL']!,
  anonKey: dotenv.env['SUPABASE_ANON_KEY']!,
);

final supabase = Supabase.instance.client;
```

**Environment Variables** (`.env`):
```
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your_anon_key_here
```

**Note**: Install `flutter_dotenv` package and add `.env` to `.gitignore`

### Swift / iOS (Native)

**Install via Swift Package Manager**:
- Add: `https://github.com/supabase/supabase-swift`

**Initialize Client**:
```swift
import Supabase

// Load from environment variables or Info.plist
let supabaseURL = Bundle.main.object(forInfoDictionaryKey: "SUPABASE_URL") as! String
let supabaseKey = Bundle.main.object(forInfoDictionaryKey: "SUPABASE_ANON_KEY") as! String

let supabase = SupabaseClient(
  supabaseURL: URL(string: supabaseURL)!,
  supabaseKey: supabaseKey
)
```

**Configuration** (`Info.plist` or environment variables):
```xml
<key>SUPABASE_URL</key>
<string>https://your-project-id.supabase.co</string>
<key>SUPABASE_ANON_KEY</key>
<string>your_anon_key_here</string>
```

**Note**: Never hardcode keys in Swift files. Use Info.plist or environment variables.

### Kotlin / Android (Native)

**Add to `build.gradle.kts`**:
```kotlin
dependencies {
    implementation("io.github.jan-tennert.supabase:postgrest-kt:2.0.0")
    implementation("io.ktor:ktor-client-android:2.3.0")
}
```

**Initialize Client**:
```kotlin
import io.github.jan.supabase.SupabaseClient
import io.github.jan.supabase.createSupabaseClient
import io.github.jan.supabase.postgrest.Postgrest

// Load from BuildConfig or local.properties
val supabaseUrl = BuildConfig.SUPABASE_URL
val supabaseKey = BuildConfig.SUPABASE_ANON_KEY

val supabase = createSupabaseClient(
    supabaseUrl = supabaseUrl,
    supabaseKey = supabaseKey
) {
    install(Postgrest)
}
```

**Configuration** (`local.properties` - add to `.gitignore`):
```properties
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your_anon_key_here
```

**Note**: Never hardcode keys in Kotlin files. Use BuildConfig or local.properties.

---

## Example: Complete Dashboard Component

### React Native Example

```javascript
import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { createClient } from '@supabase/supabase-js';

// Initialize Supabase client using environment variables
const supabase = createClient(
  process.env.EXPO_PUBLIC_SUPABASE_URL,
  process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
);

export default function Dashboard() {
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAnalytics();
  }, []);

  const fetchAnalytics = async () => {
    try {
      const { data, error } = await supabase
        .from('analytics')
        .select('*')
        .order('snapshot_date', { ascending: false })
        .limit(1)
        .single();

      if (error) throw error;
      
      setAnalytics(data);
    } catch (error) {
      console.error('Error fetching analytics:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <Text>Loading...</Text>;
  if (!analytics) return <Text>No data</Text>;

  const topBrands = JSON.parse(analytics.top_brands_json);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>PriceSmart Analytics</Text>
      
      <View style={styles.section}>
        <Text style={styles.label}>Total Products</Text>
        <Text style={styles.value}>{analytics.total_products}</Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.label}>Total Value</Text>
        <Text style={styles.value}>
          ${parseFloat(analytics.total_value).toLocaleString()}
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.label}>Average Price</Text>
        <Text style={styles.value}>
          ${parseFloat(analytics.average_price).toFixed(2)}
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.label}>Price Changes (30d)</Text>
        <Text style={styles.value}>{analytics.total_price_changes_30d}</Text>
        <Text style={styles.subtext}>
          ↑ {analytics.price_increases_30d} | ↓ {analytics.price_decreases_30d}
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.label}>Top Brands</Text>
        {topBrands.slice(0, 5).map((brand, index) => (
          <Text key={index} style={styles.brand}>
            {index + 1}. {brand.brand || '(No brand)'}: {brand.count} products
          </Text>
        ))}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  section: { marginBottom: 15 },
  label: { fontSize: 14, color: '#666' },
  value: { fontSize: 20, fontWeight: 'bold' },
  subtext: { fontSize: 12, color: '#999' },
  brand: { fontSize: 14, marginTop: 5 },
});
```

---

## Data Types Reference

### Analytics Fields
- `total_products`: INTEGER - Total number of products
- `total_value`: TEXT (string) - Total inventory value (parse as float)
- `average_price`: TEXT (string) - Average product price (parse as float)
- `active_products`: INTEGER - Currently active products
- `discontinued_products`: INTEGER - Discontinued products count
- `total_price_changes_30d`: INTEGER - Price changes in last 30 days
- `price_increases_30d`: INTEGER - Number of price increases
- `price_decreases_30d`: INTEGER - Number of price decreases
- `average_increase_percentage`: TEXT (string) - Average % increase (parse as float)
- `average_decrease_percentage`: TEXT (string) - Average % decrease (parse as float)
- `top_brands_json`: TEXT (JSON string) - Top 5 brands array (parse as JSON)

### Product Fields
- `pid`: String - Product ID (unique)
- `title`: String - Product title
- `price_TT`: Float/String - Price in TTD
- `brand`: String - Brand name
- `category`: String - Category code
- `thumb_image`: String - Image URL
- `is_active`: String - 'true' or 'false'
- `availability_TT`: String - Availability status
- `inventory_TT`: String - Inventory status

---

## Error Handling

Always handle errors in your queries:

```javascript
const { data, error } = await supabase
  .from('analytics')
  .select('*')
  .limit(1)
  .single();

if (error) {
  console.error('Supabase error:', error);
  // Handle error (show message to user, retry, etc.)
  return;
}

// Use data safely
console.log('Analytics:', data);
```

---

## Rate Limits & Best Practices

1. **Cache Results**: Analytics data updates daily, cache for 1 hour
2. **Pagination**: Use `.limit()` for large datasets
3. **Selective Fields**: Only select fields you need (`.select('field1, field2')`)
4. **Error Handling**: Always check for errors
5. **Loading States**: Show loading indicators during queries
6. **Offline Support**: Consider caching for offline access

---

## Security Notes

- ✅ Use **anon key** (public key) for client-side requests
- ❌ **Never** expose service role key in mobile app
- ✅ Supabase Row Level Security (RLS) is enabled
- ✅ Analytics table is read-only for authenticated users
- ✅ Products table is readable by all (public access)

---

## Support & Updates

- Analytics data updates daily via automated sync
- Product data updates multiple times per day
- Price history accumulates over time
- Check `last_updated` field to see when data was last refreshed

---

## Quick Reference Card

| Use Case | Table | Query |
|----------|-------|-------|
| Dashboard Stats | `analytics` | Latest record |
| Product List | `pricesmart_products` | Filter `is_active='true'` |
| Product Details | `pricesmart_products` | Filter by `pid` |
| Price History | `price_history` | Filter by `product_pid` |
| Recent Changes | `price_history` | Last 30 days |
| Top Brands | `analytics` | Parse `top_brands_json` |
| Trends | `analytics` | Last 30 records |

---

**Last Updated**: 2025-11-12  
**API Version**: 1.0

