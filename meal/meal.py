def main():
    # Ask user what time it is
    time = input("What time is it? ")

    # convert time to a float value representing hours
    flotime = convert(time)

    # determine meal time based on converted time
    if 7 <= flotime <= 8:
        print("breakfast time")
    elif 12 <= flotime <= 13:
        print("lunch time")
    elif 18 <= flotime <= 19:
        print("dinner time")

def convert(time):
    # separate time into hours and minutes
    hours, minutes = time.split(":")

    # format hours and minutes as integers
    hours = int(hours)
    minutes = int(minutes)

    # reformat time to float value representing hours
    return hours + minutes / 60


if __name__ == "__main__":
    main()
