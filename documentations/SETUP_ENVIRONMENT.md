# Environment Setup Guide

## Overview
This project uses environment variables to securely store Supabase credentials. This prevents sensitive keys from being committed to GitHub.

## Quick Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `python-dotenv` - For loading `.env` file
- `supabase` - Supabase Python client
- `sqlalchemy` - Database ORM
- Other required packages

### 2. Create `.env` File

Copy the example file:
```bash
cp .env.example .env
```

### 3. Fill in Your Credentials

Edit `.env` and add your Supabase credentials:

```env
SUPABASE_URL=https://roqczhmpqsyymzvfebmh.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
SUPABASE_ANON_KEY=your_anon_key_here
SUPABASE_DB_PASSWORD=your_database_password_here
```

### 4. Get Your Supabase Keys

1. Go to [Supabase Dashboard](https://app.supabase.com)
2. Select your project
3. Go to **Settings** → **API**
4. Copy the following:
   - **Project URL** → `SUPABASE_URL`
   - **service_role** key → `SUPABASE_SERVICE_ROLE_KEY` (for sync script)
   - **anon** key → `SUPABASE_ANON_KEY` (for mobile app)
   - **Database Password** → `SUPABASE_DB_PASSWORD` (if you set one)

### 5. Verify Setup

Test the sync script:
```bash
python supabase_sync.py
```

If you see connection errors, check that:
- `.env` file exists in the project root
- All keys are filled in correctly
- No extra spaces or quotes around values

## Security Notes

✅ **DO:**
- Keep `.env` file local (it's in `.gitignore`)
- Use `.env.example` as a template (safe to commit)
- Use `SUPABASE_SERVICE_ROLE_KEY` only for server-side scripts
- Use `SUPABASE_ANON_KEY` for mobile app client-side

❌ **DON'T:**
- Commit `.env` to Git (already in `.gitignore`)
- Share your service role key publicly
- Hardcode keys in source code
- Use service role key in mobile app

## Mobile App Setup

For your mobile app, you'll need:

### React Native / Expo
```env
EXPO_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
EXPO_PUBLIC_SUPABASE_ANON_KEY=your_anon_key_here
```

### Flutter
```env
SUPABASE_URL=https://roqczhmpqsyymzvfebmh.supabase.co
SUPABASE_ANON_KEY=your_anon_key_here
```

**Important**: Only use the **anon key** (public key) in mobile apps, never the service role key!

## Troubleshooting

### Error: "SUPABASE_SERVICE_ROLE_KEY not found"
- Make sure `.env` file exists in project root
- Check that `SUPABASE_SERVICE_ROLE_KEY` is set in `.env`
- Verify no typos in variable name

### Error: "Connection failed"
- Verify Supabase URL is correct
- Check that API keys are valid (not expired)
- Ensure internet connection is working

### Script works but app doesn't connect
- Make sure you're using `SUPABASE_ANON_KEY` (not service role key)
- Check Row Level Security (RLS) policies in Supabase
- Verify table names match exactly

## Files

- `.env.example` - Template file (safe to commit)
- `.env` - Your actual credentials (DO NOT COMMIT - already in .gitignore)
- `supabase_sync.py` - Uses `SUPABASE_SERVICE_ROLE_KEY`
- `test_analytics_query.py` - Uses `SUPABASE_SERVICE_ROLE_KEY`
- Mobile app - Uses `SUPABASE_ANON_KEY`

## CI/CD Setup

For GitHub Actions or other CI/CD:

1. Go to your repository → **Settings** → **Secrets**
2. Add these secrets:
   - `SUPABASE_URL`
   - `SUPABASE_SERVICE_ROLE_KEY`
   - `SUPABASE_DB_PASSWORD`

3. Update your workflow file to use secrets:
```yaml
env:
  SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
  SUPABASE_SERVICE_ROLE_KEY: ${{ secrets.SUPABASE_SERVICE_ROLE_KEY }}
```

## Next Steps

1. ✅ Set up `.env` file
2. ✅ Run sync script to verify connection
3. ✅ Check `API_DOCUMENTATION.md` for mobile app integration
4. ✅ Set up mobile app with anon key

---

**Need Help?** Check `API_DOCUMENTATION.md` for detailed API usage examples.

