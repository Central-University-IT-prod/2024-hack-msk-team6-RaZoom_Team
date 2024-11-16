from random import choices
import string

def generate_email():
    return f"{''.join(choices(string.ascii_letters, k=10))}@mail.ru"

