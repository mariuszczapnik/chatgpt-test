import sys
import pandas as pd


def convert_excel_to_html(excel_path: str, html_path: str) -> None:
    """Read an Excel file and write its contents to an HTML file."""
    df = pd.read_excel(excel_path, engine="openpyxl")
    html = df.to_html(index=False)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)


def main(args: list[str]) -> None:
    if len(args) != 2:
        print("Usage: python convert_to_html.py <excel_file> <output_html>")
        sys.exit(1)
    excel_file, output_html = args
    convert_excel_to_html(excel_file, output_html)


if __name__ == "__main__":
    main(sys.argv[1:])
