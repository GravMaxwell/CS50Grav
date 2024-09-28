#import sys so we can access command line arguments
import sys
import random # in case user wants to choose a random font
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    # get list of available fonts
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        # choose random font if no font specified
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        if sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))

main()
