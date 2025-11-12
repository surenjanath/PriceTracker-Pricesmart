# PriceSmart API - Quick Start Guide

## 📱 For Mobile App Developers

This guide shows you how to integrate PriceSmart data into your mobile app.

## Quick Links

- **[API_DOCUMENTATION.md](./API_DOCUMENTATION.md)** - Complete API reference with examples
- **[SETUP_ENVIRONMENT.md](./SETUP_ENVIRONMENT.md)** - Environment setup guide
- **[ANALYTICS_DATABASE_MAPPING.md](./ANALYTICS_DATABASE_MAPPING.md)** - Analytics data structure

## 🚀 Quick Start

### 1. Get Your API Key

1. Go to [Supabase Dashboard](https://app.supabase.com)
2. Select your project
3. Go to **Settings** → **API**
4. Copy the **anon/public key** (NOT the service_role key!)

### 2. Initialize Supabase Client

**React Native / Expo:**
```bash
npm install @supabase/supabase-js
```

```javascript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.EXPO_PUBLIC_SUPABASE_URL,
  process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
);
```

**Flutter:**
```yaml
dependencies:
  supabase_flutter: ^2.0.0
```

```dart
import 'package:supabase_flutter/supabase_flutter.dart';

import 'package:flutter_dotenv/flutter_dotenv.dart';

await dotenv.load(fileName: ".env");

await Supabase.initialize(
  url: dotenv.env['SUPABASE_URL']!,
  anonKey: dotenv.env['SUPABASE_ANON_KEY']!,
);
```

### 3. Get Analytics Data (Dashboard)

```javascript
// Get latest analytics (matches README)
const { data, error } = await supabase
  .from('analytics')
  .select('*')
  .order('snapshot_date', { ascending: false })
  .limit(1)
  .single();

// Parse top brands
const topBrands = JSON.parse(data.top_brands_json);

// Display
console.log(`Total Products: ${data.total_products}`);
console.log(`Total Value: $${parseFloat(data.total_value).toLocaleString()}`);
console.log(`Average Price: $${parseFloat(data.average_price).toFixed(2)}`);
```

### 4. Get Products List

```javascript
// Get all active products
const { data, error } = await supabase
  .from('pricesmart_products')
  .select('*')
  .eq('is_active', 'true')
  .order('title', { ascending: true });
```

### 5. Search Products

```javascript
// Search by title
const { data, error } = await supabase
  .from('pricesmart_products')
  .select('*')
  .eq('is_active', 'true')
  .ilike('title', `%${searchTerm}%`);
```

## 📊 Available Data

### Analytics Table
- Total products, value, average price
- Price changes (30 days)
- Top brands
- Product statistics

### Products Table
- Product details (title, price, brand, category)
- Images, availability, inventory
- Active/discontinued status

### Price History Table
- Historical price changes
- Price increase/decrease tracking
- Change percentages

## 🔐 Security

- ✅ Use **anon key** (public key) for mobile apps
- ❌ **Never** use service_role key in mobile apps
- ✅ All data is read-only for public access
- ✅ Row Level Security (RLS) is enabled

## 📚 Full Documentation

See **[API_DOCUMENTATION.md](./API_DOCUMENTATION.md)** for:
- Complete API reference
- All available queries
- Code examples for React Native, Flutter, iOS, Android
- Error handling
- Best practices

## 🆘 Support

- Check `API_DOCUMENTATION.md` for detailed examples
- Check `SETUP_ENVIRONMENT.md` for setup issues
- Analytics data updates daily automatically

---

**Last Updated**: 2025-11-12

