from dotenv import load_dotenv
import os
load_dotenv()

# Fetch values from environment variables or use default values
SERVER_URL = os.getenv('SERVER_URL', '127.0.0.1')  # Default to localhost if not found
PORT = os.getenv('PORT', '8900')                   # Default to port 8000 if not found
ENV = os.getenv('ENV', 'dev')                      # Default to 'dev' environment

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')       # No default, ensure this is set in .env

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")