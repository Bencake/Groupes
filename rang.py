def rang(group):
	if docs[group]['Parent']==[]:
		maxSG=0
		for e in docs[group]['SousGroupe']:
			maxSG=max(maxSG,rang(e))
		return maxSG
	else:
		maxParent=0
		for e in docs[group]['Parent']:
			maxParent=max(maxParent,rang(e))
		maxSG=0
		for e in docs[group]['SousGroupe']:
			maxSG=max(maxSG,rang(e))
		return max(maxParent+1,maxSG)

# Test
for i in docs.keys():
	print i, ' -> Rang ', rang(i)

# On peut créer un dictionnaire listant les groupes par rang.
# ex :
#			{0:['G0'], 1:['G1','G2','G3','G4']...}
	