"""Load the sample customer CSV into a SQLite database."""

from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "customers_raw.csv"
DB_PATH = PROJECT_ROOT / "data" / "db" / "analytics.db"


def load_csv_to_sqlite(
    csv_path: Path = CSV_PATH,
    db_path: Path = DB_PATH,
) -> None:
    """Replace the customers_raw table with rows from the CSV file."""
    customers = pd.read_csv(csv_path)
    expected_columns = ["customer_id", "city", "monthly_spend", "churned"]
    customers = customers[expected_columns]

    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as connection:
        connection.execute("DROP TABLE IF EXISTS customers_raw")
        connection.execute(
            """
            CREATE TABLE customers_raw (
                customer_id INTEGER,
                city TEXT,
                monthly_spend REAL,
                churned INTEGER
            )
            """
        )
        customers.to_sql("customers_raw", connection, if_exists="append", index=False)


if __name__ == "__main__":
    load_csv_to_sqlite()
    print(f"Loaded {CSV_PATH} into {DB_PATH}")
