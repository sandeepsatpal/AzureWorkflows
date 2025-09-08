import fitz  # PyMuPDF
from pdfminer.high_level import extract_text
from PyPDF2 import PdfReader

#Method 1
print("Method 1")

doc = fitz.open('C:\\Users\\ssatpal\\Downloads\D290820241114128538-GroupOfPDFS_2 (1).pdf')
text = ""
i = 0
for page in doc:
    print(f"page:{i}")
    text = page.get_text()
    print(text)
    i=i+1
doc.close()


#Method 2
print("Method 2")
text = extract_text('C:\\Users\\ssatpal\\Downloads\D290820241114128538-GroupOfPDFS_2 (1).pdf')
print(text)


#Method 3
print("Method 3")

reader = PdfReader('C:\\Users\\ssatpal\\Downloads\D290820241114128538-GroupOfPDFS_2 (1).pdf')
text = ""
for page in reader.pages:
    text += page.extract_text()

print(text)



