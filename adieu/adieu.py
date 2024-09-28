import sys
import inflect

def main():
    p = inflect.engine()
    names = []

    print("Enter names (press ctrl-d to finish):")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    if names:
        farewell = p.join(names)
        print(f"Adieu, adieu, to {farewell}")

main()
