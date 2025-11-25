# Wrapper to run the production app on Streamlit Cloud

import runpy

# Run the prod/app.py file as the main script
runpy.run_path("prod/app.py", run_name="__main__")