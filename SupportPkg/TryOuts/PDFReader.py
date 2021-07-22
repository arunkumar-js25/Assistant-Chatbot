from pdfminer.high_level import extract_text
from wand.image import Image  
#ImageMagick - http://docs.wand-py.org/en/latest/guide/install.html
import os

#https://theautomatic.net/2020/01/21/how-to-read-pdf-files-with-python/
 
#text = extract_text("apple_10k.pdf")

# extract text from the first 10 pages
#text10 = extract_text("apple_10k.pdf", page_numbers = range(10))
 
# get text from pages 0, 2, and 4
#text_pages = extract_text("apple_10k.pdf", page_numbers = [0, 2, 4])

#Password protected
#text = extract_text("apple_10k.pdf", password = "top secret password")

def pdfminer(pdffile,pages):
    text= extract_text(pdffile, page_numbers = pages)

def pdf2image2text(pdf_file):
    files = []
    with(Image(filename=pdf_file, resolution = 500)) as conn: 
        for index, image in enumerate(conn.sequence):
            image_name = os.path.splitext(pdf_file)[0] + str(index + 1) + '.png'
            Image(image).save(filename = image_name)
            files.append(image_name)

    all_text = []
    for file in files:
        text = pytesseract.image_to_string(Image.open(file))
        all_text.append(text)
        
    all_text = [pytesseract.image_to_string(Image.open(file)) for file in files]

#pdfminer(r"C:\Users\Arun Kumar\Videos\deeplearningwithpython.pdf",[6])
pdf2image2text(r"C:\Users\Arun Kumar\Videos\deeplearningwithpython.pdf")