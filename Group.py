# -*- coding: utf-8 -*-
class group(object):
    def __init__(self,sujet,subGroup=[],parent=[]):
        # Définition des 3 attributs d'un groupe
        self.sujet=sujet
        self.subGroup=subGroup
        self.parent=parent
    
    def __str__(self):
        # Définition de l'affichage du groupe
        st = "["+self.sujet+"]"
        if self.subGroup!=[]:
            st+="\n -inclut ["
            for e in self.subGroup:
                if st[-1]!="[":
                    st+=","
                st+=e
            st+="]"
        if self.parent!=[]:
            st+="\n -découle de ["
            for e in self.parent:
                if st[-1]!="[":
                    st+=","
                st+=e
            st+="]"
        return st
    
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
    


# Essais

c=group('Test1')
c.ajSG('G1')
c.ajSG('G2')
c.ajSG('G3')
c.ajP('P1')
c.ajP('P2')
c.ajP('P3')
c.ajP('P4')

print c
