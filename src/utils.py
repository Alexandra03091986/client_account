import os
import json


def get_list_dict_finance_transactions(full_path):
    """ Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список. """

    try:
        # Проверяем, существует ли файл
        if not os.path.exists(full_path):
            return []

        # Открываем файл и читаем данные
        with open(full_path, 'r', encoding='utf-8') as f:
            list_dict = json.load(f)

            # Проверяем, что данные - это список
            if isinstance(list_dict, list):
                amount_list = []
                for transaction in list_dict:
                    if 'amount' in transaction:
                        amount_list.append(transaction['amount'])
                return amount_list
            else:
                return []

    except (json.JSONDecodeError, FileNotFoundError):
        # Если файл пустой или невалидный JSON
        return []


transactions = get_list_dict_finance_transactions('../data/operations.json')
print(transactions)  # Выведет список транзакций или [] в случае ошибки


