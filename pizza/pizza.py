import sys
import csv
from tabulate import tabulate


def main():
    # check number of command line arguments (similiar to problem #1 lines.py)
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # check if file has the correct extension .csv
    if not filename.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [row for row in reader]

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    # print the table
    print(tabulate(rows, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
