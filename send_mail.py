import smtplib
from email.mime.text import MIMEText
from config import rules


def create_body_sub(currency, gold):
    sub = f'قیمت ارز و طلا {currency[1]}'
    body_currency = f'Last Update: {currency[2]}\n'
    body_gold = f'\nLast Update: {gold[2]}\n'

    for cu in currency[0]:
        body_currency += f'Name: {cu["nameFa"].ljust(15)}\t\t Price: {cu["price"]}\n'

    for go in gold[0]:
        body_gold += f'Name: {go["name"].ljust(15)}\t\t Price: {go["price"]}\n'

    return send_mail(sub, body_currency + body_gold)


def send_mail(subject, body):
    if (
            rules['send_mail']['sender'] or
            rules['send_mail']['receiver'] or
            rules['send_mail']['sender_pass']
    ) is None:
        print('Oops! please go in config file and edit send_mail params')

    else:
        for receiver in rules['send_mail']['receiver']:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = rules['send_mail']['sender']
            msg['To'] = receiver

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(rules['send_mail']['sender'],
                    rules['send_mail']['sender_pass'])
            s.sendmail(msg['From'], msg['To'], msg.as_string())
            s.quit()
