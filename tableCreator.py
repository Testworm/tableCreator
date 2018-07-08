#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/22 10:42

# 根据excel表格的字段 建表, 以列/行的字段两种情况为例子
# 整体思路, 读取excel/csv表格的字段, 并存储到 dict, 结合建表语句, 创建表; 核心问题, 如何兼顾 字符的类型格式;
# 或者生成建表语句; 问题：1.数据库类型;2.所有字符类型
# 涉及的 模块： os, random , string
# 实现过程：1.读取文件,存到dict 2.插入模板 3.保存到sql文件

import csv
import os
import random
import openpyxl
import compiler
import numpy


def getTableCols(xlsx, tableName):
    wb = openpyxl.load_workbook(xlsx)
    # 选择sheet
    sheetA = wb['a']
    active = wb.active  # 选择打开展示的sheet
    cols = sheetA.columns
    # print(col)
    rows = sheetA.rows
    keys = []
    values = []
    dicts = dict()
    # i = 1
    for cellRow in rows:
        # 选择字段名所在列
        keys.append(cellRow[1].value)
        # 选择字段类型所在列
        values.append(cellRow[2].value)
        keyss = keys[1:]
        valuess = values[1:]
        # print(keyss)
        for key, value in zip(keyss, valuess):
            dicts[key] = value
    return tableCreatSQL(dicts, tableName)


def tableCreatSQL(dict, table):
    savecols = []
    for key, value in zip(dict.keys(), dict.values()):
        # print(key, value)
        col_type = '`' + key + '`' + ' ' + value
        savecols.append(col_type)
    sql = ','.join(savecols)
    # tableSQL = 'CREATE TABLE `'+table+'` (' + sql + ') ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT="临时表";'
    tableSQL = 'Drop table if EXISTS `' + table + '`;' \
            'CREATE TABLE `' + table + '` (' + sql + ') ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT="临时表";'
    with open('tableCreat.sql', 'w', encoding='utf-8') as f:
        f.write(tableSQL)
    return tableSQL


if __name__ == '__main__':
    # print(tableCreatSQL(getTableCols('test.xlsx'), 'temp'))
    print(getTableCols('test.xlsx', 'user'))
