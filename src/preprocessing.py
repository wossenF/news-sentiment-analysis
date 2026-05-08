import pandas as pd

def convert_to_datetime(df: pd.DataFrame, column: str = "date") -> pd.DataFrame:
    """
    Convert date column to datetime format.
    """
    df[column] = pd.to_datetime(df[column], errors="coerce")

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates()

def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Return missing value counts.
    """
    return df.isnull().sum()



def add_headline_length(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add headline length column.
    """
    df["headline_length"] = df["headline"].astype(str).apply(len)

    return df