# Originial twttr.py code:
# def main():
#     # prompt the user for input
#     inpt = input("Input: ")

#     # Define vowels for python
#     vwls = "AaEeIiOoUu"

#     # setup an empty string to store result
#     otpt = ""

#     # iterate over each character in the users input
#     for char in inpt:
#         # check if character is not a vowel
#         if char not in vwls:
#             # add the character to the result string
#             otpt += char

#     # print the output / result
#     print(otpt)

# main()

# Reimplement from problem set #2
def main():
    # prompt the user for input
    inpt = input("Input: ")
    # print the output / result
    print(shorten(inpt))

def shorten(word):
    # Define vowels for python
    vwls = "AaEeiIOoUu"
    # setup an empty string to store result
    otpt = ""
    # iterate over each character in the users input
    for char in word:
        # check if character is not a vowel
        if char not in vwls:
            # add the character to the result string
            otpt += char
    # return the result string
    return otpt

if __name__ == "__main__":
    main()

