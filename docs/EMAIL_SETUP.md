# Email Collection Setup Guide

This guide will help you set up email collection for beta testers and release notifications on your launch page.

## Step 1: Create Supabase Tables

1. Go to your [Supabase Dashboard](https://app.supabase.com)
2. Select your project
3. Navigate to **SQL Editor**
4. Copy and paste the contents of `supabase_email_tables.sql`
5. Click **Run** to execute the SQL

This will create:
- `beta_testers` table - for beta testing signups
- `release_notifications` table - for release notification signups
- Row Level Security (RLS) policies to allow public inserts but restrict reads to authenticated users

## Step 2: Get Your Supabase Credentials

1. In Supabase Dashboard, go to **Settings** → **API**
2. Copy the following:
   - **Project URL** (e.g., `https://your-project-id.supabase.co`)
   - **anon public** key (this is safe to use in client-side code)

## Step 3: Configure the Launch Page

1. Open `index.html` in a text editor
2. Find these lines near the bottom of the file (in the `<script>` section):

```javascript
const SUPABASE_URL = 'YOUR_SUPABASE_URL_HERE';
const SUPABASE_ANON_KEY = 'YOUR_SUPABASE_ANON_KEY_HERE';
```

3. Replace the placeholders with your actual credentials:

```javascript
const SUPABASE_URL = 'https://your-project-id.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...';
```

## Step 4: Test the Forms

1. Open `index.html` in a web browser
2. Scroll down to the "Stay Updated" section
3. Try submitting both forms with test email addresses
4. Check your Supabase dashboard:
   - Go to **Table Editor**
   - You should see entries in `beta_testers` and `release_notifications` tables

## Security Notes

✅ **Safe to Expose:**
- The Supabase **anon key** is designed to be public and used in client-side code
- Row Level Security (RLS) policies protect your data
- Users can only INSERT (submit forms), not read or modify existing data

❌ **Never Expose:**
- The **service_role** key (this has full access and should only be used server-side)
- Database passwords
- Any other sensitive credentials

## Viewing Collected Emails

To view the collected emails:

1. Go to Supabase Dashboard → **Table Editor**
2. Select either `beta_testers` or `release_notifications` table
3. You'll see all submitted email addresses with signup dates

## Exporting Email Lists

You can export the email lists:

1. In Supabase Dashboard → **Table Editor**
2. Select the table you want to export
3. Click the **Export** button (usually in the top right)
4. Choose CSV or JSON format

## Troubleshooting

### Forms show "Email collection is not configured"
- Make sure you've replaced `YOUR_SUPABASE_URL_HERE` and `YOUR_SUPABASE_ANON_KEY_HERE` with actual values
- Check that there are no extra spaces or quotes around the values

### "Something went wrong" error
- Check browser console (F12) for detailed error messages
- Verify that the Supabase tables were created successfully
- Ensure RLS policies are set up correctly
- Check that your Supabase project is active and not paused

### Duplicate email error
- This is expected behavior - the forms prevent duplicate email addresses
- The user will see a friendly message that they're already signed up

### Can't see data in Supabase
- Make sure you're logged into Supabase Dashboard
- Check that RLS policies allow authenticated users to SELECT
- Verify the data was actually inserted (check the table directly)

## Next Steps

Once emails are being collected:

1. **Beta Testing:** When ready, export the `beta_testers` list and send beta invites
2. **Release:** When the app launches, export the `release_notifications` list and send launch announcements
3. **Email Service:** Consider integrating with an email service (SendGrid, Mailchimp, etc.) for automated emails

## Optional: Email Service Integration

For automated email sending, you can:

1. Create Supabase Edge Functions to send emails
2. Use a service like SendGrid, Mailchimp, or Resend
3. Set up webhooks to trigger emails when new signups occur

---

**Need Help?** Contact surenjanath.singh@gmail.com

