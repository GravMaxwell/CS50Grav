import sys

def main():
    # check for correct number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python lines.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # check if file has python extension
    if not filename.endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File does not exist")

    # count lines of code in python file
    linecount = countlines(lines)
    print(linecount)

def countlines(lines):
    count = 0
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line.startswith("#") or stripped_line == "":
            continue
        count += 1
    return count

if __name__ == "__main__":
    main()
