def main():
    # create a list of months
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()

        try:
            # try to convert the data into MM/DD/YY format
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:
                # try to convert the data into Month DD, YYYY format
                month_str, day_year = date.split(" ", 1)
                day, year = day_year.split(", ")
                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)

            # validate the date entered
            if 1 <= month <= 12 and 1 <= day <= 31:
                # format date as 'YYY-MM-DD'
                print(F"{year:04}-{month:02}-{day:02}")
                break
            else:
                raise ValueError

        except (ValueError, IndexError):
            print({date})

main()
