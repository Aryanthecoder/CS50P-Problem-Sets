import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        count = count_lines(filename)
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(filename):
    count = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            count += 1

    return count


if __name__ == "__main__":
    main()
