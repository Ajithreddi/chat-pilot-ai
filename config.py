# Test and Production URLs
TEST_URL = "https://ajithreddy777.app.n8n.cloud/webhook-test/1e8f137c-0be7-4b2a-b6b9-894849164051"
PROD_URL = "https://ajithreddy777.app.n8n.cloud/webhook/1e8f137c-0be7-4b2a-b6b9-894849164051"

# Toggle environment
USE_TEST = False   # True = test URL, False = production

# Pick correct URL
WEBHOOK_URL = TEST_URL if USE_TEST else PROD_URL