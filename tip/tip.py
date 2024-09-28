# Given information
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# TO-DO No.1 : complete the remaining function
def dollars_to_float(d):
    # Tell python how we want format (remove leading "$")
    amtstring = d.replace("$", "")
    # convert string to float
    amtfloat = float(amtstring)
    return amtfloat
    print(dollars_to_float)


# TO-DO No.2: complete the remaining function
def percent_to_float(p):
    # tell python how we want to format (remove trailing " % ")
    nstring = p.replace("%", "")
    # convert string to float and divide by 100 to get decimal
    nfloat = float(nstring) / 100
    return nfloat
    print(percent_to_float)

# call back the main function so we get prompt at beginning
main()


