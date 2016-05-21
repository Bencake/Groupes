# -*- coding: utf-8 -*-
from Group import *
import string

PATH_TO_FILE = 'F:\MyPython\Groupes\Sauvegarde'

def lectSauv():
	inFile = open(PATH_TO_FILE, 'r', 0)
	listGroup={}
	variable='nom'
	dictTemp={'nom':'',
					'sujet':'',
					'parents':'',
					'sousGroupe':''}
	for line in inFile:
		line=line[:-1]
		if line == "<I>":
			variable='nom'
		elif line == "<s>":
			variable='sujet'
		elif line == "<p>":
			variable='parents'
		elif line == "<sg>":
			variable='sousGroupe'
		elif line == "<O>":
			variable=''
			listGroup[dictTemp['nom']]=dictTemp.copy()
			#(dictTemp['sujet'],dictTemp['parents'],dictTemp['sousGroupe'])
			dictTemp={'nom':'',
					'sujet':'',
					'parents':'',
					'sousGroupe':''}
		else:
			if variable in ('parents', 'sousGroupe'):
				# Ici, line vaut 'G1,G2'
				dictTemp[variable]=line.split(',')
				# Ici, dictTemp[variable] vaut ['G1','G2']
				'''
				if dictTemp[variable] == ['']:
					dictTemp[variable]=[]
				else:
					temp=[]
					for e in dictTemp[variable]:
						#temp=locals()[e]
						None
					dictTemp[variable]=temp
				'''
			else:
				dictTemp[variable]=line
		#print line,
	#line = inFile.readline()
	#wordlist = string.split(line)
	#print "  ", len(wordlist), "words loaded."
	inFile.close()
	return listGroup

c=lectSauv()
d=c.copy()
for key in d.keys():
	if d[key]['sousGroupe']==['']:
		c[key]['sousGroupe']=[]
	else:
		tempList=[]
		for e in d[key]['sousGroupe']:
			if e not in locals().keys():
				locals()[e]=group(e,'sujet temp')
			tempList.append(locals()[e])
		c[key]['sousGroupe']=tempList
	if d[key]['parents']==['']:
		c[key]['parents']=[]
	else:
		tempList=[]
		for e in d[key]['parents']:
			if e not in locals().keys():
				locals()[e]=group(e,'sujet temp')
			tempList.append(locals()[e])
		c[key]['parents']=tempList
	#print (locals()[key])
	'''
	Code à compléter
	faire copie du dictionnaire
	Tant que dictionnaire non vide
		Récupérer parents et sous-groupes
		vérifier que les variables ont été créées au préalable
		Si oui : créer cette variable puis supprimer
		Si non : passer à suivante
	Refaire copie du dico diminué et reprendre boucle
	'''
	
	locals()[key]=group(key,c[key]['sujet'],c[key]['parents'],c[key]['sousGroupe'])
