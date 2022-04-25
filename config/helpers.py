import re

regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

def check(email):
    if re.search(regex, email):
        return True
    else:
        return False