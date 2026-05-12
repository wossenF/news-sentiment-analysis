"""
Tests for data_loader module
"""
import pytest
import pandas as pd
from src.data_loader import load_news_data

# Try to import load_stock_data; use conditional import to handle if not available
try:
    from src.data_loader import load_stock_data
    HAS_LOAD_STOCK_DATA = True
except (ImportError, AttributeError):
    HAS_LOAD_STOCK_DATA = False


class TestDataLoader:
    """Test cases for data loading functions"""

    def test_load_news_data(self):
        """Test loading news data"""
        df = load_news_data()

        assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
        assert len(df) > 0, "DataFrame should not be empty"
        assert "headline" in df.columns, "Should have headline column"

    @pytest.mark.skipif(not HAS_LOAD_STOCK_DATA, reason="load_stock_data not available")
    def test_load_stock_data_aapl(self):
        """Test loading AAPL stock data"""
        df = load_stock_data("AAPL.csv")

        assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
        assert len(df) > 0, "DataFrame should not be empty"
        assert "Date" in df.columns or "date" in df.columns, "Should have date column"
        assert "Close" in df.columns or "close" in df.columns, "Should have close column"

    @pytest.mark.skipif(not HAS_LOAD_STOCK_DATA, reason="load_stock_data not available")
    def test_load_stock_data_amzn(self):
        """Test loading AMZN stock data"""
        df = load_stock_data("AMZN.csv")

        assert isinstance(df, pd.DataFrame), "Should return a DataFrame"
        assert len(df) > 0, "DataFrame should not be empty"

    @pytest.mark.skipif(not HAS_LOAD_STOCK_DATA, reason="load_stock_data not available")
    def test_nonexistent_file(self):
        """Test that loading non-existent file raises FileNotFoundError"""
        with pytest.raises(FileNotFoundError):
            load_stock_data("nonexistent.csv")
