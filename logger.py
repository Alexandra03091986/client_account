import logging


""" Настраиваем логгер """
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

""" Создаем хендлер для вывода в файл """
file_handler = logging.FileHandler('logs/app.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

