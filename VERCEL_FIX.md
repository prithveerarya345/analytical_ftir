# Vercel Deployment Fix

## Common Issues & Solutions

### Issue: Serverless Function Crashed (500 Error)

**Possible Causes:**
1. File paths not found (data files)
2. Import errors
3. Missing dependencies
4. Flask WSGI wrapper issues

## Quick Fix Steps:

### 1. Check Vercel Logs
```bash
vercel logs
```
Or check in Vercel dashboard → Your Project → Deployments → Click deployment → Functions tab

### 2. Ensure Data Files are Committed
Make sure these files are in your git repo:
- `1_ab.txt`
- `2_ec.txt`
- `3_eb.txt`

### 3. Test Locally with Vercel
```bash
vercel dev
```
This will simulate Vercel environment locally.

### 4. Check File Paths
The app now tries multiple paths:
- Current directory
- Same directory as app.py
- Parent directory

### 5. Alternative: Use Environment Variables
If files still not found, you could:
- Upload data files to a CDN
- Use environment variables for file paths
- Embed data in code (not recommended for large files)

## Updated Files:
- ✅ `api/index.py` - Proper Flask wrapper with error handling
- ✅ `app.py` - Enhanced file path resolution
- ✅ `vercel.json` - Correct routing

## Redeploy:
```bash
vercel --prod
```

## Debug Checklist:
- [ ] All data files committed to git
- [ ] `requirements.txt` has all dependencies
- [ ] Check Vercel logs for specific error
- [ ] Test with `vercel dev` locally
- [ ] Verify file paths in logs

