

from pathlib import Path
import pandas as pd

from clean_data import clean_transactions

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "raw" / "Online Retail.xlsx"


def main():
    df = pd.read_excel(DATA_PATH)

    cleaned = clean_transactions(df)

    print("Original rows:", len(df))
    print("Cleaned rows:", len(cleaned))
    print("\nSample cleaned data:")
    print(cleaned.head())

    print("\nTotal sales value:")
    print(round(cleaned["TotalPrice"].sum(), 2))


if __name__ == "__main__":
    main()

