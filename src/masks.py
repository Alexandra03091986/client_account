from mypy.types import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """ Функция маскировки номера банковской карты """
    mask_card_number = card_number.replace(" ", "")[:4] + ' ' + card_number.replace(" ", "")[4:6] + '** **** ' + card_number[-4:]
    return mask_card_number


def get_mask_account(number_account: Union[str]) -> str:
    """ Функция маскировки номера банковского счета """
    mask_account = '**' + number_account[-4:]
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number('7000792289606361'))

if __name__ == "__main__":
    print(get_mask_account('73654108430135874305'))
