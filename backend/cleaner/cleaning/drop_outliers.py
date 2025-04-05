import pandas as pd

def drop_outliers(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include="number")
    if numeric_cols.empty:
        return df

    mask = pd.Series([True] * len(df))
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        mask &= df[col].between(lower, upper)

    return df[mask]