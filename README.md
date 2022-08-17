# LOTO
Tous les fichiers relatifs au projet LOTO  

## But
Automatiser la génération d'au moins un tirage du LOTO  

### Fonctionnement
1) Récupérer les données des anciens tirages sur le site de la fdj (seulement si besoin).   
2) Merge les données dans un seul Excel et faire automatiquement des stats sur l'ensemble des tirages.  
3) Récupérer ces stats comme base de données en Python. Appliquer des règles mathématiques.  
4) Générer au moins un tirage (Si plusieurs -> Vérifier qu'ils sont différents).  
*5) Enregistrer les tirages sortis (Option).  

# Conclusion
**main.py** --> Code to run
Toutes les étapes fonctionnent comme attendu.


## Attention
La récupération fonctionne tant que la FDJ ne change pas l'emplacement de récupération du fichier.  
De même, le jour ou un nouveau fichier prend la place du fichier "loto_201911.csv" --> PB.  
