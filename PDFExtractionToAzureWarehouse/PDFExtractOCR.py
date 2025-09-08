
import pytesseract
from pdf2image import convert_from_path

# Convert PDF to images
images = convert_from_path('Sample.pdf')

# OCR each image
text = ""
table = []
for img in images:
    text = pytesseract.image_to_string(img)
    for str in text.splitlines():
        if (str.startswith("2024")):
            data = str.split(' ')
            if(len(data) < 3):
                continue
            value = ""
            try:
                value=float(data[-1])
            except:
                value = ""
            if(isinstance(value, float)):
                table.append(str)
        #text += pytesseract.image_to_string(img)
for text in table:
    data = text.split(' ')
    date = data[0]
    number = data[1]
    test = data[2:-3]
    qty = data[-3]
    value = data[-2]
    print(date, number, test, qty, value)
