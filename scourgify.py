import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            students = []

            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                students.append({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)

if __name__ == "__main__":
    main()
