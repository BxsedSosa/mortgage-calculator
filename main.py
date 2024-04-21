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
def temp():
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
