from pathlib import Path
import pandas as pd

# ALWAYS resolve from project root (src -> parent -> parent)
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "raw" / "newsData"


def load_news_data(filename="raw_analyst_ratings.csv"):
    file_path = DATA_PATH / filename

    print("Loading from:", file_path)  # optional debug

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path)