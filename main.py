import re

def validate_phone_number(phone_number):
    pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

phone_number = "+7-997)5523457"
if validate_phone_number(phone_number):
    print(f"{phone_number} is a valid phone number")
else:
    print(f"{phone_number} is not a valid phone number")

