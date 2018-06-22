#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/22 10:42

# 根据excel表格的字段 建表, 以列/行的字段两种情况为例子
# 整体思路, 读取excel/csv表格的字段, 并存储到 list中, 结合建表语句, 创建表; 核心问题, 如何兼顾 字符的类型格式;
# 或者生成建表语句; 问题：1.数据库类型;2.所有字符类型
# 涉及的 模块：pyMysql, os, random , string
# 实现过程：1.读取文件,存到list 2.插入模板 3.保存到sql文件

import csv
import os
import random
import openpyxl

wb = openpyxl.load_workbook('test.xlsx')
# print(type(wb))
# wb.get_sheet_names()
# print(wb.get_sheet_by_name('a'))
# sheetA = wb.get_sheet_by_name('a')
sheetA = wb['a']
active = wb.active  # 选择打开展示的sheet
# 获取最大行数,max_row; max_column 获取最大列数
# print(active.max_column)
# print(active)
# print(sheetA)
# print(sheetA['A'])
# sheetValue = sheetA.cell(row=1, column=2)
# print(sheetValue.value)
# for i in range(2, 8):
#     print(i, sheetA.cell(row=i, column=1).value)
# for i in range(1, 3):
#     cols = sheetA.columns[i]
#     for cellObj in cols:
#         print(cellObj.value)
col = sheetA.columns
# print(col)
rows = sheetA.rows
# for cellObj in col:
#     for cell in cellObj:
#         print(cell.value)
#     print(end=',')
# print(type(rows))
for cellRow in rows:
    saveRows = []
    for cellR in cellRow:
        # print(cellR.value)
        saveRows.append(cellR.value)
    # print(saveRows)
    print(' '.join(saveRows[1:]), end=',')
    # print(end=',')













# 建表模板
# tableCols = 'a'
# tableName = 'user'
# comment = '资产账户表'
# model = 'Drop table if exists `'+str(tableName)+'`('+tableCols+')'+'ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT="'+comment+'";'
# print(model)







