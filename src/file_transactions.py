import csv


def get_transactions_file_csv(file_csv):
    """ Функция для считывания финансовых операций из CSV.
     Возвращает список словарей, где каждый словарь — одна транзакция."""
    transactions = []

    with open(file_csv, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

# Пример использования
if __name__ == '__main__':
    csv_transactions = get_transactions_file_csv("../transactions.csv")
    print(csv_transactions)

