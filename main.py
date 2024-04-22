'''Imported libraries'''
import json
import os

from pyfiglet import Figlet

USER_LANGUAGES = ['en', 'es']
VALID_RETRY = ['y', 'yes']

with open("text.json", "r", encoding='utf-8') as f:
    MSG = json.load(f)

def clear_console():
    '''Clears console from clutter'''
    os.system('clear')

def display_welcome():
    '''Welcome sign'''
    sign = Figlet(font='slant')
    print(sign.renderText('Welcome'))
    print('-----------------------------------------------')

def display_mortgage_sign():
    '''Mortgage sign'''
    sign = Figlet(font='slant')
    print(sign.renderText(MSG[language]['mortgage']))
    print('-----------------------------------------------')

def prompt(text):
    '''Adds Arrows to beginning of every output from code'''
    return f'{MSG['arrow']} {text}'

def validate_number(num_str):
    '''Checks if user input number is valid'''
    try:
        float(num_str)
    except ValueError:
        return True

    return False

def validate_language():
    '''Checks if user input is a valid entry for language'''
    selected_language = input(prompt(MSG['en']['question']['select-lang'])).lower()

    while selected_language not in USER_LANGUAGES:
        selected_language = input(prompt(MSG['en']['error']['select-lang'])).lower()

    return selected_language

def ask_user_number(text):
    '''This is where user will be asked for a input of a number'''
    edge_cases = ['inf', '-inf', 'nan', '-nan']
    user_number = input(prompt(MSG[language]['question'][text])).lower()

    while user_number in edge_cases:
        user_number = input(prompt(MSG[language]['error'][text])).lower()

    while validate_number(user_number):
        user_number = input(prompt(MSG[language]['error'][text])).lower()

    return  user_number

def ask_loan_amnt(text):
    '''Asking user for loan amount'''
    loan_amount = ask_user_number(text)
    return float(loan_amount)

def ask_annual_rate(text):
    '''Asking user for loan rate'''
    loan_apr = ask_user_number(text)
    return (float(loan_apr)* .01) / 12

def ask_loan_dur(text):
    '''Asking user for loan duration'''
    loan_duration = ask_user_number(text)
    return float(loan_duration) * 12

def calculate_payment(amount, interest, duration):
    '''Does the calcuation for payments'''
    if interest == 0:
        result = amount / duration
        return round(result, 2)

    result = amount * (interest / (1 - (1 + interest) ** (-duration)))
    return round(result, 2)

def ask_retry():
    '''Gives option to retry another calcuation'''
    valid_answer = ['y', 'yes', 'n', 'no']
    user_answer = input(prompt(MSG[language]['question']['retry'])).lower()

    while user_answer not in valid_answer:
        user_answer = input(prompt(MSG[language]['error']['retry'])).lower()

    return user_answer

def main():
    '''Main function'''
    loan_amount = ask_loan_amnt('amount')
    loan_interest_rate = ask_annual_rate('apr')
    loan_duration = ask_loan_dur('duration')
    result = calculate_payment(loan_amount, loan_interest_rate, loan_duration)
    print(f'{prompt(MSG[language]['payment'])}{result}\n')

clear_console()
display_welcome()
language = validate_language()

while True:
    clear_console()
    display_mortgage_sign()
    main()

    answer = ask_retry()
    if answer not in VALID_RETRY:
        break
