import os
from dotenv import load_dotenv

# Detect if running on Streamlit Cloud
IS_CLOUD = os.getenv("STREAMLIT_RUNTIME") is not None

if not IS_CLOUD:
    # Load .env for LOCAL dev/prod
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ENV_PATH = os.path.join(BASE_DIR, "env", ".env")
    load_dotenv(ENV_PATH)

ENV = os.getenv("ENV", "DEV")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")


print(f"Running on Cloud? {IS_CLOUD}")
print(f"ENV: {ENV}")
print(f"WEBHOOK_URL: {WEBHOOK_URL}")
