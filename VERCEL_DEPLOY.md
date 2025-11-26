# Quick Vercel Deployment Guide

## Step 1: Install Vercel CLI (if not installed)

```bash
npm install -g vercel
```

## Step 2: Login to Vercel

```bash
vercel login
```

## Step 3: Deploy

From your project directory:

```bash
vercel
```

Follow the prompts:
- Set up and deploy? **Yes**
- Which scope? (Choose your account)
- Link to existing project? **No**
- Project name? (Press Enter for default)
- Directory? (Press Enter for current directory)

## Step 4: Deploy to Production

```bash
vercel --prod
```

## Alternative: Deploy via GitHub

1. Push your code to GitHub
2. Go to https://vercel.com
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will auto-detect Python and deploy

## Important Notes:

- **File paths**: Make sure your data files (`1_ab.txt`, `2_ec.txt`, `3_eb.txt`) are in the root directory
- **Dependencies**: `requirements.txt` is automatically detected
- **Serverless**: Vercel uses serverless functions, so the app will work differently than local Flask

## If You Get Errors:

1. **Missing files**: Ensure all `.txt` data files are committed to git
2. **Python version**: Vercel uses Python 3.9 by default
3. **Dependencies**: Check that all packages in `requirements.txt` are compatible

## Quick Test After Deployment:

Visit your Vercel URL (provided after deployment) and check:
- `/` - Main page
- `/api/data` - API endpoint

## Troubleshooting:

If the app doesn't work, check Vercel logs:
```bash
vercel logs
```

Or check the Vercel dashboard for function logs.

