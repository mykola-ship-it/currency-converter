import requests

S = input("Введіть суму: ")
Currency = input("Введіть валюту: ")
ToCurrency = input("В яку валюту конвертувати: ")

Url = f"https://api.frankfurter.app/latest?amount={S}&from={Currency}&to={ToCurrency}"

response = requests.get(Url)

if response.status_code == 200:
    data = response.json()

    result = data["rates"][ToCurrency]

    print("Результат:")
    print(S, Currency, "=", result, ToCurrency)

else:
    print("Помилка!")
    print("Код помилки:", response.status_code)