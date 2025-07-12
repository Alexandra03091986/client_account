from src.masks import get_mask_account, get_mask_card_number
from src.utils import get_amount_transactions_in_rub, get_list_dict_finance_transactions
from config import PATH_JSON

result = get_mask_card_number("7000792289606361")
print(result)

result = get_mask_account("73654108430135874305")
print(result)

transactions = get_list_dict_finance_transactions(PATH_JSON)
print(transactions)  # Выведет список транзакций или [] в случае ошибки
print(get_amount_transactions_in_rub(transactions[2]))
