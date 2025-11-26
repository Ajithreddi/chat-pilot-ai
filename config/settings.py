import os
from dotenv import load_dotenv

# Detect if running on Streamlit Cloud
IS_CLOUD = os.getenv("STREAMLIT_RUNTIME") is not None

if not IS_CLOUD:
    # Load from env/.env when running locally
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ENV_PATH = os.path.join(BASE_DIR, "env", ".env")
    load_dotenv(ENV_PATH)

# Load environment (DEV or PROD)
ENV = os.getenv("ENV", "PROD").upper()

# Webhook: Cloud will directly provide WEBHOOK_URL
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Local fallback logic (automatically select correct webhook)
if not IS_CLOUD:
    if ENV == "DEV":
        WEBHOOK_URL = os.getenv("DEV_WEBHOOK_URL")
    else:
        WEBHOOK_URL = os.getenv("PROD_WEBHOOK_URL")

# Debug info for logs
print(f"[ENV CHECK] Running environment: {ENV}")