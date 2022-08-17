# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:18:35 2021

@author: theom
"""
import pandas as pd

import loto_actualisation_donnees_fdj
import file_csv_to_file_xlsx
import Loto_calcul_with_python



if __name__ == "__main__":
    
    if(loto_actualisation_donnees_fdj.Actualise()):
        file_csv_to_file_xlsx.file_csv_to_file_xlsx('loto_201911.csv','Moyenne_finale_excel.xlsx','novembre')
        
    #file_csv_to_file_xlsx.file_csv_to_file_xlsx('loto_201911.csv','Moyenne_finale_excel.xlsx','novembre')
    
    jour_de_tirage, date_de_tirage = loto_actualisation_donnees_fdj.determiner_jour_date_tirage()
    tab_id_tirage, tab_jouer_simple, tab_jouer_chance = Loto_calcul_with_python.run_it(5, date_de_tirage)

    tab_jouer_croissant=[]
    combinaison=''
    
    for tirage in tab_jouer_simple:
        tirage.sort()   # Ordonne même tab_jouer_simple
        combinaison = '-'.join(str(num) for num in tirage)
        combinaison+='+'+str(tab_jouer_chance[tab_jouer_simple.index(tirage)])
        
        tab_jouer_croissant.append(combinaison)
    
       
    df_Last_Loto = pd.read_csv('loto_201911.csv',sep=';')
    combi_ancien = df_Last_Loto.iloc[0,10] # Combinaison gagnante ancienne

    combi_jour =   'XX-XX-XX-XX-XX+X'         
    
    df = pd.read_excel('Historique_Tirage_Python.xlsx', index_col=None, header=0)
    
    for k in range(5):
        df_to_insert=[tab_id_tirage[k],jour_de_tirage,date_de_tirage,tab_jouer_simple[k][0],
                      tab_jouer_simple[k][1],tab_jouer_simple[k][2],tab_jouer_simple[k][3],
                      tab_jouer_simple[k][4],tab_jouer_chance[k],tab_jouer_croissant[k],
                      combi_jour,'???']
        
        
        df.loc[-1]=df_to_insert
        df.index = df.index + 1  # shifting index
        df.sort_index(inplace=True)
    
    df.to_excel('Historique_Tirage_Python.xlsx',index=False)
        
        
        