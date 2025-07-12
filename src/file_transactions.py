import csv
import pandas as pd


def get_transactions_file_csv(file_csv):
    """ Функция для считывания финансовых операций из CSV.
     Возвращает список словарей с транзакцией."""
    transactions = []
    try:
        with open(file_csv, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
        return transactions
    except FileNotFoundError:
        print(f"Ошибка: файл {file_csv} не найден! ")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def get_transactions_file_xlsx(file_xlsx):
    """ Функция для считывания финансовых операций из Excel.
    Возвращает список словарей с транзакцией."""

    # print(excel_transaction.shape)
    # print(excel_transaction.head())

    #transactions = []
    try:
        with open(file_xlsx, encoding='utf-8') as file:
            excel_transaction = pd.read_excel(file_xlsx)
            print(type(excel_transaction.to_dict("records")))
            return excel_transaction.to_dict("records")
            # for row in excel_transaction:
            #     transactions.append(row)

        # return transactions
    except FileNotFoundError:
        print(f"Ошибка: файл {file_xlsx} не найден! ")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []

# Пример использования
if __name__ == '__main__':
    # csv_transactions = get_transactions_file_csv("../transactions.csv")
    # print(csv_transactions)
    xlsx_transactions = get_transactions_file_xlsx("../transactions_excel.xlsx")
    print(xlsx_transactions)
