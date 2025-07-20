from typing import Any, Dict, List


def test_card_number_fixture(card_number: List[str]) -> None:
    # Проверяем, что фикстура возвращает список
    assert isinstance(card_number, list)
    # Проверяем, что все элементы в списке - строки
    assert all(isinstance(num, str) for num in card_number)
    # Проверяем конкретные значения
    assert "7000792289606361" in card_number
    assert "1111222233334444" in card_number


def test_account_number_fixture(account_number: List[str]) -> None:
    assert isinstance(account_number, list)
    assert all(isinstance(num, str) for num in account_number)
    assert "73654108430135874305" in account_number
    assert "1234" in account_number


def test_inform_card_fixture(inform_card: List[str]) -> None:
    assert isinstance(inform_card, list)
    assert all(isinstance(info, str) for info in inform_card)
    assert "Maestro 1596837868705199" in inform_card
    assert "Visa Platinum 8990922113665229" in inform_card


def test_inform_account_fixture(inform_account: List[str]) -> None:
    assert isinstance(inform_account, list)
    assert all(isinstance(info, str) for info in inform_account)
    assert "Счет 64686473678894779589" in inform_account
    assert "Счет 73654108430135874305" in inform_account


def test_formatting_date_fixture(formatting_date: List[str]) -> None:
    assert isinstance(formatting_date, list)
    assert all(isinstance(date_str, str) for date_str in formatting_date)
    assert "2024-03-11T02:26:18.671407" in formatting_date
    assert "2024-10-16T02:26:18.671407" in formatting_date


def test_transactions_fixture(transactions: List[Dict[str, Any]]) -> None:
    assert isinstance(transactions, list)
    assert all(isinstance(tr, dict) for tr in transactions)
    # Проверяем наличие основных ключей
    required_keys = ["id", "state", "date", "operationAmount", "description"]
    assert all(all(key in tr for key in required_keys) for tr in transactions)
    # Проверяем конкретную транзакцию
    assert any(tr["id"] == 895315941 for tr in transactions)
