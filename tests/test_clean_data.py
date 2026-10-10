
import pandas as pd
from src.clean_data import clean_transactions


def test_invalid_quantity_is_removed():
    df = pd.DataFrame({
        "InvoiceNo": ["100", "101"],
        "StockCode": ["A", "B"],
        "InvoiceDate": ["2010-12-01", "2010-12-02"],
        "Quantity": [2, -1],
        "UnitPrice": [5.0, 5.0],
    })

    result = clean_transactions(df)

    assert len(result) == 1
    assert result.iloc[0]["TotalPrice"] == 10.0


def test_duplicate_rows_are_removed():
    row = {
        "InvoiceNo": "100",
        "StockCode": "A",
        "InvoiceDate": "2010-12-01",
        "Quantity": 2,
        "UnitPrice": 5.0,
    }

    df = pd.DataFrame([row, row])
    result = clean_transactions(df)

    assert len(result) == 1
