import pdfplumber

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

def inpDataCleanse(rawText):
    lines = rawText.strip().split('\n')

    partsMap = {}

    for line in lines:
        parts = line.split()
        
        if parts[0].isdigit():
            partsMap[int(parts[0])] = {'drawing': parts[6], 'issue': parts[-1], 'packed': False}

    return partsMap