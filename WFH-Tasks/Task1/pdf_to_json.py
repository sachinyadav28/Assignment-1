import json
import coercion
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1

def pdf_form_to_json(pdf_path, json_path):
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

    with open(json_path, 'w') as files:
        files.write(form_json)

    print("Success")

pdf_file = 'Enrollment_Form_filled.pdf'
json_file = 'Enrollment_Form.json'

pdf_form_to_json(pdf_file,json_file)


