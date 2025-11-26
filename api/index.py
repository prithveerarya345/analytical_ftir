# Vercel serverless function - Flask app wrapper
import sys
import os

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

try:
    from app import app
except Exception as e:
    # For debugging - will show in Vercel logs
    import traceback
    error_msg = f"Import error: {str(e)}\n{traceback.format_exc()}"
    print(error_msg)
    raise

# Vercel Python runtime automatically handles WSGI apps
# Just export the Flask app object
