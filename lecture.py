# -*- coding: utf-8 -*-

# Récupération des données de FICHIER stockées sous format YAML pour traitement par Python

import yaml

def lecture(fichier):
    # On charge le fichier et stocke son contenu dans un dictionnaire
    stream = open(fichier, "r")
    docs = yaml.load(stream)

    # On remplit les variables restées vides des dictionnaires dans le dictionnaire créé
    for key in docs.keys():
        if 'Contenu' not in docs[key].keys():
            docs[key]['Contenu']=''
        if 'Sujet' not in docs[key].keys():
            docs[key]['Sujet']=''
        if 'Parent' not in docs[key].keys():
            docs[key]['Parent']=[]
        if 'SousGroupe' not in docs[key].keys():
            docs[key]['SousGroupe']=[]
    return docs

# On imprime le contenu du dictionnaire
if __name__ == "__main__":
    docs=lecture("Sauvegarde4")
    for key in docs.keys():
        print(key, ' -> ', docs[key])