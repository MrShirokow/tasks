"""
https://youtu.be/oka2Z05bsuc?t=391
"""


def convert_email(email: str) -> str:
    email = email.lower()
    user_name, domain = email.split('@')
    return f'{user_name}@ya.ru' if domain == 'yandex.ru' else email


assert convert_email('yandex@yandex.ru') == 'yandex@ya.ru'
assert convert_email('yandex.ru@gmail.com') == 'yandex.ru@gmail.com'
assert convert_email('yandex.ru@ya.ru') == 'yandex.ru@ya.ru'
assert convert_email('google@gmail.com') == 'google@gmail.com'
assert convert_email('worker@yandex-team.ru') == 'worker@yandex-team.ru'

print('Done')
