def main():
    # prompt user for input
    greeting = input("Greeting: ")

    # format user input as needed to match with answer
    reply = greeting.strip()

    # respond with bank balance based on user input
    match greeting:
        case "Hello" | "Hello, Newman":
            print("$0")
        case "Hi" | "How you doing?" | "Hey" | "How's it going?":
            print("$20")
        case "What's happening?" | "What's up?":
            print("$100")

        case _:
            print("$0")

main()
