import requests

def convert_currency(amount, from_currency, to_currency):
    
    
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        # GET request sent to the API endpoint
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            exchange_rate = data['rates'][to_currency]

            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            print("Failed to retrieve exchange rates. Please try again later.")

    except requests.exceptions.RequestException as e:
        print("An error occurred during the API request:", e)

    return None

amount = input('Enter amount: ')
from_currency = input('Enter currency abbreviation: ')
to_currency = input('Enter destination currency abbreviation: ')

converted_amount = convert_currency(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
