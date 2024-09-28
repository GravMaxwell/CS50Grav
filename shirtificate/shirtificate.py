from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

def main():
    name = input("Name: ")

    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # Add the shirt image
    pdf.image("shirtificate.png", x=0, y=60, w=210)

    # Add the name on top of the shirt
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 200, name, 0, 1, "C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
