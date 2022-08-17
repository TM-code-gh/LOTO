# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:26:11 2021

@author: theom
"""

# =============================================================================
# 
# Fichier gérant l'export des données du csv vers l'excel qui contient tout.
# Unique utilité : Voir les données sur l'excel.
# 
# =============================================================================

import pandas as pd

# Exporter les données du csv vers l'excel qui contient tout
def file_csv_to_file_xlsx(from_csv_file,to_excel_file,sheet_name):

    # Lire le dataframe
    df = pd.read_csv(from_csv_file, sep='delimiter',engine='python')
    # Change l'ensemble des données en string (seulement lecture)
    df = df.astype(str)
    # Initiliaze data to be written as an empty list, as pyods needs a list to write
    whole_data_list = []
    
    
    # Récupérer le header des colonnes (ici lettre par lettre)
    i=0
    k=0         # Défini le stop du while par la dernière lettre de la ligne
    tab_columns=[]  # Tab contenant le header des colonnes (par ensemble de mots reconstitué)
    
    while (k<len(df.columns[0])):
        if (df.columns[0][k]==';'):
            tab_columns.append(df.columns[0][i:k])
            i=k+1
        k+=1

    # Récupérer les lignes
    for index, row in df.iterrows():
        i=0
        k=0     # Défini le stop du while par la dernière lettre de la ligne
        tab_row=[] # Tab contenant une ligne entière (par ensemble de mots reconstitué)
        
        while (k<len(row[0])):    
            if(row[0][k]==';'):
                tab_row.append(row[0][i:k])
                i=k+1   
            k+=1
            
        whole_data_list.append(tab_row) # Ensemble des lignes

    # Ensemble du DataFrame   
    dd=pd.DataFrame(data=whole_data_list,columns=tab_columns)
    
    with pd.ExcelWriter(to_excel_file, engine="openpyxl",mode='a',if_sheet_exists='replace') as writer:  
        dd.to_excel(writer, sheet_name=sheet_name,index=False) 
        
    print('csv to xlsx')

if __name__ == "__main__":
    file_csv_to_file_xlsx('loto_201911.csv','Moyenne_finale_excel.xlsx','novembre')
    
       
        
        