# -*- coding:utf-8 -*-
__author__ = "leo"

import os

import openpyxl

base_path = os.path.dirname(os.getcwd())
print(base_path)


class HandleExcel:
    def load_excel(self):
        open_excel = openpyxl.load_workbook(base_path + "/case/case.xlsx")
        return open_excel

    def get_sheet_data(self, index=None):
        sheet_name = self.load_excel().sheetnames

        if index is None:
            index = 0

        data = self.load_excel()[sheet_name[index]]
        return data

    def get_cell_value(self, row, col):
        data = self.get_sheet_data().cell(row=row, column=col).value
        return data

    def get_rows(self):
        row = self.get_sheet_data().max_row
        return row

    def get_rows_value(self, row):
        row_list = []

        for i in self.get_sheet_data()[row]:
            row_list.append(i.value)

        return row_list

    def excel_write_data(self, row, col, value):
        wb = self.load_excel()
        wr = wb.active
        wr.cell(row, col, value)
        wb.save(base_path + "/case/case.xlsx")

    def get_column_value(self, key=None):
        if not key:
            key = "A"

        column_list = []
        column_list_data = self.get_sheet_data()[key]
        for item in column_list_data:
            column_list.append(item.value)
        return column_list

    def get_row_number(self, case_id):
        col_data = self.get_column_value()
        if case_id in col_data:
            return col_data.index(case_id) + 1
        return None

    def get_excel_data(self):
        """将 Excel 中每一行的数据存储在一个列表中"""
        data_list = []
        for i in range(2, self.get_rows()+1):
            data_list.append(self.get_rows_value(i))

        return data_list


excel_data = HandleExcel()
