# -*- coding: utf-8 -*-
class group(object):
    def __init__(self,nom,sujet,parent=[],subGroup=[],):
        # Définition des 4 attributs d'un groupe
        self.nom=nom
        self.sujet=sujet
        self.parent=parent[:]
        self.subGroup=subGroup[:]

    def __str__(self):
        # Définition de l'affichage du groupe
        st = self.nom+" ["+self.sujet+"]"
        if self.subGroup not in ([],['']): #supprimer deuxième possiblité si résolu
            st+="\n -inclut ["
            for e in self.subGroup:
                if st[-1]!="[":
                    st+=","
                if type(e)==str:
                    st+=e
                else:
                    st+=e.nom
            st+="]"
        if self.parent not in ([],['']):
            st+="\n -decoule de ["
            for e in self.parent:
                if st[-1]!="[":
                    st+=","
                if type(e)==str:
                    st+=e
                else:
                    st+=e.nom
            st+="]"
        return st
    '''
    def __lt__(self, other):
        for e in other.parent:
            if self.nom==e:
                return True
        return False
    '''
    def changeSujet(self,nvSujet):
        # Changement du sujet
        self.sujet=nvSujet
    
    def ajSG(self,SG):
        # Ajoute un sous-groupe
        if SG not in self.subGroup:
            self.subGroup.append(SG)
    
    def remSG(self,SG):
        # Supprime un sous-groupe si présent
        if SG in self.subGroup:
            self.subGroup.remove(SG)
    
    def ajP(self,P):
        # Ajoute un parent
        if P not in self.parent:
            self.parent.append(P)
    
    def remP(self,P):
        # Supprime un parent si présent
        if P in self.parent:
            self.parent.remove(P)
    
    def ajEnf(self,Enf):
        # Fait de l'élément un parent d'Enf
        if self not in Enf.parent:
            Enf.parent.append(self)
            
    def remEnf(self,Enf):
        # Supprime la parenté de l'élément pour Enf s'il existe
        if self in Enf.parent:
            Enf.parent.remove(self)
    


'''
    # Essais
G0=group('G0','Test0')
G1=group('G1','Test1')
G2=group('G2','Test2')
G3=group('G3','Test3')
G4=group('G4','Test4')
G5=group('G5','Test5')

G1.ajP(G0)
G2.ajP(G0)
G3.ajP(G0)
G5.ajP(G1)
G5.ajP(G2)
G4.ajSG(G1)
G4.ajSG(G2)
G4.ajSG(G3)

print ''
print G0
print ''
print G1
print ''
print G2
print ''
print G3
print ''
print G4
print ''
print G5
print ''
'''