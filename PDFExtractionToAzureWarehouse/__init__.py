import logging
import azure.functions as func
import PyPDF2
import io
import pytesseract
from pdf2image import convert_from_path

def main(req: func.HttpRequest) -> func.HttpResponse:
    file = req.files.get('pdf')
    if not file:
        return func.HttpResponse("No PDF uploaded", status_code=400)
    images = convert_from_path(file)

    # OCR each image
    text = ""
    table = []
    for img in images:
        text = pytesseract.image_to_string(img)
        for str in text.splitlines():
            if (str.startswith("2024")):
                data = str.split(' ')
                if (len(data) < 3):
                    continue
                value = ""
                try:
                    value = float(data[-1])
                except:
                    value = ""
                if (isinstance(value, float)):
                    table.append(str)
            # text += pytesseract.image_to_string(img)
    return func.HttpResponse(table[0])