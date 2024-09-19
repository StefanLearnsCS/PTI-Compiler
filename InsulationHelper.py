import pdfplumber
import os
from PyPDF2 import PdfReader, PdfWriter

def read_insulation(path, drawing_name):
    # Open the PDF file using pdfplumber
    with pdfplumber.open(path + '/' + drawing_name.lower() + '.pdf') as pdf:
        # Create an empty string variable to store the text
        text = ""
        
        # Loop through all the pages and extract text
        for page in pdf.pages:
            # Extract the text from the page object, this preserves line breaks
            page_text = page.extract_text()

            # Add All parts list pages to the string variable
            if "Parts - SAP" in page_text:
                text += page_text + "\n"  # Append a new line after each page

    return text

def inpDataCleanse(rawText, soNumber):
    lines = rawText.strip().split('\n')

    partsMap = {}

    for line in lines:
        parts = line.split()
        
        if parts[0].isdigit():
            if soNumber in parts[6] or 'spi' in parts[6]:
                partsMap[int(parts[0])] = {'drawing': parts[6], 'issue': parts[-1], 'packed': False}
            else:
                drw = ''
                for string in parts:
                    if soNumber in string or 'spi' in string:
                        drw = string
                partsMap[int(parts[0])] = {'drawing': drw, 'issue': parts[-1], 'packed': False}
                    

    return partsMap

def inpAssyListCreator(source_folder, drawing_name, output_folder, soNumber):
    header = 'INP-CCC-ASSY'
    
    # Open the original PDF
    reader = PdfReader(source_folder + '/' + drawing_name.lower() + '.pdf')
    writer = PdfWriter()

    # Only extract the first page
    first_page = reader.pages[0]
    writer.add_page(first_page)

    # Create a dynamic file name (e.g., with the keyword and timestamp)
    output_pdf = os.path.join(output_folder, f"SO{soNumber}-{header}-LIST.pdf")

    # Save the new PDF with just the extracted page
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
        