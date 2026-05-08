import pandas as pd



def get_daily_news_counts(df: pd.DataFrame) -> pd.Series:
    """
    Count articles published per day.
    """
    daily_counts = df.groupby(df["date"].dt.date).size()

    return daily_counts



def get_hourly_news_counts(df: pd.DataFrame) -> pd.Series:
    """
    Count articles published per hour.
    """
    hourly_counts = df.groupby(df["date"].dt.hour).size()

    return hourly_counts