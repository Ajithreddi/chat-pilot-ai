import os
from dotenv import load_dotenv

# Detect if running on Streamlit Cloud
IS_CLOUD = os.getenv("STREAMLIT_RUNTIME", None) is not None

if not IS_CLOUD:
    # LOCAL PROD: Load .env from /env folder
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ENV_PATH = os.path.join(BASE_DIR, "env", ".env")
    load_dotenv(ENV_PATH)

# Shared config (both local & cloud)
ENV = os.getenv("ENV", "PROD")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

print("\n[CONFIG] ---------")
print(f"Running on Cloud? {IS_CLOUD}")
if not IS_CLOUD:
    print(f"Loaded local .env: {ENV_PATH}")
print(f"ENV = {ENV}")
print(f"WEBHOOK_URL = {WEBHOOK_URL}")
print("[CONFIG] ---------\n")



# import os

# ENV = os.getenv("ENV", "PROD")
# WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# print(f"[CONFIG] ENV = {ENV}")
# print(f"[CONFIG] WEBHOOK_URL = {WEBHOOK_URL}")


# import os
# from dotenv import load_dotenv

# # Get base directory (CHATPILOT-AI root)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Path to active .env file
# ENV_PATH = os.path.join(BASE_DIR, "env", ".env")

# # Load .env
# load_dotenv(ENV_PATH)

# ENV = os.getenv("ENV", "DEV")
# WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# print(f"[CONFIG] Loaded from {ENV_PATH}")
# print(f"[CONFIG] ENV = {ENV}")
# print(f"[CONFIG] WEBHOOK_URL = {WEBHOOK_URL}")




# # Test and Production URLs
# TEST_URL = "https://ajithreddy777.app.n8n.cloud/webhook-test/1e8f137c-0be7-4b2a-b6b9-894849164051"
# PROD_URL = "https://ajithreddy777.app.n8n.cloud/webhook/1e8f137c-0be7-4b2a-b6b9-894849164051"

# # Toggle environment
# USE_TEST = False  # True = test URL, False = production

# # Pick correct URL
# WEBHOOK_URL = TEST_URL if USE_TEST else PROD_URL
