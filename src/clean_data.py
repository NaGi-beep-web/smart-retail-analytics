
import pandas as pd


def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalize column names
    df.columns = df.columns.str.strip()

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Convert columns to appropriate types
    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"], errors="coerce"
    )
    df["Quantity"] = pd.to_numeric(
        df["Quantity"], errors="coerce"
    )
    df["UnitPrice"] = pd.to_numeric(
        df["UnitPrice"], errors="coerce"
    )

    # Remove records without essential transaction information
    df = df.dropna(
        subset=["InvoiceNo", "StockCode",
                "InvoiceDate", "Quantity", "UnitPrice"]
    )

    # Keep only rows with positive quantities and prices
    df = df[
        (df["Quantity"] > 0) &
        (df["UnitPrice"] > 0)
    ].copy()

    # Calculate the line total
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    return df
