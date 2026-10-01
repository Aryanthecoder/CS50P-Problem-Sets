import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_ext = (".jpg", ".jpeg", ".png")
    if not input_file.lower().endswith(valid_ext):
        sys.exit("Invalid input")
    if not output_file.lower().endswith(valid_ext):
        sys.exit("Invalid output")

    if input_file.split(".")[-1].lower() != output_file.split(".")[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("File does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size

    image = ImageOps.fit(image, size)

    image.paste(shirt, mask=shirt)

    image.save(output_file)

if __name__ == "__main__":
    main()
