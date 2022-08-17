# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:02:10 2021

@author: theom
"""

import pandas as pd


def file_xlsx_to_file_csv(from_excel_file,to_csv_file):

    # First read into dataframe
    df = pd.read_excel(from_excel_file,index_col=False, header=False)
    df = df.astype(str)
    
    print(df)

    df.to_csv(to_csv_file,index=False,header=False,na_rep='')
    
    print('xlsx to csv')


if __name__ == "__main__":
    file_xlsx_to_file_csv('test_ancienne_valeur.xlsx','test_ancienne_valeur.csv')
    