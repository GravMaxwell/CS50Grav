# create the first function - tell python how we want to convert user inputs
def emoconvert(input):
    # create a case for each emoticon " :( " &  " :) "
    input = input.replace(":)", "🙂")
    input = input.replace(":(", "🙁")
    return input

# create second funtion - prompt user for inputs
def main():
    prompt = input("Say something happy or sad plz")
    # print user prompt with modified emojis using emoconvert function above
    print(emoconvert(prompt))

# call back the main function so we get a prompt at the beginning!
main()
