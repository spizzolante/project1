import pandas as pd

def update_columns_to_lower(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower().str.strip()
    return df


# function to convert all floats as integers
def float_to_int(df: pd.DataFrame) -> pd.DataFrame:
    for column in df.columns:
        if df[column].dtype == 'float64':
            df[column] = df[column].astype(int)
    return df