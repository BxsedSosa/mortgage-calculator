import os
import json

USER_LANGUAGES = ['en', 'es']

with open("text.json", "r") as f:
    MSG = json.load(f)

def clear():
    os.system('clear')

def prompt(text):
    return f'{MSG['arrow']} {text}'

def valid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return True
    
    return False 

def valid_language():
    selected_language = input(prompt(MSG['en']['question']['select-lang'])).lower()

    while selected_language not in USER_LANGUAGES:
        selected_language = input(prompt(MSG['en']['error']['select-lang'])).lower()

    return selected_language

def user_numbers(text):
    EDGE_CASES = ['inf', '-inf', 'nan', '-nan']
    user_number = input(prompt(MSG[language]['question'][text])).lower()

    while user_number in EDGE_CASES:
        user_number = input(prompt(MSG[language]['error'][text])).lower()

    while valid_number(user_number):
        user_number = input(prompt(MSG[language]['error'][text])).lower()

    return  user_number

def loan_amnt(text):
    loan_amount = user_numbers(text)
    return float(loan_amount)

def annual_rate(text):
    loan_apr = user_numbers(text)
    return (float(loan_apr)* .01) / 12

def loan_dur(text):
    loan_duration = user_numbers(text)
    return float(loan_duration) * 12

def payment_calculation(amount, interest, duration):
    result = amount * (interest / (1 - (1 + interest) ** (-duration))) 
    return round(result, 2)

def retry():
    answer = ['y', 'yes', 'n', 'no']
    user_answer = input(prompt(MSG[language]['question']['retry'])).lower()

    while user_answer not in answer:
        user_answer = input(prompt(MSG[language]['error']['retry'])).lower()

    return user_answer

def main():
    LOAN_AMOUNT = loan_amnt('amount')
    LOAN_INTEREST_RATE = annual_rate('apr')
    LOAN_DURATION = loan_dur('duration')
    print(payment_calculation(LOAN_AMOUNT, LOAN_INTEREST_RATE, LOAN_DURATION))


while True:
    clear()
    language = valid_language()
    VALID_RETRY = ['y', 'yes']
    main()

    answer = retry()
    if answer in VALID_RETRY:
        continue
    else:
        break
