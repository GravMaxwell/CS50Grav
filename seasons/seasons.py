from datetime import date, datetime
import sys
import inflect

def main():
    birthdate_str = input("Date of Birth: ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birthdate)
    minutes_in_words = convert_to_words(minutes)
    print(minutes_in_words + " minutes")

def calculate_minutes(birthdate):
    today = date.today()
    delta = today - birthdate
    total_minutes = delta.days * 24 * 60
    return total_minutes

def convert_to_words(minutes):
    p = inflect.engine()
    # Format the number with commas
    formatted_number = f"{minutes:,}"
    # Convert the formatted number to words
    words = p.number_to_words(formatted_number, andword="")
    # Capitalize the first word
    words = words.capitalize()
    return words

if __name__ == "__main__":
    main()
