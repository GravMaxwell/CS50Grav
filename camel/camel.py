def camelsnake(camel_case):
    # empty string to store the 'snake_case' result
    snake_case = ""
    # iterate over each character in the camel_case string
    for char in camel_case:
        # check if the current character is capitalized/uppercase
        if char.isupper():
            # if capitilized, add an underscore "_" and replace capital letter with lowercase
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    # return the snake_case string
    return snake_case


def main():
    camel_case = input("camelCase: ")

    snake_case = camelsnake(camel_case)

    print("snake_case:" , snake_case)

main()

