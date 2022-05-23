from fpdf import FPDF


# def pdf_convert():
#     pdf = FPDF()
#     pdf.set_margins(left=10, top=15, right=10)
#     pdf.add_page()
#     pdf.set_font("Arial", size=15)

#     # create a cell
#     pdf.cell(200, 10, txt="Atmaji Setya Pangestu", ln=1, align='C')
#     pdf.image("C:\Capstone\Tumor\runs\detect\exp30\y94.jpg")

#     # save the pdf with name .pdf
#     pdf.output("GFG.pdf")


# pdf_convert()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)
# create a cell
pdf.cell(200, 10, txt="Atmaji Setya",
         ln=1, align='C')
# add another cell
pdf.cell(200, 10, txt="Laki-Laki",
         ln=2, align='C')

# path image harus relative path
pdf.image('runs\detect\exp3\y94.jpg')

# save the pdf with name .pdf
pdf.output("GFG.pdf")
