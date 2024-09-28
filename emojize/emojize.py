import emoji

def main():
    prompt = input("Input: ")
    emoji_str = emoji.emojize(prompt, language = "alias")
    print(f"Output: {emoji_str}")


main()
