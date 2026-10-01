def date_month_name(date):
    try:
        parts = date.split(" ")
        if len(parts) != 3:
            return None

        if "," not in parts[1]:
            return None
        month = parts[0]
        day = parts[1].replace(",", "")
        year = parts[2]
        months = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }

        if month not in months:
            return None
        month_num = months[month]
        day = int(day)
        year = int(year)
        if day < 1 or day > 31:
            return None
        return year, month_num, day
    except ValueError:
        return None
def date_numeric(date):
    try:
        parts = date.split("/")
        if len(parts) != 3:
            return None

        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

        if month < 1 or month > 12:
            return None
        if day < 1 or day > 31:
            return None

        return year, month, day
    except ValueError:
        return None
def main():
    while True:
        date = input("Date: ")
        result = date_month_name(date)
        if result:
            year, month, day = result
            break
        result = date_numeric(date)
        if result:
            year, month, day = result
            break
    print(f"{year}-{month:02d}-{day:02d}")
main()
