import pandas as pd
import glob  # Standard library built-in python, used for file managements etc..
from fpdf import FPDF
from pathlib import Path



# Making a list of filepaths using glob library
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    # Getting File names, data using Path library
    filename = Path(filepath).stem
    invoice_no = filename.split('-')[0]

    # Getting Date
    date = filename.split('-')[1]

    # Making a PDF
    pdf = FPDF(orientation='P' , unit = 'mm' , format='A4')
    pdf.add_page()

    # Adding Invoice Number
    pdf.set_font(family='Arial' , style='B' , size=20)
    pdf.cell(w=50,h=8, 
             txt = f'Invoice No - {invoice_no}',
             ln=1)

    # Adding Date
    pdf.set_font(family='Arial' , style='B' , size=16)
    pdf.cell(w=0,h=8,
             txt=f'Date - {date}',
             ln=1)
    
    pdf.cell(w=0,h=10, txt='',ln=1)
    

    # Created a dataframe 
    df = pd.read_excel(filepath , sheet_name="Sheet 1")

    # Adding Header row
    columns = list(df.columns)
    columns = [items.replace('_' , " ").title() for items in columns]
    

    pdf.set_font(family='Arial' ,  style='B' ,size=10)
    pdf.set_text_color(0,0,0)

    pdf.cell(w=30 , h=8 , txt=columns[0] , border=1 )
    pdf.cell(w=65 , h=8 , txt=columns[1] , border=1)
    pdf.cell(w=35 , h=8 , txt=columns[2] , border=1)
    pdf.cell(w=30 , h=8 , txt=columns[3] , border=1)
    pdf.cell(w=30 , h=8 , txt=columns[4] , border=1,
             ln=1)


    # Adding data table

    for index, row in df.iterrows():

        pdf.set_font(family='Arial' , size=10)
        pdf.set_text_color(60,60,60)
        pdf.cell(w=30 , h=8 , txt=str(row['product_id']) , border=1 )
        pdf.cell(w=65 , h=8 , txt=str(row['product_name']) , border=1)
        pdf.cell(w=35 , h=8 , txt=str(row['amount_purchased']) , border=1)
        pdf.cell(w=30 , h=8 , txt=str(row['price_per_unit']) , border=1)
        pdf.cell(w=30 , h=8 , txt=str(row['total_price']) , border=1,
                 ln=1)
        
    # Adding Total Price sum

    total_price = df['total_price'].sum()
    pdf.set_font(family='Arial' , size=10 , style='B')
    pdf.set_text_color(60,60,60)
    pdf.cell(w=30 , h=8 , txt='' , border=1)
    pdf.cell(w=65 , h=8 , txt= '', border=1)
    pdf.cell(w=35 , h=8 , txt= '', border=1)
    pdf.cell(w=30 , h=8 , txt= '', border=1)
    pdf.cell(w=30 , h=8 , txt=str(total_price), border=1,
                ln=1)
    
    # Adding total sum sentence 

    pdf.set_font(family='Arial' , size=12)
    pdf.set_text_color(0,0,0)

    pdf.cell(w=0,h=10 , txt=f'The total price is {total_price}rs' , ln=1)


    # Adding company name and logo

    pdf.set_font(family='Times' , size=16 , style='B')
    pdf.cell(w=30,h=15,txt='Siddharth')
    pdf.image('Profile.png' , w=10)

        

    
    pdf.output(f'Invoice-PDFs/{filename}.pdf')




