# Applied Analytics: City Customer KPIs

This beginner-friendly project loads a small customer CSV file into SQLite and
calculates city-level KPIs with a parameterized query.

## Project files

- `data/raw/customers_raw.csv` — sample customer data.
- `data/db/analytics.db` — SQLite database created by the ETL script.
- `src/etl_load_sqlite.py` — loads the CSV into the `customers_raw` table.
- `src/kpi_city.py` — calculates city KPIs and demonstrates SQL injection protection.
- `tests/test_kpi_city.py` — tests normal results and an injection attempt.

## Run the project

Activate your existing `.venv`, then run these commands from the project folder:

```powershell
pip install -r requirements.txt
python src\etl_load_sqlite.py
python src\kpi_city.py
pytest
```

The KPI results include the customer count, average monthly spend, and churn
rate for the selected city. The injection-attempt input is treated as a literal
city name and returns no matching customers.