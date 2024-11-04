import pandas as pd
import glob  # Standard library built-in python, used for file managements etc..

# Making a list of filepaths using glob library
filepaths = glob.glob("invoices/*.xlsx")   

for filepath in filepaths:
    df = pd.read_excel(filepath , sheet_name="Sheet 1")
    print(df)