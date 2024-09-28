# # original bank.py code:
# def main():
#     # prompt user for input
#     greeting = input("Greeting: ")

#     # format user input as needed to match with answer
#     reply = greeting.strip()

#     # respond with bank balance based on user input
#     match greeting:
#         case "Hello" | "Hello, Newman":
#             print("$0")
#         case "Hi" | "How you doing?" | "Hey" | "How's it going?":
#             print("$20")
#         case "What's happening?" | "What's up?":
#             print("$100")

#         case _:
#             print("$0")

# main()

# reimplement bank.py from Problem Set 1

def main():
    # prompt user for input
    greeting = input("Greeting: ")
    # print the output / result
    print(value(greeting))

def value(greeting):
    # Convert greeting to lowercase for case-insensitive comparison
    greeting = greeting.lower()
    # Check the conditions and return the corresponding value
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
