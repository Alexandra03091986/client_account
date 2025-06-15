from typing import Iterable


def filter_by_state(list_of_dictionaries: list, state: str = 'EXECUTED') -> Iterable:
    """ Функция, которая принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те
    словари, у которых ключ state соответствует указанному значению. """
    filtered_list = []
    for dictionary in list_of_dictionaries:
        if dictionary['state'] == state:
            filtered_list.append(dictionary)
    return filtered_list


def sort_by_date(list_of_dictionaries: Iterable, decreasing: bool = True) -> Iterable:
    """ Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать
     новый список, отсортированный по дате (date)."""
    sorted_list_by_data = sorted(list_of_dictionaries, key = lambda list_of_dic: int(list_of_dic['date'].split('T')[0].replace('-','')), reverse=decreasing)
    return sorted_list_by_data


if __name__ == '__main__':
    list_of_dictionaries = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    print(filter_by_state(list_of_dictionaries))

    print(sort_by_date(list_of_dictionaries))
