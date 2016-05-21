# -*- coding: utf-8 -*-

# Ecriture des données DATA dans un FICHIER de sauvegarde selon standard YAML

import yaml
import lecture

def ecriture(fichier, data):
    with open(fichier, 'w') as outfile:
        outfile.write( yaml.dump(data) )

# On imprime le contenu du dictionnaire
if __name__ == "__main__":
    docs=lecture.lecture("Sauvegarde4")
    for key in docs.keys():
        print(key, ' -> ', docs[key])
    docs=ecriture("Sauvegarde5", docs)