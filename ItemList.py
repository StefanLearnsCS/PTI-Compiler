import os
from PyPDF2 import PdfReader, PdfWriter

def itemListCreator(source_folder, drawing_name, keyword, output_folder, soNumber, partsAbreviation):
    # Open the original PDF
    reader = PdfReader(source_folder + '/' + drawing_name.lower() + '.pdf')
    writer = PdfWriter()

    # Loop through each page
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()  # Extract the text from the page

        # Check if the keyword is in the page
        if keyword.lower() in text.lower():
            writer.add_page(page)  # Add the page to the writer
            break  # Exit the loop once we find the page

    # Create a dynamic file name (e.g., with the keyword and timestamp)
    output_pdf = os.path.join(output_folder, f"SO{soNumber}-{partsAbreviation}-LIST.pdf")

    # Save the new PDF with just the extracted page
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
