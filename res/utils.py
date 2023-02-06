import re

def is_mail_valid(mail: str) -> bool:
    mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(mail_regex, mail):
        return True
    return False

def is_birthday_valid(birthday: str) -> bool:
    birth_regex = r'\b[0-9]{1,2}(/|.)[0-9]{1,2}(/|.)[0-9]{4}\b'
    if re.fullmatch(birth_regex, birthday):
        return True
    return False

