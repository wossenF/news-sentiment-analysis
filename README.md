# News Sentiment Analysis

A comprehensive Python project for analyzing sentiment in financial news articles and correlating sentiment with stock market movements. This project combines natural language processing, statistical analysis, and data visualization to uncover relationships between news sentiment and stock price movements.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Module Documentation](#module-documentation)
- [Notebooks](#notebooks)
- [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)

---

## 🎯 Overview

This project analyzes financial news sentiment and its potential correlation with stock market performance for major tech companies (AAPL, AMZN, GOOG, META, NVDA). It uses analyst ratings data combined with historical stock prices to perform comprehensive exploratory analysis and correlation studies.

**Key Objectives:**
- Perform exploratory data analysis (EDA) on financial news and stock data
- Extract and analyze sentiment indicators from news articles
- Conduct quantitative analysis of stock price movements
- Identify correlations between news sentiment and stock market trends
- Visualize patterns and distributions in the data

---

## 📁 Project Structure

```
news-sentiment-analysis/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .github/
│   └── workflows/
│       └── unittests.yml             # GitHub Actions CI/CD pipeline
├── data/
│   └── raw/
│       ├── AAPL.csv                  # Apple stock data
│       ├── AMZN.csv                  # Amazon stock data
│       ├── GOOG.csv                  # Google stock data
│       ├── META.csv                  # Meta stock data
│       ├── NVDA.csv                  # NVIDIA stock data
│       └── newsData/
│           └── raw_analyst_ratings.csv  # Financial analyst ratings
├── notebooks/
│   ├── README.md                     # Notebook guide
│   ├── task1_eda.ipynb              # Exploratory Data Analysis
│   ├── task2_quantitative_analysis.ipynb  # Statistical analysis
│   └── task3_sentiment_correlation.ipynb  # Sentiment-stock correlation
├── src/
│   ├── __init__.py
│   ├── data_loader.py               # Data loading utilities
│   ├── preprocessing.py             # Data cleaning and preprocessing
│   ├── text_analysis.py             # NLP and text analysis
│   ├── time_analysis.py             # Temporal analysis functions
│   ├── utils.py                     # General utility functions
│   └── visualization.py             # Plotting and visualization
├── scripts/
│   ├── __init__.py
│   └── README.md                    # Script guide
├── tests/
│   └── __init__.py                  # Unit tests directory
└── venv/                            # Python virtual environment
```

---

## ✨ Features

### Data Processing
- **Data Loading**: Load news and stock data from CSV files with robust error handling
- **Date Conversion**: Intelligent datetime parsing with timezone normalization
- **Duplicate Removal**: Identify and remove duplicate records
- **Missing Value Detection**: Comprehensive missing value analysis

### Text Analysis
- **TF-IDF Keyword Extraction**: Extract top keywords from headlines using TF-IDF scoring
- **Publisher Analysis**: Identify and rank most active publishers
- **Topic Modeling**: Latent Dirichlet Allocation (LDA) for topic discovery
- **Text Preprocessing**: Clean and normalize headline text

### Temporal Analysis
- **Daily News Volume**: Track article publication volume by day
- **Hourly Distribution**: Analyze publishing patterns by hour

### Visualization
- **Headline Length Distribution**: Visualize news article length patterns
- **Publisher Rankings**: Chart top news sources
- **Time Series Plots**: Daily and hourly news volume trends
- **Stock Price Charts**: Historical price movements for tech stocks

### Statistical Analysis
- **Correlation Studies**: Analyze relationships between sentiment and stock movements
- **Quantitative Metrics**: Calculate returns, volatility, and other financial indicators
- **Distribution Analysis**: Examine data distributions and patterns

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/wossenF/news-sentiment-analysis.git
   cd news-sentiment-analysis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Running Jupyter Notebooks

Start Jupyter Lab/Notebook to explore the analysis:

```bash
jupyter lab
# or
jupyter notebook
```

Then navigate to the `notebooks/` directory and open the desired notebook:

- **task1_eda.ipynb** - Exploratory Data Analysis
- **task2_quantitative_analysis.ipynb** - Quantitative Analysis
- **task3_sentiment_correlation.ipynb** - Sentiment Correlation Analysis

### Using Modules

Import and use individual modules in your own scripts:

```python
from src.data_loader import load_news_data, load_stock_data
from src.preprocessing import convert_to_datetime, add_headline_length
from src.text_analysis import get_top_keywords, get_top_publishers
from src.visualization import plot_headline_length_distribution

# Load data
news_df = load_news_data()
stock_df = load_stock_data("AAPL.csv")

# Process data
news_df = convert_to_datetime(news_df, "date")
news_df = add_headline_length(news_df)

# Analyze
keywords = get_top_keywords(news_df["headline"], top_n=20)
publishers = get_top_publishers(news_df, top_n=10)

# Visualize
plot_headline_length_distribution(news_df)
```

---

## 📊 Data

### Stock Data Files
Located in `data/raw/`:
- **AAPL.csv** - Apple Inc. historical stock prices
- **AMZN.csv** - Amazon.com Inc. historical stock prices
- **GOOG.csv** - Alphabet Inc. (Google) historical stock prices
- **META.csv** - Meta Platforms Inc. (Facebook) historical stock prices
- **NVDA.csv** - NVIDIA Corporation historical stock prices

### News Data
Located in `data/raw/newsData/`:
- **raw_analyst_ratings.csv** - Analyst ratings and sentiment data for financial news articles

### Data Format
Stock data typically includes: Date, Open, High, Low, Close, Volume
News data includes: date, headline, publisher, analyst_rating, and other metadata

---

## 🔧 Module Documentation

### `src/data_loader.py`
Handles loading data from CSV files with proper path resolution.

**Functions:**
- `load_news_data(filename)` - Load analyst ratings and news data
- `load_stock_data(filename)` - Load stock price data for a specific ticker

### `src/preprocessing.py`
Data cleaning and transformation utilities.

**Functions:**
- `convert_to_datetime(df, column)` - Convert date column to datetime format
- `remove_duplicates(df)` - Remove duplicate rows
- `check_missing_values(df)` - Count missing values per column
- `add_headline_length(df)` - Add headline length feature

### `src/text_analysis.py`
Natural language processing and text analysis.

**Functions:**
- `get_top_keywords(headlines, top_n)` - Extract top TF-IDF keywords
- `get_top_publishers(df, top_n)` - Return most active publishers
- `extract_email_domains(df)` - Extract publisher email domains
- `perform_lda_topic_modeling(headlines, n_topics)` - Topic modeling using LDA

### `src/time_analysis.py`
Temporal pattern analysis.

**Functions:**
- `get_daily_news_counts(df)` - Count articles per day
- `get_hourly_news_counts(df)` - Count articles per hour

### `src/visualization.py`
Data visualization utilities using Matplotlib.

**Functions:**
- `plot_headline_length_distribution(df)` - Distribution histogram
- `plot_top_publishers(publisher_counts)` - Bar chart of top publishers
- `plot_daily_news_volume(daily_counts)` - Time series of daily volume
- `plot_hourly_news_volume(hourly_counts)` - Bar chart of hourly distribution

### `src/utils.py`
General utility functions.

**Functions:**
- `dataset_overview(df)` - Print dataset shape, columns, and dtypes

---

## 📓 Notebooks

### 1. task1_eda.ipynb - Exploratory Data Analysis
Comprehensive EDA of news and stock data including:
- Dataset overviews and statistics
- Missing value analysis
- Distribution analysis
- Publisher and keyword analysis
- Basic correlations

### 2. task2_quantitative_analysis.ipynb - Quantitative Analysis
Financial and statistical analysis including:
- Stock price trends
- Return calculations
- Volatility analysis
- Volume analysis
- Moving averages

### 3. task3_sentiment_correlation.ipynb - Sentiment Correlation
Advanced analysis correlating news sentiment with stock movements:
- Sentiment scoring
- Correlation analysis
- Time-lagged correlations
- Visualization of relationships

---

## 🧪 Testing

Run unit tests using pytest:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests for a specific file:

```bash
pytest tests/test_module.py
```

Add test files in the `tests/` directory following pytest conventions.

---

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for continuous integration and testing.

**Workflow: `.github/workflows/unittests.yml`**

Triggers on:
- Push to `main`, `master`, `task-1`, or `task-3` branches
- Pull requests targeting `main`

Pipeline steps:
1. Checkout repository
2. Set up Python 3.8
3. Install dependencies
4. Run pytest suite

View workflow runs in the GitHub Actions tab of the repository.

---

## 📈 Requirements

Key dependencies:
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning and NLP tools
- **matplotlib** - Data visualization
- **pytest** - Unit testing framework
- **python-dateutil** - Date utilities
- **tzdata** - Timezone data

Full dependency list in `requirements.txt`.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Create a feature branch from `main`
2. Make your changes and add tests
3. Ensure all tests pass: `pytest`
4. Commit with clear messages following conventional commits
5. Push to your branch
6. Submit a pull request

---

## 📝 Notes

- All paths in the codebase resolve from the project root using `pathlib.Path`
- Datetime values are normalized to remove timezone awareness inconsistencies
- Data files should be placed in `data/raw/` directory
- Use virtual environment to avoid dependency conflicts

---

**Last Updated:** May 12, 2026