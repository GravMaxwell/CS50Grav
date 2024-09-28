def main():
    # prompt user for input
    reply = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

    # format the user's input: lowercase and remove hyphens/whitespace
    user_reply = reply.lower().replace("-", " ").strip()

    # check if user input matches any of the correct answers
    match user_reply:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

main()

