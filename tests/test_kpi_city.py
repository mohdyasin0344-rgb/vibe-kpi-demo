"""Tests for the city KPI query."""

import pytest

from src import etl_load_sqlite, kpi_city


@pytest.fixture
def prepared_database(tmp_path, monkeypatch):
    """Create a fresh sample database for each test."""
    db_path = tmp_path / "analytics.db"
    etl_load_sqlite.load_csv_to_sqlite(db_path=db_path)
    monkeypatch.setattr(kpi_city, "DB_PATH", db_path)


def test_city_kpi_returns_mumbai_results(prepared_database):
    result = kpi_city.city_kpi("Mumbai")

    assert result["customer_count"] == 3
    assert result["average_monthly_spend"] == pytest.approx(
        (2500.00 + 1800.50 + 3200.75) / 3
    )
    assert result["churn_rate_percent"] == pytest.approx(100 / 3)


def test_city_kpi_does_not_allow_sql_injection(prepared_database):
    result = kpi_city.city_kpi("Mumbai' OR 1=1 --")

    assert result == {
        "customer_count": 0,
        "average_monthly_spend": None,
        "churn_rate_percent": None,
    }
