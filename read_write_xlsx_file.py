# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:30:33 2022

@author: theom
"""

# =============================================================================
# 
# Fichier gérant l'ajout des données de l'excel vers l'excel qui contient l'historique des tiages.
# 
# =============================================================================

import pandas as pd


df = pd.read_excel('Historique_Tirage_Python.xlsx', index_col=None, header=0)  


# print(df[df['ID_tirage'].isin(['220221'])]['ID_tirage'].count())

df['ID_tirage'] = df['ID_tirage'].astype('str')

s1 = pd.Series(df['ID_tirage'])
print(s1)
print(s1.str.contains('220221', regex=False))





















