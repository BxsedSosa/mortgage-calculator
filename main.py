'''Imported libraries'''
import json
import os

from pyfiglet import Figlet

USER_LANGUAGES = ['en', 'es']

with open("text.json", "r") as f:
    MSG = json.load(f)

def clear():
    '''Clears console from clutter'''
    os.system('clear')

def welcome():
    '''Welcome sign'''
    sign = Figlet(font='slant')
    print(sign.renderText('Welcome'))
    print('-----------------------------------------------')

def mortgage_sign():
    '''Mortgage sign'''
    sign = Figlet(font='slant')
    print(sign.renderText(MSG[language]['mortgage']))
    print('-----------------------------------------------')

def prompt(text):
    '''Adds Arrows to beginning of every output from code'''
    return f'{MSG['arrow']} {text}'

def valid_number(num_str):
    '''Checks if user input number is valid'''
    try:
        float(num_str)
    except ValueError:
        return True

    return False

def valid_language():
    '''Checks if user input is a valid entry for language'''
    selected_language = input(prompt(MSG['en']['question']['select-lang'])).lower()

    while selected_language not in USER_LANGUAGES:
        selected_language = input(prompt(MSG['en']['error']['select-lang'])).lower()

    return selected_language

def user_numbers(text):
    '''This is where user will be asked for a input of a number'''
    edge_cases = ['inf', '-inf', 'nan', '-nan']
    user_number = input(prompt(MSG[language]['question'][text])).lower()

    while user_number in edge_cases:
        user_number = input(prompt(MSG[language]['error'][text])).lower()

    while valid_number(user_number):
        user_number = input(prompt(MSG[language]['error'][text])).lower()

    return  user_number

def loan_amnt(text):
    '''Asking user for loan amount'''
    loan_amount = user_numbers(text)
    return float(loan_amount)

def annual_rate(text):
    '''Asking user for loan rate'''
    loan_apr = user_numbers(text)
    return (float(loan_apr)* .01) / 12

def loan_dur(text):
    '''Asking user for loan duration'''
    loan_duration = user_numbers(text)
    return float(loan_duration) * 12

def payment_calculation(amount, interest, duration):
    '''Does the calcuation for payments'''
    if interest == 0:
        result = amount / duration
        return round(result, 2)

    result = amount * (interest / (1 - (1 + interest) ** (-duration)))
    return round(result, 2)

def retry():
    '''Gives option to retry another calcuation'''
    valid_answer = ['y', 'yes', 'n', 'no']
    user_answer = input(prompt(MSG[language]['question']['retry'])).lower()

    while user_answer not in valid_answer:
        user_answer = input(prompt(MSG[language]['error']['retry'])).lower()

    return user_answer

def main():
    '''Main function'''
    loan_amount = loan_amnt('amount')
    loan_interest_rate = annual_rate('apr')
    loan_duration = loan_dur('duration')
    result = payment_calculation(loan_amount, loan_interest_rate, loan_duration)
    print(f'{prompt(MSG[language]['payment'])} {result}\n')

clear()
VALID_RETRY = ['y', 'yes']
welcome()
language = valid_language()

while True:
    clear()
    mortgage_sign()
    main()

    answer = retry()
    if answer not in VALID_RETRY:
        break
