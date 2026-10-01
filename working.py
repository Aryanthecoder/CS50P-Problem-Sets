import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    return f"{parse(h1, m1, p1)} to {parse(h2, m2, p2)}"

def parse(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if hour < 1 or hour > 12:
        raise ValueError
    if minute < 0 or minute > 59:
        raise ValueError

    # Convert hour
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
