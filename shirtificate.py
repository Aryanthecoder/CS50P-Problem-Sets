from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C")

    image_width = 150
    x = (210 - image_width) / 2
    y = 40
    pdf.image("shirtificate.png", x=x, y=y, w=image_width)

   
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(x, y + 60)
    pdf.cell(image_width, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
