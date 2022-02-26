# Currency Converter using API call
# Author : T.K.Santhosh
# Created on : Feb 26, 2022
import requests


class CurrencyConverter:
    @staticmethod
    def welcome() -> None:
        """Displays a welcome message to the user to understand how to use"""
        print("WELCOME TO CURRENCY CONVERTER")
        print("-" * 33)
        print("NOTE : You should enter the acronym of the currency to work fine.\n")

    @staticmethod
    def display_currency() -> None:
        """
        Makes an API call and get all currencies available.
        Display it to the user the acronym and definition of the acronym.
        """
        data = requests.get("https://api.fastforex.io/currencies?api_key=572de19de9-0000d3204a-r7x0e9")
        data = data.json()
        for currency in data['currencies'].items():
            currency_name, definition = currency
            print("{0} - {1}".format(currency_name, definition))

    def get_values(self) -> str:
        """Get required input values from the user to process the next API call"""
        print("\n")
        currency_form = input("From : ").upper()
        currency_to = input("To : ").upper()
        amount = float(input("How much you want to covert from {0} to {1} : ".format(currency_form, currency_to)))
        print("Converting...")

        return self.convert_currency(currency_form, currency_to, amount)

    def convert_currency(self, from_name, to_name, amount_to_convert) -> str:
        """
        Makes an API call with the user input from the `get_values()` method.
        Args:
            from_name: The name of the currency.
            to_name:  Name of the currency to be converted.
            amount_to_convert: How much to convert (float).

        Returns: A formatted string with appropriate values.
        """
        URL = "https://api.fastforex.io/convert?from={0}&to={1}&amount={2}&api_key=572de19de9-0000d3204a-r7x0e9".format(
            from_name, to_name, amount_to_convert)

        # Making API call to get converted currency value
        return_value = requests.get(URL)
        data = return_value.json()
        currency_value = data["result"]
        result = "The current value of {0} to {1} is {2}".format(from_name, to_name, currency_value[to_name])

        return result


cc = CurrencyConverter()
cc.welcome()
cc.display_currency()
print(cc.get_values())
