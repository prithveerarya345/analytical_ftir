# Quick Fix for Vercel 500 Error

## Immediate Steps:

### 1. Check Vercel Logs
Go to Vercel Dashboard → Your Project → Functions → Check the error message

### 2. Most Likely Issue: File Paths
The data files might not be found. I've updated the code to try multiple paths.

### 3. Redeploy
```bash
git add .
git commit -m "Fix Vercel deployment"
git push
vercel --prod
```

### 4. If Still Failing - Check Logs
The error will show in Vercel logs. Common issues:
- **FileNotFoundError**: Data files not in repo or wrong path
- **ImportError**: Missing dependencies
- **ModuleNotFoundError**: Check requirements.txt

### 5. Alternative: Test Locally
```bash
vercel dev
```
This simulates Vercel environment and shows errors locally.

## Files Updated:
✅ `api/index.py` - Better error handling
✅ `app.py` - Enhanced file path resolution (already had it)
✅ `vercel.json` - Correct configuration

## Next Steps:
1. Check Vercel logs for specific error
2. Ensure all `.txt` files are committed
3. Redeploy
4. If error persists, share the log message

