def main():
    time = input("What time is it? ")
    dec_time = convert(time)

    if 7 <= dec_time <= 8:
        print("breakfast time")
    elif 12 <= dec_time <= 13:
        print("lunch time")
    elif 18 <= dec_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes =float(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
