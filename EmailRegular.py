import re

def email(email):
    patt = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if  patt.search(email):
        print("The email address is in the expected format.")
    else:
        print("The email address is not in the expected format.")
