# GitHub Actions Workflow Setup

## Overview
The GitHub Actions workflow automatically runs the scraper and syncs data to Supabase daily.

## Workflow Steps

The workflow (`/.github/workflows/main.yml`) performs these steps in order:

1. **Checkout code** - Gets the latest code from repository
2. **Set up Python 3.10** - Configures Python environment
3. **Install dependencies** - Installs packages from `requirements.txt`
4. **Set Time Zone** - Sets timezone to America/Port_of_Spain
5. **Run Scraper** - Executes `pricesmart_scraper.py` to scrape products
6. **Verify Database** - Checks that database file was created
7. **Sync to Supabase** - Runs `supabase_sync.py` to sync data
8. **Update README** - Updates README with analysis report
9. **Commit & Push** - Commits changes back to repository

## Required GitHub Secrets

Make sure these secrets are set in your repository:

1. **`SUPABASE_URL`**
   - Your Supabase project URL
   - Example: `https://your-project-id.supabase.co`

2. **`SUPABASE_SERVICE_ROLE_KEY`**
   - Your Supabase service_role key
   - Get from: Supabase Dashboard → Settings → API → service_role key

3. **`SUPABASE_DB_PASSWORD`** (Optional)
   - Database password if using direct PostgreSQL connections

4. **`GH_TOKEN`** (for committing)
   - GitHub personal access token with repo permissions

5. **`GitName`** (for committing)
   - Git username for commits

6. **`GitEmail`** (for committing)
   - Git email for commits

## How to Set Up Secrets

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret with the exact name shown above

## Workflow Schedule

The workflow runs:
- **Daily at midnight UTC** (cron: `0 0 * * *`)
- You can also trigger it manually via **Actions** tab → **Run workflow**

## What Gets Synced

The sync step (`supabase_sync.py`) syncs:

1. **Products** - All products from SQLite to Supabase `pricesmart_products` table
2. **Price History** - All price change records to `price_history` table
3. **Analytics** - Calculated analytics to `analytics` table

## Error Handling

- If scraper fails, sync won't run
- If database file is missing, sync step will fail
- If sync fails, workflow will fail (won't commit changes)
- All errors are logged in GitHub Actions logs

## Monitoring

To check if workflow ran successfully:

1. Go to **Actions** tab in GitHub
2. Click on the latest workflow run
3. Check each step for success/failure
4. View logs for detailed output

## Troubleshooting

### Sync Step Fails

**Error: "SUPABASE_SERVICE_ROLE_KEY not found"**
- Check GitHub Secrets are set correctly
- Verify secret names match exactly (case-sensitive)

**Error: "Database file not found"**
- Scraper may have failed
- Check scraper step logs for errors

**Error: "Connection failed"**
- Verify Supabase URL is correct
- Check API key is valid (not expired)
- Ensure Supabase project is active

### Workflow Not Running

**Scheduled workflow not triggering:**
- Check workflow file syntax is correct
- Verify cron schedule is valid
- GitHub Actions may have delays (up to 15 minutes)

**Manual trigger not working:**
- Check workflow file is in `.github/workflows/` directory
- Verify file is named correctly (`main.yml`)
- Check for YAML syntax errors

## Testing Locally

Before relying on GitHub Actions, test locally:

```bash
# 1. Run scraper
python pricesmart_scraper.py

# 2. Verify database exists
ls Database/PriceSmart_Products_Database.db

# 3. Run sync (with .env file)
python supabase_sync.py
```

## Workflow File Location

The workflow file is located at:
```
.github/workflows/main.yml
```

## Customization

### Change Schedule

Edit the cron expression in `main.yml`:
```yaml
schedule:
  - cron: "0 0 * * *"  # Daily at midnight UTC
```

Common schedules:
- `"0 */6 * * *"` - Every 6 hours
- `"0 0 * * 1"` - Every Monday at midnight
- `"0 0 1 * *"` - First day of every month

### Add Manual Trigger

Add `workflow_dispatch` to allow manual runs:
```yaml
on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:  # Allows manual trigger
```

### Skip Sync on Errors

If you want workflow to continue even if sync fails:
```yaml
- name: Sync to Supabase
  continue-on-error: true  # Don't fail workflow if sync fails
```

## Security Notes

- ✅ All secrets are encrypted in GitHub
- ✅ Secrets are only available to GitHub Actions
- ✅ Service role key is never exposed in logs
- ✅ Database file is not committed (in .gitignore)

---

**Last Updated**: 2025-11-12

