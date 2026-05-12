import requests

amount = input("Введіть суму: ")
from_currency = input("Введіть валюту (наприклад UAH): ").upper()
to_currency = input("В яку валюту конвертувати (наприклад USD): ").upper()

url = f"https://api.frankfurter.app/v2/rates?amount={amount}&from={from_currency}&to={to_currency}"

print(url)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    result = data["rates"][to_currency]

    print("Результат:")
    print(amount, from_currency, "=", result, to_currency)

else:
    print("Помилка!")
    print("Код помилки:", response.status_code)
