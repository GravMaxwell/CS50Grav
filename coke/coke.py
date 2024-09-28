def main():
    # list the amount due
    amount_due = 50

    # loop function until amount is zero or less
    while amount_due > 0:
        print(f"Amount Due: {amount_due}" )

        # prompt the user to insert a coin (format coin input as an integer)
        coin = int(input("Insert coins:"))

        # check for the right currency
        if coin in [25, 10, 5]:
            # subctract the coin amount, from the amount due
            amount_due -= coin



        # calculate change owed
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")


main()
