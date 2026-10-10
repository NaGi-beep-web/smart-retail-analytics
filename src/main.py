
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "Online Retail.xlsx"

def main():
    if not DATA_PATH.exists():
        print(f"Dataset not found: {DATA_PATH}")
        return

    df = pd.read_excel(DATA_PATH)

    print("\n--- Dataset shape ---")
    print(df.shape)

    print("\n--- First 5 rows ---")
    print(df.head())

    print("\n--- Column names ---")
    print(df.columns.tolist())

    print("\n--- Data types and missing values ---")
    df.info()

    print("\n--- Missing values per column ---")
    print(df.isnull().sum())

    print("\n--- Duplicate rows ---")
    print(df.duplicated().sum())

if __name__ == "__main__":
    main()
