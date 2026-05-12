"""
Tests for preprocessing module
"""
import pytest
import pandas as pd
from src.preprocessing import (
    convert_to_datetime,
    remove_duplicates,
    check_missing_values,
    add_headline_length,
)


class TestPreprocessing:
    """Test cases for preprocessing functions"""
    
    def test_convert_to_datetime(self):
        """Test datetime conversion"""
        df = pd.DataFrame(
            {"date": ["2020-01-01", "2020-01-02", "2020-01-03"]}
        )
        
        result = convert_to_datetime(df, "date")
        
        assert pd.api.types.is_datetime64_any_dtype(result["date"]), "Should convert to datetime"
        assert len(result) == 3, "Should preserve all rows"
    
    def test_convert_to_datetime_with_invalid(self):
        """Test datetime conversion with invalid values"""
        df = pd.DataFrame(
            {"date": ["2020-01-01", "invalid", "2020-01-03"]}
        )
        
        result = convert_to_datetime(df, "date")
        
        assert pd.api.types.is_datetime64_any_dtype(result["date"]), "Should convert to datetime"
        assert pd.isna(result["date"].iloc[1]), "Invalid date should become NaT"
    
    def test_remove_duplicates(self):
        """Test duplicate removal"""
        df = pd.DataFrame(
            {"col1": [1, 2, 2, 3], "col2": ["a", "b", "b", "c"]}
        )
        
        result = remove_duplicates(df)
        
        assert len(result) == 3, "Should remove one duplicate"
        assert result["col1"].tolist() == [1, 2, 3], "Should preserve unique rows"
    
    def test_check_missing_values(self):
        """Test missing value detection"""
        df = pd.DataFrame(
            {
                "col1": [1, 2, None, 4],
                "col2": ["a", None, "c", "d"],
            }
        )
        
        result = check_missing_values(df)
        
        assert result["col1"] == 1, "Should detect 1 missing value in col1"
        assert result["col2"] == 1, "Should detect 1 missing value in col2"
    
    def test_add_headline_length(self):
        """Test headline length feature"""
        df = pd.DataFrame(
            {"headline": ["Short", "This is a medium headline", "This is a very long headline that contains many words"]}
        )
        
        result = add_headline_length(df)
        
        assert "headline_length" in result.columns, "Should add headline_length column"
        assert result["headline_length"].iloc[0] == 5, "First headline length should be 5"
        assert result["headline_length"].iloc[1] == 25, "Second headline length should be 25"
        assert result["headline_length"].iloc[2] == 53, "Third headline length should be 53"
