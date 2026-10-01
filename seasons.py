import sys
from datetime import date
import inflect


def main():
    birth_date = input("Date of Birth: ")
    minutes = get_minutes(birth_date)
    print(minutes_to_words(minutes))


def get_minutes(birth_date):
    try:
        year, month, day = birth_date.split("-")
        born = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    return (today - born).days * 24 * 60


def minutes_to_words(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
