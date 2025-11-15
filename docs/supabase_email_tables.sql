-- Supabase Tables for Email Collection
-- Run this SQL in your Supabase SQL Editor to create the tables for beta testers and release notifications

-- Table for Beta Testers
CREATE TABLE IF NOT EXISTS beta_testers (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    name TEXT,
    signup_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    source TEXT DEFAULT 'website',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Table for Release Notifications
CREATE TABLE IF NOT EXISTS release_notifications (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    name TEXT,
    signup_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    source TEXT DEFAULT 'website',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable Row Level Security (RLS)
ALTER TABLE beta_testers ENABLE ROW LEVEL SECURITY;
ALTER TABLE release_notifications ENABLE ROW LEVEL SECURITY;

-- RLS Policy: Allow anyone to INSERT (for form submissions)
CREATE POLICY "Allow public inserts for beta_testers"
    ON beta_testers
    FOR INSERT
    TO anon, authenticated
    WITH CHECK (true);

CREATE POLICY "Allow public inserts for release_notifications"
    ON release_notifications
    FOR INSERT
    TO anon, authenticated
    WITH CHECK (true);

-- RLS Policy: Only authenticated users (you) can SELECT (view the data)
-- You can modify this to allow public reads if needed, but it's more secure to keep it private
CREATE POLICY "Allow authenticated selects for beta_testers"
    ON beta_testers
    FOR SELECT
    TO authenticated
    USING (true);

CREATE POLICY "Allow authenticated selects for release_notifications"
    ON release_notifications
    FOR SELECT
    TO authenticated
    USING (true);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_beta_testers_email ON beta_testers(email);
CREATE INDEX IF NOT EXISTS idx_beta_testers_signup_date ON beta_testers(signup_date);
CREATE INDEX IF NOT EXISTS idx_release_notifications_email ON release_notifications(email);
CREATE INDEX IF NOT EXISTS idx_release_notifications_signup_date ON release_notifications(signup_date);

-- Optional: Add comments to tables
COMMENT ON TABLE beta_testers IS 'Stores email addresses of users who signed up for beta testing';
COMMENT ON TABLE release_notifications IS 'Stores email addresses of users who want to be notified when the app launches';

