URL_CURRENCY = 'https://hamyarandroid.com/api?t=currency'
URL_GOLD = 'https://hamyarandroid.com/api?t=gold'

rules = {
    'archive': True,
    'send_mail': {
        'enable': True,
        'sender': None,  # ==> type str and type mail like : 'm.sender@gmail.com'
        'sender_pass': None,  # ==> type str and type pass like: '1234'
        'receiver': None  # list of receiver like: ['ali@gmail.com', mmd@gmail.com']
    },
    'currency': {
        'which_currency': ['دینار کویت', 'روبل روسیه', 'یورو',
                           'دلار کانادا', 'دلار استرالیا', 'دلار']
    },
    'gold': {
        'which_gold': ['سکه بهار آزادی', 'ربع سکه', 'سکه گرمی',
                       'سکه امامی', 'نیم سکه', 'انس طلا', 'انس نقره']
    }
}
