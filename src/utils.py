import pandas as pd



def dataset_overview(df: pd.DataFrame):
    """
    Print basic dataset overview.
    """
    print("Dataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)