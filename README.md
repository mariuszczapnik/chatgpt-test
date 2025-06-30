# ChatGPT Test Repository

This repository contains sample Dimplex price lists in Excel format and a simple Python script for converting these spreadsheets to HTML. The HTML output can be easily viewed in any web browser.

## Installation

1. Ensure you have **Python 3** installed.
2. Install the required Python packages:

```bash
pip install pandas openpyxl
```

## Converting a Spreadsheet

Run the `convert_to_html.py` script with the Excel file you want to convert and the name of the resulting HTML file:

```bash
python convert_to_html.py cennik_dimplex_EUG_2025_PL_2025_06_30.xlsx output.html
```

The script reads the Excel file using **pandas** and **openpyxl**, then writes an HTML table to `output.html`.


