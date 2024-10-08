import pdfplumber
import os
from PyPDF2 import PdfReader, PdfWriter
import shutil

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
                partsMap[int(parts[0])] = {'drawing': parts[6].lower(), 'issue': parts[-1], 'packed': False}
            else:
                drw = ''
                for string in parts:
                    if soNumber in string.lower() or 'spi' in string.lower():
                        drw = string
                partsMap[int(parts[0])] = {'drawing': drw.lower(), 'issue': parts[-1], 'packed': False}
                    

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

    return output_pdf

        
def inpCombined(folder_path, soNumber):
    # Create a PdfWriter object to combine PDFs
    writer = PdfWriter()
    
    # Get a list of all the PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    # Sort files alphabetically (can be adjusted as needed)
    pdf_files.sort()

    # Loop through each PDF file and add its pages to the writer
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        reader = PdfReader(pdf_path)
        
        # Add all pages from this PDF to the writer
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

    pdf_name = "SO" + soNumber + "-CLAMP-INSULATION-COMBINED-PDF.pdf"
    
    # Define the output file name (combine.pdf)
    output_pdf = os.path.join(folder_path, pdf_name)

    # Save the combined PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)


def inpAssyDataCleanse(rawText):
    lines = rawText.strip().split('\n')

    partsList = []

    for line in lines:
        parts = line.split()
        if parts[-1].lower() == 'mq':
            for i in parts:
                if "INP-CLM" in i:
                    partsList.append(i.lower())

    return partsList

def read_assyInsulation(path, drawing_name):
    # Open the PDF file using pdfplumber
    with pdfplumber.open(path + '/' + drawing_name.lower() + '.pdf') as pdf:
        # Extract text from the first page only
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        
    return text

def inpAssyCompile(source, folderPath, assyList):

    for itemNumber in assyList:

        pdfName = itemNumber + '.pdf'
        dxfName = itemNumber + '.dxf'
        multiDxfName = itemNumber + '_'

        for root, dirs, files in os.walk(source):
            for file in files:
                if (pdfName in file) or (dxfName in file) or (multiDxfName in file):
                    source_file = os.path.join(root, file)
                    dest_file = os.path.join(folderPath, file)
                    shutil.copy2(source_file, dest_file)

def uaCombined(folder_path, soNumber):
    # Create a PdfWriter object to combine PDFs
    writer = PdfWriter()
    
    # Get a list of all the PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    # Sort files alphabetically (can be adjusted as needed)
    pdf_files.sort()

    # Loop through each PDF file and add its pages to the writer
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        reader = PdfReader(pdf_path)
        
        # Add all pages from this PDF to the writer
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

    pdf_name = "SO" + soNumber + "-UA-TX2-COMBINED-PDF.pdf"
    
    # Define the output file name (combine.pdf)
    output_pdf = os.path.join(folder_path, pdf_name)

    # Save the combined PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
