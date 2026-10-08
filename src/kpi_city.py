"""Calculate customer KPIs for one city from the SQLite database."""

from pathlib import Path
import sqlite3


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "db" / "analytics.db"


def city_kpi(city: str) -> dict[str, int | float | None]:
    """Return customer count, average spend, and churn rate for a city."""
    with sqlite3.connect(DB_PATH) as connection:
        row = connection.execute(
            """
            SELECT
                COUNT(*) AS customer_count,
                AVG(monthly_spend) AS average_monthly_spend,
                AVG(churned) * 100.0 AS churn_rate_percent
            FROM customers_raw
            WHERE city = ?
            """,
            (city,),
        ).fetchone()

    result = {
        "customer_count": row[0],
        "average_monthly_spend": row[1],
        "churn_rate_percent": row[2],
    }
    print(f"City KPI for {city!r}: {result}")
    return result


if __name__ == "__main__":
    city_kpi("Mumbai")
    city_kpi("Mumbai' OR 1=1 --")
