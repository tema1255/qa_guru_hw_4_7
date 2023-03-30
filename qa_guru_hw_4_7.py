import zipfile
from zipfile import ZipFile
from PyPDF2 import PdfReader
import csv, os, openpyxl

pdf_size = os.path.getsize("examples/docs.pdf")
xlsx_size = os.path.getsize("examples/file.xlsx")
csv_size = os.path.getsize("examples/username.csv")


def delete_zip():
    path = os.path.abspath("resources")
    os.remove(path)


def pdf_pages_num():
    with open("examples/docs.pdf", "rb") as pdffile:
        pdf_reader = PdfReader(pdffile)
        pdf_pages = len(pdf_reader.pages)
        return pdf_pages


def xlsx_max_row():
    workbook = openpyxl.load_workbook("examples/file.xlsx")
    sheet = workbook.active
    xlsx_row = sheet.max_row
    return xlsx_row


def csv_max_row():
    with open("examples/username.csv") as csvfile:
        csvfile = csv.reader(csvfile)
        csv_row = 0
        for r in csvfile:
            csv_row += 1
        return csv_row


def zip_file():
    with ZipFile("resources/test.zip", "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write("examples/docs.pdf", "pytest.pdf")
        pdf_zipfile = zf.open("pytest.pdf")
        pdf_reader = PdfReader(pdf_zipfile)
        pdf_zipfile_pages = len(pdf_reader.pages)
        pdf_zipfile_size = zf.getinfo("pytest.pdf").file_size

        zf.write("examples/file.xlsx", "example.xlsx")
        xlsx_zipfile = zf.open("example.xlsx")
        zip_workbook = openpyxl.load_workbook(xlsx_zipfile)
        sheet = zip_workbook.active
        xlsx_zip_row = sheet.max_row
        xlsx_zipfile_size = zf.getinfo("example.xlsx").file_size

        zf.write("examples/username.csv", "username.csv")
        csv_zipfile = zf.open("username.csv")
        csv_zip_row = 0
        for r in csv_zipfile:
            csv_zip_row += 1
        csv_zipfile_size = zf.getinfo("username.csv").file_size

        return [
            pdf_zipfile_size,
            xlsx_zipfile_size,
            csv_zipfile_size,
            pdf_zipfile_pages,
            xlsx_zip_row,
            csv_zip_row,
        ]


def test_rezult():
    assert pdf_size == zip_file()[0]
    assert xlsx_size == zip_file()[1]
    assert csv_size == zip_file()[2]
    assert pdf_pages_num() == zip_file()[3]
    assert xlsx_max_row() == zip_file()[4]
    assert csv_max_row() == zip_file()[5]
