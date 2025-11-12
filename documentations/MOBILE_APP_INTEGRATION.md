# Mobile App Integration Guide

## Overview
This document explains how to integrate PriceSmart data into your mobile app. All the analytics and product data shown in the README is available via Supabase API.

## ✅ What's Available in Your App

### 1. Analytics Dashboard (Same as README)
- Total products, total value, average price
- Price changes (30 days)
- Top 5 brands
- Product statistics

### 2. Product Catalog
- All products with details
- Search and filter capabilities
- Product images and pricing

### 3. Price History
- Historical price changes
- Biggest increases/decreases
- Recent price changes

## 🚀 Setup Steps

### Step 1: Create `.env` File

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Supabase keys:
   ```env
   SUPABASE_URL=https://your-project-id.supabase.co
   SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
   SUPABASE_ANON_KEY=your_anon_key_here
   SUPABASE_DB_PASSWORD=your_password_here
   ```

3. Get your keys from Supabase Dashboard:
   - Go to **Settings** → **API**
   - Copy **service_role** key → `SUPABASE_SERVICE_ROLE_KEY`
   - Copy **anon/public** key → `SUPABASE_ANON_KEY`

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Test Connection

```bash
python test_analytics_query.py
```

If successful, you'll see analytics data displayed.

### Step 4: Integrate in Mobile App

See **[API_DOCUMENTATION.md](./API_DOCUMENTATION.md)** for:
- Complete code examples
- React Native, Flutter, iOS, Android setup
- All available queries
- Error handling

## 📱 Mobile App Quick Example

### React Native

```javascript
import { createClient } from '@supabase/supabase-js';

// Initialize (use anon key, NOT service_role!)
const supabase = createClient(
  process.env.EXPO_PUBLIC_SUPABASE_URL,
  process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
);

// Get analytics (dashboard)
const getAnalytics = async () => {
  const { data, error } = await supabase
    .from('analytics')
    .select('*')
    .order('snapshot_date', { ascending: false })
    .limit(1)
    .single();
  
  if (error) {
    console.error('Error:', error);
    return null;
  }
  
  return {
    totalProducts: data.total_products,
    totalValue: parseFloat(data.total_value),
    averagePrice: parseFloat(data.average_price),
    priceChanges: data.total_price_changes_30d,
    topBrands: JSON.parse(data.top_brands_json)
  };
};

// Get products
const getProducts = async () => {
  const { data, error } = await supabase
    .from('pricesmart_products')
    .select('*')
    .eq('is_active', 'true')
    .order('title');
  
  return data;
};
```

## 🔐 Security Checklist

- [x] `.env` file is in `.gitignore` (already done)
- [x] Using **anon key** in mobile app (not service_role)
- [x] Never commit `.env` to Git
- [x] Use environment variables in CI/CD

## 📊 Data Structure

### Analytics Table Fields
```
snapshot_date: DATE
total_products: INTEGER
total_value: TEXT (parse as float)
average_price: TEXT (parse as float)
active_products: INTEGER
total_price_changes_30d: INTEGER
price_increases_30d: INTEGER
price_decreases_30d: INTEGER
average_increase_percentage: TEXT (parse as float)
average_decrease_percentage: TEXT (parse as float)
top_brands_json: TEXT (parse as JSON array)
```

### Products Table Fields
```
pid: String (unique ID)
title: String
price_TT: Float
brand: String
category: String
thumb_image: String (URL)
is_active: String ('true' or 'false')
availability_TT: String
inventory_TT: String
```

## 🔄 Data Updates

- **Analytics**: Updates daily via automated sync
- **Products**: Updates multiple times per day
- **Price History**: Accumulates over time

Check `last_updated` field to see when data was refreshed.

## 📚 Documentation Files

1. **[API_DOCUMENTATION.md](./API_DOCUMENTATION.md)** - Complete API reference
2. **[SETUP_ENVIRONMENT.md](./SETUP_ENVIRONMENT.md)** - Environment setup
3. **[ANALYTICS_DATABASE_MAPPING.md](./ANALYTICS_DATABASE_MAPPING.md)** - Data mapping
4. **[README_API.md](./README_API.md)** - Quick start guide

## 🆘 Troubleshooting

### App can't connect to Supabase
- Verify you're using the **anon key** (not service_role)
- Check Supabase URL is correct
- Ensure internet connection

### No data returned
- Check Row Level Security (RLS) policies in Supabase
- Verify table names match exactly
- Check filters (e.g., `is_active='true'`)

### Analytics not updating
- Analytics updates daily via sync script
- Run `python supabase_sync.py` manually to sync
- Check `snapshot_date` to see last update

## ✅ Next Steps

1. ✅ Create `.env` file with your keys
2. ✅ Test connection with `test_analytics_query.py`
3. ✅ Read `API_DOCUMENTATION.md` for detailed examples
4. ✅ Integrate Supabase client in your mobile app
5. ✅ Use anon key (not service_role) in app

---

**Questions?** Check the documentation files or review the test script examples.

