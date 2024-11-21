import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of files to create for the updated project structure
list_of_files = [
    "app.py",
    "requirements.txt",
    "README.md",
    "config.py",
    "data/raw/.gitkeep",            # Placeholder for raw data
    "data/processed/.gitkeep",      # Placeholder for processed data
    "data/schemas/schema.json",     # Placeholder for data schema
    "assets/css/styles.css",        # Placeholder for custom CSS
    "assets/images/.gitkeep",       # Placeholder for static images
    "components/__init__.py",
    "components/navbar.py",
    "components/sidebar.py",
    "components/graphs.py",
    "components/tables.py",
    "pages/__init__.py",
    "pages/overview.py",
    "pages/distribution.py",
    "pages/comparison.py",
    "pages/trends.py",
    "scripts/__init__.py",
    "scripts/data_cleaning.py",
    "scripts/data_loader.py",
    "scripts/analysis.py",
    "scripts/visualization.py",
    "tests/__init__.py",
    "tests/test_app.py",
    "tests/test_data_cleaning.py",
    "tests/test_visualization.py",
    "logs/app.log",                 # Placeholder for app logs
    "logs/error.log",               # Placeholder for error logs
    "deployment/Dockerfile",
    "deployment/docker-compose.yml",
    "deployment/nginx.conf",
    "deployment/wsgi.py"
]

# Create directories and files based on the list
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # Create directory if it doesn't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    # Create the file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
