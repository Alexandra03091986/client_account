from unittest.mock import patch
from src.file_transactions import get_transactions_file_csv, get_transactions_file_xlsx, PATH_CSV, PATH_XLSX


# import pandas as pd

# Тест успешного чтения cvs
def test_get_transactions_file_csv() -> None:
    with patch("pandas.read_csv") as mock_read:
        mock_read.return_value.to_dict.return_value = {
                                                        'id': 650703.0,
                                                       'state': 'EXECUTED',
                                                       'date': '2023-09-05T11:30:32Z',
                                                       'amount': 16210.0,
                                                       'currency_name': 'Sol',
                                                       'currency_code': 'PEN',
                                                       'from': 'Счет 58803664561298323391',
                                                       'to': 'Счет 39745660563456619397',
                                                       'description': 'Перевод организации'
                                                       }
        result = get_transactions_file_csv(PATH_CSV)
        assert result == {
                            'id': 650703.0,
                           'state': 'EXECUTED',
                           'date': '2023-09-05T11:30:32Z',
                           'amount': 16210.0,
                           'currency_name': 'Sol',
                           'currency_code': 'PEN',
                           'from': 'Счет 58803664561298323391',
                           'to': 'Счет 39745660563456619397',
                           'description': 'Перевод организации'
                           }


# Тест успешного чтения xlsx
def test_get_transactions_file_xlsx() -> None:
    with patch("pandas.read_xlsx") as mock_read:
        mock_read.return_value.to_dict.return_value = {
                                                        'id': 650703.0,
                                                       'state': 'EXECUTED',
                                                       'date': '2023-09-05T11:30:32Z',
                                                       'amount': 16210.0,
                                                       'currency_name': 'Sol',
                                                       'currency_code': 'PEN',
                                                       'from': 'Счет 58803664561298323391',
                                                       'to': 'Счет 39745660563456619397',
                                                       'description': 'Перевод организации'
                                                       }
        result = get_transactions_file_xlsx(PATH_XLSX)
        assert result == {
                            'id': 650703.0,
                           'state': 'EXECUTED',
                           'date': '2023-09-05T11:30:32Z',
                           'amount': 16210.0,
                           'currency_name': 'Sol',
                           'currency_code': 'PEN',
                           'from': 'Счет 58803664561298323391',
                           'to': 'Счет 39745660563456619397',
                           'description': 'Перевод организации'
                           }
# 3. Тест, когда файл не найден
def test_get_transactions_file_csv_missing():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = get_transactions_file_csv("no_file.csv")
        assert result == []  # Проверим, что вернулся пустой список

# 4. Тест, когда файл не найден
def test_get_transactions_file_xlsx_missing():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = get_transactions_file_xlsx("no_file.xlsx")
        assert result == []  # Проверим, что вернулся пустой список


# from unittest.mock import patch, mock_open
# from src.file_transactions import get_transactions_file_csv  # Замени your_module на имя файла с функцией
# import pandas as pd
#
#
# # 1. Тест, когда файл читается нормально
# def test_good_file():
#     # Подготовим "фальшивый" файл с данными
#     fake_file_content = """id;state;amount
# 1;EXECUTED;100
# 2;CANCELED;200"""
#
#     # Скажем Python'у: "Когда кто-то откроет файл, верни вот эти данные"
#     with patch('builtins.open', mock_open(read_data=fake_file_content)):
#         # Скажем pandas: "Когда вызовут read_csv, верни вот такой словарь"
#         with patch('pandas.read_csv') as mock_read:
#             mock_read.return_value = pd.DataFrame([
#                 {"id": 1, "state": "EXECUTED", "amount": 100},
#                 {"id": 2, "state": "CANCELED", "amount": 200}
#             ])
#
#             # Вызовем нашу функцию
#             result = get_transactions_file_csv("test.csv")
#
#             # Проверим, что получили то, что ожидали
#             assert result == [
#                 {"id": 1, "state": "EXECUTED", "amount": 100},
#                 {"id": 2, "state": "CANCELED", "amount": 200}
#             ]
#
#
# # 2. Тест, когда файл не найден
# def test_missing_file():
#     # Скажем Python'у: "Когда кто-то попытается открыть файл, сделай вид, что его нет"
#     with patch('builtins.open', side_effect=FileNotFoundError):
#         result = get_transactions_file_csv("no_file.csv")
#         assert result == []  # Проверим, что вернулся пустой список
#
#
# # Запустим тесты
# test_good_file()
# test_missing_file()
# print("Все тесты прошли успешно!")