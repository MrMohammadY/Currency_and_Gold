from currency import get_data_curr, create_data_curr, create_data_file_curr
from gold import get_data_go, create_data_go, create_data_file_go
from send_mail import create_body_sub
from config import rules
import os


def create_archives():
    """
    create archives file in directories
    :return:
    """
    cwd = os.getcwd()
    path_currency = f'{cwd}/archive_currency'
    path_gold = f'{cwd}/archive_gold'
    try:
        os.mkdir(path_currency)
        os.mkdir(path_gold)
    except OSError:
        pass


def run():
    """
    make data of currency file and gold file and check config file
    and do sendmail and insert data in files
    :return:
    """
    create_archives()

    currency = create_data_curr(get_data_curr())
    gold = create_data_go(get_data_go())

    if rules['archive']:
        create_data_file_curr(currency[0], currency[1])
        create_data_file_go(gold[0], gold[1])

    if rules['send_mail']:
        create_body_sub(currency, gold)


if __name__ == '__main__':
    run()
