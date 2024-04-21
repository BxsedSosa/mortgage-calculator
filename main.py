from enum import Flag
import json

with open("text.json", "r") as f:
    MSG = json.load(f)

def prompt(text):
    return f'{MSG['arrow']} {text}'

def valid_number(amount):
    try:
        float(amount)
    except ValueError:
        return True
    
    return False 

def user_numbers(text):
    user_number = input(prompt(MSG[language]['question'][text]))

    while valid_number(user_number):
        user_number = input(prompt(MSG[language]['error'][text]))

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

def main():
    LOAN_AMOUNT = loan_amnt('amount')
    LOAN_INTEREST_RATE = annual_rate('apr')
    LOAN_DURATION = loan_dur('duration')
    print(payment_calculation(LOAN_AMOUNT, LOAN_INTEREST_RATE, LOAN_DURATION))

language = 'en'

main()
