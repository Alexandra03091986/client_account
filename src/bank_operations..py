import re


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """  Фильтрует список словарей с данными о банковских операциях, оставляя только те,
    в описании которых встречается заданная строка. """
    try:
        result = []
        for operation in data:
            if 'description' in operation and re.search(search, operation['description'], re.IGNORECASE):
                result.append(operation)
        return result
    except re.error:
        return []


if __name__ == '__main__':
    operations = [
        {"amount": 500, "description": "Оплата кафе"},
        {"amount": 1000, "description": "Перевод другу"},
        {"amount": 300, "description": "Покупка в МАГАЗИНЕ"},
    ]
    found = process_bank_search(operations, "маг")
    print(found)

