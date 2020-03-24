import json
import coercion
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1

def pdf_form_to_json(pdf_path):
    fp = open(pdf_path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    fields = resolve1(doc.catalog['AcroForm'])['Fields']
    page_count = resolve1(doc.catalog['Pages'])['Count']
    field_count = 0
    form_data = {"document.pagecount":page_count}
    for i in fields:
        field = resolve1(i)
        field_count += 1
        name, value = field.get('T'), field.get('V')
        form_data[name] = value
    form_data["document.fieldcount"] =  field_count
    form_json = json.dumps({"map":coercion.normalize_collection(form_data)})
    return form_json

pdf_file = '/home/sachinyadav/Documents/Task1/Enrollment_Form_filled.pdf'
print(pdf_form_to_json(pdf_file))

