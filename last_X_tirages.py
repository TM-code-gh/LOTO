# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:32:34 2021

@author: theom
"""
import pandas as pd

# =============================================================================
# 
# Fichier gérant la vérification que le tirage sorti est différent des x derniers tirages.
# 
# =============================================================================


def last_X_tirage(nb):
    df_Last_Loto=pd.read_csv('loto_201911.csv',sep=';')
    
    tab_boule=[4,5,6,7,8]   # numeros de colonne
    tab_chance=[9]          # numeros de colonne
    tab_tirage_num=[]
    tab_tirage_chance=[]
    
    for k in range(nb):
        tab_temp_num=[] 
        for i in tab_boule:
            tab_temp_num.append(df_Last_Loto.iloc[k,i])
        tab_tirage_num.append(tab_temp_num)
        tab_tirage_chance.append(df_Last_Loto.iloc[k,tab_chance[0]])
        
    return tab_tirage_num, tab_tirage_chance


if __name__ == "__main__":
    last_X_tirage(10)