# BITCOIN TO THE MOON !!

import sys
import requests

def main():
    # check if user provided a 'command-line argument' of bitcoins, n
    if len(sys.argv) !=2:
        sys.exit("Missing command-line argument")

    # convert the argument as a float
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Query Coindesk API for the current Bitcoin price
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status() # DO NOT FORGET PARENTHESES :SAD FACE:
        data = response.json() # DO NOT FORGET PARENTHESES :SMILES:
        price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Failed to retrieve Bitcoin price")

    # calculate the total cost
    total_cost = num_bitcoins * price_per_bitcoin

    # output total cost formatted to four decimals and with thousands separator
    print(f"${total_cost:,.4f}")

main()
