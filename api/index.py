# Vercel serverless function wrapper for Flask app
import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel serverless function handler
def handler(request):
    return app(request.environ, request.start_response)

# Export app for Vercel
__all__ = ['app', 'handler']

