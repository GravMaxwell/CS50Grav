import sys
import csv

def main():
    # check for correct # of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py <input_csv> <output_csv>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]


    # check if file has the correct extension .csv
    if not input_csv.endswith(".csv") or not output_csv.endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    try:
        with open(input_csv, "r") as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                last, first = row["name"].split(", ")
                rows.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        print(f"Could not read {input_csv}")
        sys.exit(1)

    # write the csv output file (refer to lecture 6 video)
    with open(output_csv, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()
