"""
Tests for utils module
"""
import pandas as pd
import io
import sys
from src.utils import dataset_overview


class TestUtils:
    """Test cases for utility functions"""
    
    def test_dataset_overview(self, capsys):
        """Test dataset overview printing"""
        df = pd.DataFrame(
            {
                "col1": [1, 2, 3],
                "col2": ["a", "b", "c"],
                "col3": [1.1, 2.2, 3.3],
            }
        )
        
        dataset_overview(df)
        
        captured = capsys.readouterr()
        assert "Dataset Shape:" in captured.out, "Should print dataset shape"
        assert "(3, 3)" in captured.out, "Should show correct shape"
        assert "Columns:" in captured.out, "Should print column names"
        assert "Data Types:" in captured.out, "Should print data types"
    
    def test_dataset_overview_empty(self, capsys):
        """Test dataset overview with empty DataFrame"""
        df = pd.DataFrame()
        
        dataset_overview(df)
        
        captured = capsys.readouterr()
        assert "Dataset Shape:" in captured.out, "Should handle empty DataFrame"
        assert "(0, 0)" in captured.out, "Should show correct empty shape"
