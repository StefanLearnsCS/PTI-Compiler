import PyPDF2

def read_allparts(path, drawing_name):
    # Open the PDF file in read mode
    pdf_file = open(path + '/' + drawing_name.lower() + '.pdf', 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)
    # Create an empty string variable to store the text
    text = ""

    # Loop through all the pages and extract text
    for page in range(num_pages):
        # Get the page object
        pdf_page = pdf_reader.pages[page]
        # Extract the text from the page object
        page_text = pdf_page.extract_text()
        
        # Add All parts list pages to the string variable
        if "All Parts & Assemblies" in page_text:
            text += page_text

    # Close the PDF file
    pdf_file.close()

    return text