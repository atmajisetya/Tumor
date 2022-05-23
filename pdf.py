from email.mime import base
from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()

list_img_path = []
base_dir = "runs\detect\exp30"
list_img = os.listdir(base_dir)
for x in list_img:
    list_img_path.append(base_dir + "\\" + x)

# print(list_img_path)
# print(list_img)

for i in list_img_path:
    pdf.image(i)

pdf.output("multi.pdf")
