# Write a function to do the math for user
def calculate(expression):
    # (RE: QUESTION HINT) split input string into components x,y,z
    x, y, z = expression.split(" ")

    # format x & z as integers
    x = int(x)
    z = int(z)

    #format y as an operator and perform respective mathematical operation
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    # return result and formatted to 1 decimal place
    return f"{result:.1f}"

def main():
    # ask user for a mathematical expression
    expression = input("Expression: ")

    # do some math and print result
    print (calculate(expression))

main()
