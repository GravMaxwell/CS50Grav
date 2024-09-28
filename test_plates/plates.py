# original plates.py code:
# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")

#     else:
#         print("Invalid")

# def is_valid(s):
#     # create a dictionary of validation fuctions
#     validations = {
#         "length": has_valid_length,
#         "start": starts_with_two_letters,
#         "characters": has_valid_characters,
#         "numbers": numbers_at_end
#     }

#     # loop through each validation function
#     for key, validation in validations.items():
#         if not validation(s):
#             return False
#     return True


# def has_valid_length(s):
#     return 2 <= len(s) <= 6

# def starts_with_two_letters(s):
#     return s[:2].isalpha()

# def has_valid_characters(s):
#     return s.isalnum()

# def numbers_at_end(s):
#     #find the first digit in the string
#     found_digit = False
#     for i, char in enumerate(s):
#         if char.isdigit():
#             if char == "0" and not found_digit:
#                 return False
#             found_digit = True
#             if not s[i:].isdigit():
#                 return False
#     return True  # this took me 4 hours to get right bc of indentation :( :(


# main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Create a dictionary of validation functions
    validations = {
        "length": has_valid_length,
        "start": starts_with_two_letters,
        "characters": has_valid_characters,
        "numbers": numbers_at_end
    }

    # Loop through each validation function
    for key, validation in validations.items():
        if not validation(s):

            return False
    return True

def has_valid_length(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return s[:2].isalpha()

def has_valid_characters(s):
    return s.isalnum()

def numbers_at_end(s):
    # Find the first digit in the string
    found_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and not found_digit:
                return False
            found_digit = True
            if not s[i:].isdigit():
                return False
    return True

if __name__ == "__main__":
    main()
