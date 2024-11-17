import xlwt
from pandas import DataFrame


def convert_to_xls(df: DataFrame, output_file: str) -> None:
    workbook_xls = xlwt.Workbook()
    sheet_xls = workbook_xls.add_sheet("OrganizeX")

    for row_idx, row in enumerate(df.to_records(index=False)):
        for col_idx, cell_value in enumerate(row):
            sheet_xls.write(row_idx, col_idx, str(cell_value))

    workbook_xls.save(output_file)
