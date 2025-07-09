import json
from typing import Any, Dict, List, Union

from src.external_api import get_converter


def get_list_dict_finance_transactions(full_path: str) -> List[Dict[str, Any]]:
    """ Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, невалидный, содержит не список или не найден,
     функция возвращает пустой список. """

    try:
        # Открываем файл и читаем данные
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    except (json.JSONDecodeError, FileNotFoundError):
        # Если файл пустой или невалидный JSON
        return []


def get_amount_transactions_in_rub(transaction: Dict[str, Any]) -> Union[float, str]:
    """ Функция, принимает транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float."""

    amount = transaction.get('operationAmount').get('amount')
    currency = transaction.get('operationAmount').get('currency').get('code')

    if currency == 'RUB':
        return float(amount)
    elif currency in ['USD', 'EUR']:
        return get_converter(currency, str(amount))
    else:
        return 'Неизвестная валюта'

if __name__ == '__main__':
    transactions = get_list_dict_finance_transactions('../data/operations.json')
    print(get_amount_transactions_in_rub(transactions[1]))

transactions = get_list_dict_finance_transactions('../data/operations.json')
print(transactions)  # Выведет список транзакций или [] в случае ошибки
