# GitHub Secrets Setup Guide

## Overview
This guide shows how to set up GitHub Secrets for CI/CD workflows, so your credentials are never exposed in code.

## ✅ What's Already Done

- ✅ All hardcoded credentials removed from code
- ✅ Scripts now require environment variables
- ✅ `.env` file is in `.gitignore` (won't be committed)
- ✅ `.env.example` provided as template (safe to commit)

## 🔐 Setting Up GitHub Secrets

### Step 1: Go to Repository Settings

1. Open your GitHub repository
2. Click **Settings** (top menu)
3. Click **Secrets and variables** → **Actions** (left sidebar)

### Step 2: Add Required Secrets

Click **New repository secret** and add each of these:

#### Required Secrets:

1. **`SUPABASE_URL`**
   - Name: `SUPABASE_URL`
   - Value: Your Supabase project URL
   - Example: `https://your-project-id.supabase.co`

2. **`SUPABASE_SERVICE_ROLE_KEY`**
   - Name: `SUPABASE_SERVICE_ROLE_KEY`
   - Value: Your Supabase service_role key
   - Get from: Supabase Dashboard → Settings → API → service_role key
   - ⚠️ **Keep this secret!** Never expose publicly

3. **`SUPABASE_DB_PASSWORD`** (Optional)
   - Name: `SUPABASE_DB_PASSWORD`
   - Value: Your database password
   - Only needed if using direct PostgreSQL connections

### Step 3: Update GitHub Actions Workflow

Your `.github/workflows/main.yml` should use these secrets:

```yaml
env:
  SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
  SUPABASE_SERVICE_ROLE_KEY: ${{ secrets.SUPABASE_SERVICE_ROLE_KEY }}
  SUPABASE_DB_PASSWORD: ${{ secrets.SUPABASE_DB_PASSWORD }}
```

## 📝 Example Workflow File

```yaml
name: Sync to Supabase

on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight
  workflow_dispatch:  # Manual trigger

jobs:
  sync:
    runs-on: ubuntu-latest
    env:
      SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
      SUPABASE_SERVICE_ROLE_KEY: ${{ secrets.SUPABASE_SERVICE_ROLE_KEY }}
      SUPABASE_DB_PASSWORD: ${{ secrets.SUPABASE_DB_PASSWORD }}
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run sync script
        run: |
          python supabase_sync.py
```

## 🔍 Verifying Secrets Are Set

After adding secrets, you can verify they're set (but not see their values):

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. You should see your secrets listed
3. You can update or delete them, but you cannot view their values

## 🚨 Security Best Practices

### ✅ DO:
- Use GitHub Secrets for all sensitive data
- Use different keys for different environments (dev/prod)
- Rotate keys periodically
- Use service_role key only in CI/CD (server-side)
- Use anon key in mobile apps (client-side)

### ❌ DON'T:
- Commit `.env` files (already in `.gitignore`)
- Hardcode credentials in code
- Share service_role keys publicly
- Use service_role key in mobile apps
- Print secrets in logs

## 📱 Mobile App Keys

For mobile apps, you'll need different keys:

### Development
- Store in `.env` file (local only)
- Use `EXPO_PUBLIC_*` prefix for Expo
- Never commit to Git

### Production
- Use environment variables in your build system
- Use app config files (not in code)
- Use **anon key** only (never service_role)

## 🔄 Local Development Setup

For local development, create a `.env` file:

```bash
# Copy template
cp .env.example .env

# Edit .env and add your actual values
# This file is gitignored and won't be committed
```

## ✅ Checklist

- [ ] GitHub Secrets added for all required variables
- [ ] Workflow file updated to use secrets
- [ ] `.env` file created locally (not committed)
- [ ] `.env.example` updated (safe to commit)
- [ ] No hardcoded credentials in code
- [ ] Mobile app uses anon key (not service_role)

## 🆘 Troubleshooting

### Error: "SUPABASE_SERVICE_ROLE_KEY not found"
- Check GitHub Secrets are set correctly
- Verify secret names match exactly (case-sensitive)
- Check workflow file uses `${{ secrets.SECRET_NAME }}`

### Error: "Connection failed"
- Verify Supabase URL is correct
- Check API keys are valid (not expired)
- Ensure secrets are set in correct repository

### Secrets not working in workflow
- Check secret names match exactly
- Verify workflow has access to secrets
- Check workflow syntax is correct

---

**Remember**: Secrets are encrypted and can only be used in GitHub Actions workflows. They cannot be viewed once set, only updated or deleted.

