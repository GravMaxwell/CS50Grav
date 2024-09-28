import re
import sys

def main():
    # Prompt for input when running the script directly
    s = input("Hours: ")
    try:
        print(convert(s))
    except ValueError:
        print("ValueError")
        sys.exit(1) # added sys.exit to address exit code errors in check50

def convert(s):
    # Regular expression to match time formatting
    pattern = r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$'
    match = re.match(pattern, s)
    if not match:
        raise ValueError

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Convert starting time
    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute else 0

    # Add validation to check for invalid minute inputs
    if start_minute >= 60:
        raise ValueError
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    # Convert finish/end time
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute else 0
    if end_minute >= 60:
        raise ValueError
    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    # Format times with leading zeroes [24-hr time HH:MM]
    start_time = f"{start_hour:02}:{start_minute:02}"
    end_time = f"{end_hour:02}:{end_minute:02}"

    return f"{start_time} to {end_time}"

if __name__ == "__main__":
    main()
