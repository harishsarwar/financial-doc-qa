import pdfplumber
import pandas as pd

def extract_from_pdf(file):
    text = ""
    tables = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
            tables.extend(page.extract_tables())
    return text, tables

def extract_from_excel(file):
    xls = pd.ExcelFile(file)
    dfs = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
    return dfs
