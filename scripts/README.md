# Scripts Guide

This directory is intended for Python scripts that automate analysis, data processing, or other project tasks.

## 📝 Purpose

The `scripts/` directory contains standalone Python scripts for:
- Automated data loading and preprocessing
- Batch processing of datasets
- Pipeline orchestration
- Report generation
- Data validation and quality checks

## 📂 Current Scripts

Currently, this directory is prepared for scripts. Add production-ready scripts here as they are developed.

## 🚀 Running Scripts

From the project root directory:

```bash
# Run a script
python scripts/your_script.py

# With arguments
python scripts/your_script.py --input data.csv --output results.csv

# With virtual environment activated
python -m scripts.your_script
```

## 📋 Script Development Guidelines

When creating new scripts:

1. **Add docstring** at the top explaining purpose
   ```python
   """
   Script Description: What this script does
   Usage: python scripts/script_name.py [options]
   """
   ```

2. **Use argument parsing** for flexibility
   ```python
   import argparse
   
   parser = argparse.ArgumentParser(description='Script description')
   parser.add_argument('--input', required=True, help='Input file path')
   args = parser.parse_args()
   ```

3. **Use relative imports** from src modules
   ```python
   from src.data_loader import load_news_data
   from src.preprocessing import convert_to_datetime
   ```

4. **Handle errors gracefully**
   ```python
   try:
       data = load_data(filepath)
   except FileNotFoundError:
       print(f"Error: File not found: {filepath}")
       exit(1)
   ```

5. **Add logging** for production scripts
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   ```

## 🔄 Integration with Notebooks

- **Notebooks** - Interactive exploration and analysis
- **Scripts** - Automated, production-ready operations

Scripts can perform the same operations as notebooks but:
- Are version-controlled more easily
- Can be scheduled/automated
- Support command-line arguments
- Are more suitable for CI/CD pipelines

## 📊 Example Script Template

```python
"""
Process news and stock data for sentiment analysis.
Usage: python scripts/process_data.py --output processed_data.csv
"""

import sys
import argparse
import logging
from pathlib import Path

from src.data_loader import load_news_data, load_stock_data
from src.preprocessing import convert_to_datetime, add_headline_length

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(output_path: str):
    """Main processing function."""
    try:
        logger.info("Loading data...")
        news_df = load_news_data()
        
        logger.info("Processing news data...")
        news_df = convert_to_datetime(news_df, "date")
        news_df = add_headline_length(news_df)
        
        logger.info(f"Saving processed data to {output_path}...")
        news_df.to_csv(output_path, index=False)
        
        logger.info("Processing complete!")
        
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process news and stock data")
    parser.add_argument("--output", default="processed_data.csv", 
                       help="Output file path")
    args = parser.parse_args()
    
    main(args.output)
```

## 🧪 Testing Scripts

Test scripts can be added here:
```bash
# Run script tests
pytest tests/test_scripts.py

# Or run tests for a specific script
pytest tests/test_data_processing.py
```

## 📦 Dependencies

All scripts inherit dependencies from the main project. Ensure virtual environment is activated:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Then install dependencies
pip install -r requirements.txt
```

## 🔗 Related Documentation

- [Main README](../README.md) - Project overview
- [Notebooks Guide](../notebooks/README.md) - Interactive analysis notebooks
- [Source Modules](../src/) - Core analysis modules
- [Requirements](../requirements.txt) - Python dependencies

---

**Last Updated:** May 12, 2026
