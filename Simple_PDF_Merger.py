# First install this module from internet -> pip install PyPDF2
from PyPDF2 import PdfMerger

def merge_two_pdfs(pdf1, pdf2):
    # List of PDF files to merge
    pdfs = [pdf1, pdf2]

    # Create a PdfMerger object
    merger = PdfMerger()

    # Append each PDF
    for pdf in pdfs:
        merger.append(pdf)

    # Write out the merged PDF
    merger.write("merged_output.pdf")
    merger.close()