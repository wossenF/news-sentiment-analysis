# Notebooks Guide

This directory contains Jupyter notebooks for analyzing news sentiment and its correlation with stock market movements.

## 📓 Available Notebooks

### 1. task1_eda.ipynb - Exploratory Data Analysis (EDA)

**Objective:** Perform comprehensive exploratory analysis of news and stock data.

**Contents:**
- Load news and stock datasets
- Display dataset information and statistics
- Check for missing values and duplicates
- Analyze headline length distributions
- Identify top publishers
- Extract key keywords from headlines
- Perform basic correlation analysis

**Data Used:**
- `data/raw/newsData/raw_analyst_ratings.csv` - News/analyst data
- `data/raw/AAPL.csv`, `AMZN.csv`, `GOOG.csv`, `META.csv`, `NVDA.csv` - Stock data

**Key Outputs:**
- Dataset summaries
- Distribution charts
- Publisher rankings
- Top keywords and topics

**Target Audience:** Data analysts, business stakeholders

---

### 2. task2_quantitative_analysis.ipynb - Quantitative Analysis

**Objective:** Conduct statistical and financial analysis of stock data.

**Contents:**
- Load and preprocess stock price data
- Calculate daily returns
- Analyze volatility metrics
- Examine trading volumes
- Compute moving averages
- Statistical summaries and distributions

**Data Used:**
- Historical stock prices for AAPL, AMZN, GOOG, META, NVDA

**Key Metrics:**
- Daily returns
- Rolling volatility
- Price trends
- Volume patterns

**Target Audience:** Financial analysts, quantitative researchers

---

### 3. task3_sentiment_correlation.ipynb - Sentiment-Stock Correlation

**Objective:** Analyze and visualize correlations between news sentiment and stock market movements.

**Contents:**
- Load and normalize news sentiment data
- Load stock price data with timezone-aware datetime handling
- Align news dates with stock trading dates
- Calculate correlation coefficients
- Perform time-lagged correlation analysis
- Visualize sentiment-price relationships
- Statistical significance testing

**Data Used:**
- News sentiment from analyst ratings
- Stock prices aligned by date

**Key Analysis:**
- Pearson correlation coefficients
- Lagged correlations (1-5 day lags)
- Rolling correlation windows
- Predictive insights

**Target Audience:** Researchers, investment professionals

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+
- Virtual environment activated with dependencies installed
- See main README.md for installation instructions

### Running a Notebook

1. **Start Jupyter Lab** (recommended):
   ```bash
   jupyter lab
   ```

2. **Or start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

3. Navigate to the desired notebook and open it

4. Run cells sequentially using `Shift + Enter` or the Run button

5. All dependencies will be imported automatically

### Running All Cells
- Use `Kernel` → `Restart Kernel and Run All Cells` to run entire notebook

### Clearing Output
- Use `Kernel` → `Restart Kernel` to clear outputs and reset notebook state

---

## 📊 Data Flow

```
Raw Data (CSV files)
      ↓
Data Loading (data_loader.py)
      ↓
Preprocessing (preprocessing.py)
      ↓
Analysis (text_analysis.py, time_analysis.py)
      ↓
Visualization (visualization.py)
      ↓
Notebook Outputs (Charts, Statistics, Insights)
```

---

## ⚠️ Common Issues & Solutions

### Issue: File not found error
- **Cause:** Notebooks must be run from project root or paths may be incorrect
- **Solution:** Ensure your working directory is the project root
- **Code:** `%cd /path/to/news-sentiment-analysis`

### Issue: Timezone-aware/naive datetime mixing
- **Cause:** Mixing timezone-aware and timezone-naive datetime values
- **Solution:** Use `pd.to_datetime(..., utc=True).dt.tz_localize(None)` for normalization
- **Applied in:** task3_sentiment_correlation.ipynb

### Issue: Module import errors
- **Cause:** Virtual environment not activated or packages not installed
- **Solution:** 
  ```bash
  source venv/bin/activate  # or venv\Scripts\activate on Windows
  pip install -r requirements.txt
  ```

### Issue: Kernel crashes or hangs
- **Cause:** Memory issues with large datasets or infinite loops
- **Solution:** Restart kernel and run cells one at a time

---

## 📈 Output Files

Notebooks generate:
- **Display outputs** - Charts, tables, and statistics shown inline
- **Variables in memory** - DataFrames and analysis results available for further use
- **Print statements** - Informational messages and debug output

To save outputs:
- Right-click charts and select "Save Image"
- Use `.to_csv()` to export DataFrames
- Use `.to_json()` for JSON export

---

## 🔄 Execution Order

**Recommended execution sequence:**

1. **task1_eda.ipynb** - Understand the data first
2. **task2_quantitative_analysis.ipynb** - Analyze stock movements
3. **task3_sentiment_correlation.ipynb** - Find sentiment-stock correlations

Each notebook is independent but should be run in this order for logical flow.

---

## 💡 Tips for Working with Notebooks

- **Use markdown cells** to document your analysis and findings
- **Add comments** in code cells to explain complex operations
- **Restart kernel regularly** to ensure clean state
- **Test with small data samples** before running on full dataset
- **Version control** - Commit `.ipynb` files to track analysis progress
- **Create backups** before making major changes

---

## 📞 Support

For issues or questions:
1. Check the main README.md for project context
2. Review the module documentation in `src/`
3. Check GitHub Issues for known problems
4. Add print statements or use debuggers to troubleshoot

---

**Last Updated:** May 12, 2026
