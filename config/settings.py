import os
from dotenv import load_dotenv

IS_CLOUD = os.getenv("STREAMLIT_RUNTIME") is not None

if not IS_CLOUD:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ENV_PATH = os.path.join(BASE_DIR, "env", ".env")
    load_dotenv(ENV_PATH)

ENV = os.getenv("ENV", "PROD")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")