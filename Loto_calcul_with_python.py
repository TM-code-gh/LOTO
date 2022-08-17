# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:11:22 2021

@author: theom
"""
from tkinter import *
from tkinter.messagebox import *
from math import *
import random
import pandas as pd
from datetime import datetime

import last_X_tirages

# =============================================================================
# 
# Fichier "bordel".
#
# data_from_new_csv(name_csv) et data_from_old_csv(name_xlsx) : A modif le cas d'un changement de fichier.
# 
# =============================================================================


# Récupèrer le nombre d'itération de chaque boule du mois de novembre (csv file)
def data_from_new_csv(name_csv):
    
    df_Last_Loto=pd.read_csv(name_csv,sep=';')
    
    tab_boule=['boule_1','boule_2','boule_3','boule_4','boule_5']
    tab_numero=[] # Tab contenant la somme de chaque sortie des simples numéros
    tab_chance=['numero_chance']
    tab_num_chance=[] # Tab contenant la somme de chaque sortie des numéros chances
    
    for k in range(1,50): # Simples numeros
        num=0    
        for boule in tab_boule:
            num+=df_Last_Loto[df_Last_Loto[boule].isin([k])][boule].count()    
        tab_numero.append(num)
    
    for k in range(1,11): # Numeros chances
        num=0
        for chance in tab_chance:
            num+=df_Last_Loto[df_Last_Loto[chance].isin([k])][chance].count()        
        tab_num_chance.append(num)    
   

    # Retourne les 2 tableaux (Synthèse des infos utiles)
    return tab_numero, tab_num_chance


# Récuperer le nombre d'itération de chaque boule : anciennes valeurs        
def data_from_old_csv(name_xlsx):    
    
    df_ancienne_valeur=pd.read_excel(name_xlsx)
    
    tab_numero_ancien=[]
    tab_num_chance_ancien=[]
    
    for k in range(49):
        tab_numero_ancien.append(df_ancienne_valeur.iloc[k,1])
    
    for k in range(10):
        tab_num_chance_ancien.append(df_ancienne_valeur.iloc[k,3])
    
    
    # Retourne les 2 tableaux (Synthèse des infos utiles)
    return tab_numero_ancien,tab_num_chance_ancien
   
 
# Associer new csv et old csv    
def associer_data(tab_numero, tab_num_chance, tab_numero_ancien,tab_num_chance_ancien):    
    for k in range(len(tab_numero)):
        tab_numero[k]+=tab_numero_ancien[k]
    
    for k in range(len(tab_num_chance)):
        tab_num_chance[k]+=tab_num_chance_ancien[k]


    return tab_numero, tab_num_chance


# Calculer les probas
def calcul_de_proba(tab_numero, tab_num_chance):
           
    # Nombre total de tirage/numéros
    nombre_tirage=sum(tab_num_chance)
    nombre_numero=sum(tab_numero)
    
    if (5*nombre_tirage!=nombre_numero):
        raise ValueError
    else:    
        # Calculer les proba
        esperance_num=204       # Esperance_num = 2.04 * 100
        esperance_chance=1000   # Esperance_chance = 10 *100
        
        tab_numero_proba=[]     # Inutile?
        tab_numero_proba_inv=[]
        
        tab_num_chance_proba=[] # Inutile?
        tab_num_chance_proba_inv=[]
        
        tab_numero_nb_num=[]
        tab_num_chance_nb_num=[]
        
        tab_numero_big_liste=[]
        tab_num_chance_big_liste=[]
    
        # Calcul de pourcentages
        # Inverser les pourcentages à partir de l'espérance numéros classique = pourcentage
        for k in range(len(tab_numero)):
            temp=10000*tab_numero[k]/nombre_numero #X*10000 pour avoir des centaines
            
            if (int(temp)+0.5<temp):
                temp=int(temp+1)
            
            tab_numero_proba.append(temp)
            temp = 2*esperance_num - temp # => X=A-(B-A) & X=(A-B)+A 
            tab_numero_proba_inv.append(temp/10000)
        
        # Calcul de pourcentages
        # Inverser les pourcentages à partir de l'espérance numéros chance = pourcentage
        for k in range(len(tab_num_chance)):
            temp=10000*tab_num_chance[k]/nombre_tirage #X*10000 pour avoir des centaines
            
            if (int(temp)+0.5<temp):
                temp=int(temp+1)
                
            tab_num_chance_proba.append(temp)
            temp = 2*esperance_chance - temp # => X=A-(B-A) & X=(A-B)+A
            tab_num_chance_proba_inv.append(temp/10000)
    
        #Passer de liste de pourcentage à une liste de nombres de numéros classique
        for k in range(len(tab_numero_proba_inv)):
            temp=tab_numero_proba_inv[k]*nombre_numero
            
            if((temp)<int(temp)+0.5):
                tab_numero_nb_num.append(int(temp)+1)
            else:
                tab_numero_nb_num.append(int(temp))
    
        #Passer de liste de pourcentage à une liste de nombres de numéros chance
        for k in range(len(tab_num_chance_proba_inv)):
            temp=tab_num_chance_proba_inv[k]*nombre_numero
            
            if((temp)<int(temp)+0.5):
                tab_num_chance_nb_num.append(int(temp)+1)
            else:
                tab_num_chance_nb_num.append(int(temp))
        
        
        #Ajout nombre par nombre d'itération : exmple => 159*1, 156*2, .... numéros classique
        for i in range(len(tab_numero_nb_num)):
            for j in range(tab_numero_nb_num[i]):
                tab_numero_big_liste.append(i+1)
        
        random.shuffle(tab_numero_big_liste)
    
        
        #Ajout nombre par nombre d'itération : exmple => 15*1, 16*2, .... numéros chance
        for i in range(len(tab_num_chance_nb_num)):
            for j in range(tab_num_chance_nb_num[i]):
                tab_num_chance_big_liste.append(i+1)
    
        random.shuffle(tab_num_chance_big_liste)
        
        print('calul de proba')
        return tab_numero_big_liste, tab_num_chance_big_liste


# Tirage numéros
def tirage_numeros(tab_numero_big_liste, tab_num_chance_big_liste):
    
    liste_finale=[]
    
    for k in range(5):
        numero = tab_numero_big_liste[random.randrange(len(tab_numero_big_liste)+1)]
        while(numero in tab_numero_big_liste):
            tab_numero_big_liste.remove(numero)
        liste_finale.append(numero)
        
        if(tab_numero_big_liste.count(numero)!=0):  # Vérifier que le remove est ok = 0
            raise Exception 
            

    #Tirage numéros chance
    numero_chance = tab_num_chance_big_liste[random.randrange(len(tab_num_chance_big_liste)+1)]
    
    print('')
    print("Liste finale à jouer :",liste_finale)
    print('le numéro chance :',numero_chance)
    
    return liste_finale, numero_chance
    

# Out of date
def affichage(liste_finale, numero_chance):
    
    def affichage_SurEx():
        B = 0
        inListe = 'red'
        offListe = 'blue'
        color = offListe
        for k in range (8):
            if (k != 7):
                can.create_line(70 * k, 0, 70 * k, 490, fill='blue')
            can.create_line(0, 70 * k, 490, 70 * k, fill='blue')
        for k in range (10):
            if (k==numero_chance-1):
                color=inListe
            else:
                color=offListe
            can.create_line(49 * k, 490, 49 * k, 560, fill='blue')
            can.create_text(24 + 49 * k, 525 , text = k+1, font = "Arial 16 italic" , fill = color)
        for k in range (7):
            for i in range (7):
                B+=1
                for j in range (len(liste_finale)):
                    if (B==liste_finale[j]):
                        color=inListe
                        break
                    else:
                        color=offListe
                can.create_text(35 + 70 * i, 35 + 70 * k, text = B, font = "Arial 16 italic" , fill = color)
                
    
    fen = Tk()
    can = Canvas(fen, width=490, height=560, bg="white")
    can.pack(side=TOP, padx=5, pady=5)
    B_Surbrillance=Button(fen, text="Afficher les numéros", command = affichage_SurEx)
    B_Surbrillance.pack(side = LEFT, padx = 3, pady = 3)
    
    fen.mainloop()


# Comparer les X derniers tirages et les nouveux tirages
def comparer_tirages(tab_numero_big_liste, tab_num_chance_big_liste, tab_tirage_num, tab_tirage_chance, how_many):
    compt=0
    tab_jouer_simple=[]
    tab_jouer_chance=[]
    
    while compt<how_many:

        liste_finale, numero_chance = tirage_numeros(tab_numero_big_liste, tab_num_chance_big_liste)
        
        for tab in tab_tirage_num:
            is_equal=0  # Vérifier que tous les numéros sont différents
            
            for numero in tab:
                if(numero in liste_finale):
                    is_equal+=1
                    
            if(is_equal==5):
                print('Même tirage que dans les ','10',' derniers tirages')
                compt-=1
                

        tab_jouer_simple.append(liste_finale)
        tab_jouer_chance.append(numero_chance)
        compt+=1
        
        if(compt>20):
            print('WARNING : ERROR')
            break
        
    return tab_jouer_simple, tab_jouer_chance


# Générer les ids des Tirages
def generer_id(nb_id, date_de_tirage):
    tab_id_tirage=[]
    
    for i in range(nb_id):
        id_tirage=date_de_tirage[8:10]
        id_tirage+=date_de_tirage[3:5]
        id_tirage+=date_de_tirage[0:2]
        
        if(i<10):
            id_tirage+='0'+str(i)
        else:
            id_tirage+=str(i)
        
        id_tirage=int(id_tirage)
        #tab_id_tirage.insert(0, id_tirage)
        tab_id_tirage.append(id_tirage)
    
    return tab_id_tirage


def run_it(how_many, date_de_tirage):

    tab_numero, tab_num_chance = data_from_new_csv('loto_201911.csv')
    tab_numero_ancien,tab_num_chance_ancien = data_from_old_csv('test_ancienne_valeur.xlsx')
    tab_numero, tab_num_chance = associer_data(tab_numero, tab_num_chance, tab_numero_ancien, tab_num_chance_ancien)
    tab_numero_big_liste, tab_num_chance_big_liste = calcul_de_proba(tab_numero, tab_num_chance)
    
    tab_tirage_num, tab_tirage_chance = last_X_tirages.last_X_tirage(10)
    tab_jouer_simple, tab_jouer_chance = comparer_tirages(tab_numero_big_liste, tab_num_chance_big_liste, tab_tirage_num, tab_tirage_chance, 5)
    tab_id_tirage = generer_id(how_many, date_de_tirage)
    
    return tab_id_tirage, tab_jouer_simple, tab_jouer_chance
    
    
def show_it():
    tab_id_tirage, tab_jouer_simple, tab_jouer_chance = run_it(5, 'XX/XX/XXXX')
    #affichage(liste_finale, numero_chance)
    

if __name__ == "__main__":
    #show_it()
    run_it(5, 'XX/XX/XXXX')
    










    