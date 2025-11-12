-- Quick script to check what triggers exist on pricesmart_products table
-- Run this in Supabase SQL Editor to see what's causing the issue

-- Check all triggers on pricesmart_products
SELECT 
    trigger_name,
    event_manipulation,
    event_object_table,
    action_statement,
    action_timing
FROM information_schema.triggers
WHERE event_object_table = 'pricesmart_products';

-- Check all functions that might be related
SELECT 
    proname as function_name,
    pg_get_functiondef(oid) as function_definition
FROM pg_proc
WHERE prosrc LIKE '%analytics%' 
   OR prosrc LIKE '%avg_price%'
   OR prosrc LIKE '%pricesmart_products%';

