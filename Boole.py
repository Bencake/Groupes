# -*- coding: utf-8 -*-
def booleNett(phrase):
    '''
    phrase : chaîne de caractères.
    Apairage des parenthèses nécessaires, espaces tolérés, tous les autres caractères hors opérateurs sont considérés comme variables
    '''

    # 1-On enlève les espaces
    phrase=phrase.decode(encoding='UTF-8')
    phrase=phrase.replace(" ","")
            
    # 2-On fait le tour des vérifications de base avant de traiter davantage la phrase
    # 2.1-Vérification de la présence des opérateurs bien écrits, pas de caractères "|" isolés
    phrase_sans_op=phrase.replace("|ET|","")
    phrase_sans_op=phrase_sans_op.replace("|OU|","")
    if "|" in phrase_sans_op:
        print("Présence de caractères \'|\' indésirables")
        return None

    # 2.2-Vérification du bon nombre de parenthèses (ouverture et fermeture)
    parEntr=phrase_sans_op.count('(')
    parFerm=phrase_sans_op.count(')')
    if parEntr!=parFerm:
        print("Votre phrase contient "+str(parEntr)+" ouverture(s) de parenthèse pour "+str(parFerm)+" fermeture(s) !")
        return None

    # 2.3-Vérification qu'un opérateur ne colle pas l'intérieur d'une parenthèse
    if '(|' in phrase or '|)' in phrase:
        print('Un opérateur colle l\'intérieur d\'une parenthèse !')
        return None
    
    
    return phrase.encode(encoding='UTF-8')


def ou(liste):
    '''
    liste : liste de propositions évaluées
    Retourne la version simplifiée si possible de l'expression sous la forme linéaire
    '''
    
    # 1-Élimination des doublons
    liste=list(set(liste))
    
    # 2-Développement des |ET|
    dev=[]
    for e in range(len(liste)):
        dev.append(liste[e].split("|ET|"))
    print(dev)
    
    # 3-On vérifie qu'aucun des éléments de OU n'est sous-ensemble de l'un des autres (ex: a|ET|b inclus dans a|ET|b|ET|c -> la deuxième liste est supprimée)
    simpl=dev[:]
    for e in range(len(dev)):
        # A COMPLETER
        None
    
    return liste    