import dashboard
import pytest
from unittest.mock import patch

@patch('dashboard.get_total_income')
def test_get_total_income(mock_get_income):
    mock_get_income.return_value = 2000


    result = dashboard.get_total_income(1)

    assert result == 2000

@patch('dashboard.get_total_spends')
def test_get_total_spends(mock_get_spends):
    mock_get_spends.return_value = 1500

    result2 = dashboard.get_total_spends(1)

    assert result2 == 1500

@patch('dashboard.get_total_income')
@patch('dashboard.get_total_spends')

def test_balance(mock_get_spends, mock_get_income):
    mock_get_income.return_value = 2000
    mock_get_spends.return_value = 1500

    income = dashboard.get_total_income(1)
    spends = dashboard.get_total_spends(1)
    balance = income - spends

    assert balance == 500
    print("\nSUCCESS!")