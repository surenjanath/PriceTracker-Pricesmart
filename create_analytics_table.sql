-- SQL script to create analytics table in Supabase
-- Run this in Supabase SQL Editor

-- Find and drop ALL triggers that might reference analytics
DO $$ 
DECLARE
    r RECORD;
BEGIN
    -- Drop ALL triggers on pricesmart_products table (they might reference analytics)
    FOR r IN (SELECT trigger_name, event_object_table 
              FROM information_schema.triggers 
              WHERE event_object_table = 'pricesmart_products') 
    LOOP
        EXECUTE 'DROP TRIGGER IF EXISTS ' || quote_ident(r.trigger_name) || ' ON ' || quote_ident(r.event_object_table) || ' CASCADE';
        RAISE NOTICE 'Dropped trigger: %', r.trigger_name;
    END LOOP;
    
    -- Drop all functions that might reference analytics or avg_price
    FOR r IN (SELECT proname::text, oid::regprocedure::text as full_name
              FROM pg_proc 
              WHERE proname LIKE '%analytics%' 
              OR proname LIKE '%update%'
              OR prosrc LIKE '%avg_price%'
              OR prosrc LIKE '%analytics%'
              OR prosrc LIKE '%pricesmart_products%') 
    LOOP
        BEGIN
            EXECUTE 'DROP FUNCTION IF EXISTS ' || r.full_name || ' CASCADE';
            RAISE NOTICE 'Dropped function: %', r.full_name;
        EXCEPTION WHEN OTHERS THEN
            RAISE NOTICE 'Could not drop function %: %', r.full_name, SQLERRM;
        END;
    END LOOP;
END $$;

-- Drop any views or materialized views
DROP VIEW IF EXISTS analytics_view CASCADE;
DROP MATERIALIZED VIEW IF EXISTS analytics_mv CASCADE;

-- Drop table if exists to recreate with correct schema
DROP TABLE IF EXISTS analytics CASCADE;

CREATE TABLE analytics (
    id BIGSERIAL PRIMARY KEY,
    snapshot_date DATE UNIQUE NOT NULL,
    
    -- Basic Analysis (matches README)
    total_products INTEGER DEFAULT 0,
    total_value TEXT, -- Stored as string to handle large numbers
    average_price TEXT, -- Stored as string to handle decimals
    
    -- Product Status
    active_products INTEGER DEFAULT 0,
    discontinued_products INTEGER DEFAULT 0,
    
    -- Database Changes (matches README)
    new_products_added INTEGER DEFAULT 0,
    existing_products_updated INTEGER DEFAULT 0,
    price_changes_detected INTEGER DEFAULT 0,
    stock_availability_changes INTEGER DEFAULT 0,
    discontinued_products_count INTEGER DEFAULT 0,
    
    -- Price Change Statistics (30 days - matches README)
    total_price_changes_30d INTEGER DEFAULT 0,
    price_increases_30d INTEGER DEFAULT 0,
    price_decreases_30d INTEGER DEFAULT 0,
    average_increase_percentage TEXT, -- Stored as string
    average_decrease_percentage TEXT, -- Stored as string
    
    -- Daily Stats
    new_products_today INTEGER DEFAULT 0,
    
    -- Top Brand (stored as JSON string for top 5 brands)
    top_brands_json TEXT, -- JSON array: [{"brand": "Name", "count": 123}, ...]
    
    last_updated TIMESTAMPTZ DEFAULT NOW(),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Create index on snapshot_date for faster lookups
CREATE INDEX IF NOT EXISTS idx_analytics_date ON analytics(snapshot_date);

-- Enable Row Level Security (RLS) - adjust policies as needed
ALTER TABLE analytics ENABLE ROW LEVEL SECURITY;

-- Create policy to allow service role to read/write (adjust as needed)
-- Note: Drop existing policies first if they exist
DROP POLICY IF EXISTS "Service role can manage analytics" ON analytics;
DROP POLICY IF EXISTS "Authenticated users can read analytics" ON analytics;

CREATE POLICY "Service role can manage analytics" ON analytics
    FOR ALL
    USING (auth.role() = 'service_role')
    WITH CHECK (auth.role() = 'service_role');

-- Create policy to allow authenticated users to read
CREATE POLICY "Authenticated users can read analytics" ON analytics
    FOR SELECT
    USING (auth.role() = 'authenticated');

