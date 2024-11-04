import pandas as pd
import glob  # Standard library built-in python, used for file managements etc..
from fpdf import FPDF
from pathlib import Path



# Making a list of filepaths using glob library
filepaths = glob.glob("invoices/*.xlsx")   

for filepath in filepaths:
    # Created a dataframe 
    df = pd.read_excel(filepath , sheet_name="Sheet 1")

    # Getting File names, data using Path library
    filename = Path(filepath).stem
    invoice_no = filename.split('-')[0]


    # Making a PDF
    pdf = FPDF(orientation='P' , unit = 'mm' , format='A4')
    pdf.add_page()
    pdf.set_font(family='Times' , style='B' , size=20)
    pdf.cell(w=50,h=8, txt = f'Invoice No - {invoice_no}')

    pdf.output(f'PDFs/{filename}.pdf')




