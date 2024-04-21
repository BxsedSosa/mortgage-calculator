import json

with open("text.json", "r") as f:
    MSG = json.load(f)

def prompt(text):
    return f'{MSG['arrow']} {text}'

def valid_number(amount):
    try:
        int(amount)
    except ValueError:
        return True
    
    return False 

language = 'en'

print(prompt(MSG[language]['welcome']))
    
print(prompt(MSG[language]['loan-amount']))
loan_amount = input()

while valid_number(loan_amount):
    print(prompt(MSG[language]['error-amount']))
    loan_amount = input()

print(prompt(MSG[language]['loan-apr']))
loan_apr = input()

while valid_number(loan_apr):
    print(prompt(MSG[language]['error-apr']))
    loan_apr = input()

print(prompt(MSG[language]['loan-duration']))
loan_duration = input()

while valid_number(loan_duration):
    print(prompt(MSG[language]['error-duration']))
    loan_duration = input()

MONTHLY_INTEREST_RATE = (float(loan_apr) * .01) / 12
MONTHLY_DURATION = float(loan_duration) * 12

MONTHLY_PAYMENT = float(loan_amount) * (MONTHLY_INTEREST_RATE / (1 - (1 + MONTHLY_INTEREST_RATE) ** (-MONTHLY_DURATION)))


print(round(MONTHLY_PAYMENT, 2))
