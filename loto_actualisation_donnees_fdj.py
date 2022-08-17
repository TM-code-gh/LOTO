    # -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:02:32 2021

@author: theom
"""
# =============================================================================
# 
# Fichier gérant l'actualisation du fichier csv correspondant à novembre.
# Il s'actualise directement sur le site de la fdj. Il télécharge l'archive zip
# et extrait le fichier csv dans le même dossier. 
#
# Jour_tirage=['Monday','Wednesday','Saturday']
# Heure_fin_jeu='20:15'
# Heure_tirage='20:20'
# Heure_resultat='21'
#
# last_modified = datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%A-%d-%m-%Y')
# today = datetime.today().strftime('%A-%d-%m-%Y')
# 
# 
# =============================================================================

import os.path
from datetime import datetime, timedelta
import requests
from zipfile import ZipFile



filename='loto_201911.csv'

last_modified = datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%d/%m/%Y')
today = datetime.today().strftime('%d/%m/%Y')

print("last modified:", last_modified)
print("today:        ", today, '\n')


last_modified_hour = datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%H')
today_day = datetime.today().strftime('%A')
today_hour = datetime.today().strftime('%H')

#Télécharge le zip du loto
def get_zip_extract_zip():
    r = requests.get('https://media.fdj.fr/static/csv/loto/loto_201911.zip', allow_redirects=True)
    open('loto_201911.zip', 'wb').write(r.content)
    with ZipFile('loto_201911.zip', 'r') as zipObj:
        zipObj.extractall()
    print("Le fichier a été mis à jour - get_zip...")
    return True


# Déterminer le jour et la date du prochain tirage
def determiner_jour_date_tirage():
    if(today_day=='Monday') or (today_day=='Wednesday') or (today_day=='Saturday'):
        if(int(today_hour[0:2])<20):
            jour_de_tirage=today_day
            date_de_tirage=datetime.today().strftime('%d/%m/%Y')
        else:
            if(today_day=='Monday'):
                jour_de_tirage='Wednesday'
                date_de_tirage=datetime.now() + timedelta(days=2)
                date_de_tirage=date_de_tirage.strftime('%d/%m/%Y')           
            elif(today_day=='Wednesday'):
                jour_de_tirage='Saturday'
                date_de_tirage=datetime.now() + timedelta(days=3)
                date_de_tirage=date_de_tirage.strftime('%d/%m/%Y')            
            else:
                jour_de_tirage='Monday'
                date_de_tirage=datetime.now() + timedelta(days=2)
                date_de_tirage=date_de_tirage.strftime('%d/%m/%Y')
    else:
        if(today_day=='Sunday'):
            jour_de_tirage='Monday'
            date_de_tirage=datetime.now() + timedelta(days=1)
            date_de_tirage=date_de_tirage.strftime('%d/%m/%Y')        
        elif(today_day=='Thursday'):
            jour_de_tirage='Saturday'
            date_de_tirage=datetime.now() + timedelta(days=1)
            date_de_tirage=date_de_tirage.strftime('%d/%m/%Y')           
        elif(today_day=='Friday'):
            jour_de_tirage='Saturday'
            date_de_tirage=datetime.now() + timedelta(days=2)
            date_de_tirage=date_de_tirage.strftime('%d/%m/%Y')
        else:
            jour_de_tirage='Wednesday'
            date_de_tirage=datetime.now() + timedelta(days=1)
            date_de_tirage=date_de_tirage.strftime('%d/%m/%Y')
                    
    return jour_de_tirage, date_de_tirage


# Déterminer le jour et la date du dernier tirage
def determiner_jour_date_last_tirage():
    if(today_day=='Monday') or (today_day=='Wednesday') or (today_day=='Saturday'):
        if(int(today_hour[0:2])>20):
            jour_de_tirage_ancien=today_day
            date_de_tirage_ancien=datetime.today().strftime('%d/%m/%Y')        
        else:
            if(today_day=='Monday'):
                jour_de_tirage_ancien='Saturday'
                date_de_tirage_ancien=datetime.now() - timedelta(days=2)
                date_de_tirage_ancien=date_de_tirage_ancien.strftime('%d/%m/%Y')           
            elif(today_day=='Wednesday'):
                jour_de_tirage_ancien='Monday'
                date_de_tirage_ancien=datetime.now() - timedelta(days=3)
                date_de_tirage_ancien=date_de_tirage_ancien.strftime('%d/%m/%Y')            
            else:
                jour_de_tirage_ancien='Wednesday'
                date_de_tirage_ancien=datetime.now() - timedelta(days=2)
                date_de_tirage_ancien=date_de_tirage_ancien.strftime('%d/%m/%Y')
    else:
        if(today_day=='Sunday'):
            jour_de_tirage_ancien='Saturday'
            date_de_tirage_ancien=datetime.now() - timedelta(days=1)
            date_de_tirage_ancien=date_de_tirage_ancien.strftime('%d/%m/%Y')        
        elif(today_day=='Thursday'):
            jour_de_tirage_ancien='Wednesday'
            date_de_tirage_ancien=datetime.now() - timedelta(days=1)
            date_de_tirage_ancien=date_de_tirage_ancien.strftime('%d/%m/%Y')           
        elif(today_day=='Friday'):
            jour_de_tirage_ancien='Wednesday'
            date_de_tirage_ancien=datetime.now() - timedelta(days=2)
            date_de_tirage_ancien=date_de_tirage_ancien.strftime('%d/%m/%Y')
        else:
            jour_de_tirage_ancien='Monday'
            date_de_tirage_ancien=datetime.now() - timedelta(days=1)
            date_de_tirage_ancien=date_de_tirage_ancien.strftime('%d/%m/%Y')
                    
    return jour_de_tirage_ancien, date_de_tirage_ancien

 
#Détermine s'il y a besoin d'actualiser
def Actualise():
    jour_de_tirage_ancien, date_de_tirage_ancien = determiner_jour_date_last_tirage()
    
    if(today_day=='Monday') or (today_day=='Wednesday') or (today_day=='Saturday'):
        print('Aujourd\'hui est un jour de tirage')
        if(last_modified==today):
            print('La dernière modification a été faîte ajd') 
            if(int(last_modified_hour)>=21):
                print('Le fichier est à jour (Heure d\'actualisation > Heure de tirage)')
                return False
            elif(int(today_hour)<21):
                print('Le fichier est à jour (Heure d\'actualisation < Heure mnt < Heure de tirage)')
                return False
            else:
                print('Le fichier n\'est pas à jour (Heure d\'actualisation < Heure de tirage)')
                get_zip_extract_zip()
                return True
    
        else:
            print('Le fichier n\'a pas été actualisé ajd')
            if(int(today_hour[0:2])>=21):
                print('Le fichier n\'est pas à jour (Heure mnt > Heure de tirage)')
                get_zip_extract_zip()
                return True
            else:
                print('Heure mnt < Heure de tirage')
                if(last_modified==date_de_tirage_ancien):
                    print('La dernière modification a été faîte le jour du dernier Tirage')
                    if(int(last_modified_hour)>=21):
                        print('Le fichier est à jour (Heure d\'actualisation > Heure de tirage ancien)')
                        return False
                    else:
                        print('Le fichier n\'est pas à jour (Heure d\'actualisation < Heure de tirage ancien)')
                        get_zip_extract_zip()
                        return True
                
                elif(last_modified<date_de_tirage_ancien):
                    print('Le fichier n\'est pas à jour (Date d\'actualisation < Date de tirage ancien)')
                    get_zip_extract_zip()
                    return True
                else:
                    print('Le fichier est à jour (Date Ajd > Date d\'actualisation > Date de tirage ancien)')
                    return False  
    else:
        print('Aujourd\'hui n\'est pas un jour de tirage')
        if(last_modified==date_de_tirage_ancien):
            print('La dernière modification a été faîte le jour du dernier Tirage')
            if(int(last_modified_hour)>=21):
                print('Le fichier est à jour (Heure d\'actualisation > Heure de tirage ancien)')
                return False
            else:
                print('Le fichier n\'est pas à jour (Heure d\'actualisation < Heure de tirage ancien)')
                get_zip_extract_zip()
                return True
        elif(last_modified<date_de_tirage_ancien):
            print('Le fichier n\'est pas à jour (Date d\'actualisation < Date de tirage ancien)')
            get_zip_extract_zip()
            return True
        else:
            print('Le fichier est à jour (Date Ajd > Date d\'actualisation > Date de tirage ancien)')
            return False
  
    print('Le fichier n\'a pas été actualisé - Erreur')
    
    print('date_de_tirage_ancien : ',date_de_tirage_ancien)
    print('today_day : ', today_day)
    print('last_modified : ', last_modified)
    print('today : ', today)
    print('last_modified_hour : ', last_modified_hour)
    print('today_hour :', today_hour)
    
    return False
        



if __name__ == "__main__":
    Actualise()
    #print(determiner_jour_date_tirage(today_day))




# =============================================================================
# if('loto_201911.zip'):
#     with open('loto_201911.csv', 'r') as NovembreLoto:
#         novembre = csv.reader(NovembreLoto)
#         for row in novembre:
#             #print(row)
#             break
#     NovembreLoto.close()
# 
# =============================================================================




