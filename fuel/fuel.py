def main():
    while True:
        try:
            # prompt the user to input a fraction
            fraction = input("Fraction: ")

            # split the fraction into x & y
            x, y = fraction.split("/")

            # convert x & y into integers
            x = int(x)
            y = int(y)

            # check if y is zero
            if y == 0:
                raise ZeroDivisionError

            # check if x > y
            if x > y:
                raise ValueError

            # calculate percentage of fuel
            percentage = (x / y) * 100

            # round percentage to the nearest
            percentage = round(percentage)

            # output the result based on the percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except (ValueError, ZeroDivisionError):
            # Prompt the user again in case of an error
            print("Invalid input. Please enter a valid fraction in the format X/Y.")

# Call the function to get the fuel percentage
main()
