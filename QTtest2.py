import sys
import lecture
from PyQt5 import QtCore, QtGui, uic, QtWidgets
 
qtCreatorFile = "persoGroup2.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        # Création de variable vide pour contenu de sauvegarde de session
        self.sauvSession={}
        # Pour copie temporaire avant enregistrement des modifications
        self.sauvSessionMod={}

        # Création de variable vide pour contenu de liste des enfants
        self.listEnfants={}
        self.listEnfantsMod={}
        
        # Création de variable vide pour contenu de liste des sur-groupes
        self.listSurGroupes={}
        self.listSurGroupesMod={}
        
        # Création des variables correspondant à la sélection dans les listes
        # Liste de gauche
        self.selVar1=''
        
        
        
        # Création de la variable de modifications
        # La variable est True quand des modifications ont été apportées à la sauvegarde en cours de session
        # Un message de confirmation sera alors affiché avant de quitter ou de charger un autre fichier
        self.unsavedMod=False
        
        
        # Lorsque un des éléments est sélectionné dans laliste de gauche
        self.chargedList_view.currentItemChanged.connect(self.sel1_clicked)
        
        
        # Appel des fonctions liées aux boutons
        # Le bouton Nouveau Sujet est utilisé :
        self.newSubj_button.clicked.connect(self.b1_clicked)
        
        # Le bouton Enregistrer modifications est utilisé :
        self.saveChng_button.clicked.connect(self.b2_clicked)
        
        # Le bouton Ajouter parent(s) est utilisé :
        self.parentIn_button.clicked.connect(self.b3_clicked)
        
        # Le bouton Supprimer parent(s) est utilisé :
        self.parentOut_button.clicked.connect(self.b4_clicked)
        
        # Le bouton Ajouter sous-groupe(s) est utilisé :
        self.subGroupIn_button.clicked.connect(self.b5_clicked)
        
        # Le bouton Supprimer sous-groupe(s) est utilisé :
        self.subGroupOut_button.clicked.connect(self.b6_clicked)
        
        # Le bouton Ajouter enfant(s) est utilisé :
        self.childIn_button.clicked.connect(self.b7_clicked)
        
        # Le bouton Supprimer enfant(s) est utilisé :
        self.childOut_button.clicked.connect(self.b8_clicked)
        
        # Le bouton Ajouter sur-groupe(s) est utilisé :
        self.surGroupIn_button.clicked.connect(self.b9_clicked)
        
        # Le bouton Supprimer sur-groupe(s) est utilisé :
        self.surGroupOut_button.clicked.connect(self.b10_clicked)
        
        # Appel des fonctions liées aux actions de menu
        # L'action Charger est utilisée :
        self.actionCharger.triggered.connect(self.charger)
        
        # L'action Enregistrer est utilisée :
        self.actionSauvegarder.triggered.connect(self.enregistrer)
        
        # L'action Enregistrer sous est utilisée :
        self.actionSauvegarder_sous.triggered.connect(self.enregistrerSous)
        
        
    # Remplissage de la liste de sujets de gauche à partir de la sauvegarde de session
    def listeSuj(self):
        self.chargedList_view.clear()
        for doc in self.sauvSessionMod.keys():
            it = doc+'\t'+self.sauvSessionMod[doc]['Sujet']
            cont = 'Contenu :\n'+self.sauvSessionMod[doc]['Contenu']
            de=QtWidgets.QListWidgetItem(it)
            self.chargedList_view.addItem(de)
            de.setToolTip(cont)
        self.chargedList_view.sortItems()
        print("La liste de sujets a été chargée et affichée dans la liste de gauche")
     
    # Remplissage de la liste de sujets parents à partir du sujet sélectionné à gauche
    def listeSujParent(self):
        self.parentList_view.clear()
        for parent in self.sauvSessionMod[self.selVar1]['Parent']:
            it = parent+'\t'+self.sauvSessionMod[parent]['Sujet']
            cont = 'Contenu :\n'+self.sauvSessionMod[parent]['Contenu']
            de=QtWidgets.QListWidgetItem(it)
            self.parentList_view.addItem(de)
            de.setToolTip(cont)

    # Remplissage de la liste de sujets sous-groupes à partir du sujet sélectionné à gauche
    def listeSujSousG(self):
        self.subGroupList_view.clear()
        for sousGroupe in self.sauvSessionMod[self.selVar1]['SousGroupe']:
            it = sousGroupe+'\t'+self.sauvSessionMod[sousGroupe]['Sujet']
            cont = 'Contenu :\n'+self.sauvSessionMod[sousGroupe]['Contenu']
            de=QtWidgets.QListWidgetItem(it)
            self.subGroupList_view.addItem(de)
            de.setToolTip(cont)
    
    # Remplissage de la liste de sujets enfants à partir du sujet sélectionné à gauche
    def listeSujEnfant(self):
        self.childList_view.clear()
        if self.selVar1 in self.listEnfants.keys():
            for enfant in self.listEnfants[self.selVar1]:
                it = enfant+'\t'+self.sauvSessionMod[enfant]['Sujet']
                cont = 'Contenu :\n'+self.sauvSessionMod[enfant]['Contenu']
                de=QtWidgets.QListWidgetItem(it)
                self.childList_view.addItem(de)
                de.setToolTip(cont)
    
    # Remplissage de la liste de sujets sur-groupes à partir du sujet sélectionné à gauche
    def listeSujSurG(self):
        self.surGroupList_view.clear()
        if self.selVar1 in self.listSurGroupes.keys():
            for surGroupe in self.listSurGroupes[self.selVar1]:
                it = surGroupe+'\t'+self.sauvSessionMod[surGroupe]['Sujet']
                cont = 'Contenu :\n'+self.sauvSessionMod[surGroupe]['Contenu']
                de=QtWidgets.QListWidgetItem(it)
                self.surGroupList_view.addItem(de)
                de.setToolTip(cont)
    
    # Remplissage de la liste de sujets de droite (avec indications sur disponiblité)
    def listeSujDispo(self):
        self.dispoList_view.clear()
        for doc in self.sauvSessionMod.keys():
            # Création de variable de disponibilité, par défaut OK
            available=True
            suff=""
            # On vérifie si la variable dans parents
            if doc in self.sauvSessionMod[self.selVar1]['Parent']:
                suff="[P] "
                available=False
            elif doc in self.sauvSessionMod[self.selVar1]['SousGroupe']:
                suff="[S\G] "
                available=False
            elif self.selVar1 in self.listEnfants.keys() and doc in self.listEnfants[self.selVar1]:
                suff="[E] "
                available=False
            elif self.selVar1 in self.listSurGroupes.keys() and doc in self.listSurGroupes[self.selVar1]:
                suff="[S/G] "
                available=False
            elif doc == self.selVar1:
                suff="* "
                available=False
            it = suff+doc+'\t'+self.sauvSessionMod[doc]['Sujet']
            cont = 'Contenu :\n'+self.sauvSessionMod[doc]['Contenu']
            de=QtWidgets.QListWidgetItem(it)
            self.dispoList_view.addItem(de)
            de.setToolTip(cont)
            # On vérifie la disponibilité
            if not available:
                de.setFlags(QtCore.Qt.NoItemFlags)
            if doc == self.selVar1:
                de.setForeground(QtGui.QColor(255,120,120))
        self.dispoList_view.sortItems()

            
        
    # Fonctions des actions de menu

    # Bouton Charger
    def charger(self):
        # Ouverturfe de fenêtre de dialogue avec recherche réduite aux fichiers commençant par Sauv-
        fichier = QtWidgets.QFileDialog.getOpenFileName(window, 'Open file', 'F:\\MyPython\\Groupes\\',"Sauvegarde (Sauv*.*)")
        # Remplissage de la liste des sujets existants (gauche)
        # On vérifie que l'ouverture n'a pas été annulée (nom de fichier vide)
        if fichier[0] is not '':
            # On réinitialise les deux dictionnaires
            self.listEnfants.clear()
            self.listSurGroupes.clear()
            # On extrait le contenu de la sauvegarde
            self.sauvSession=lecture.lecture(fichier[0])
            # Copie temporaire du dico de session
            self.sauvSessionMod=self.sauvSession.copy()
            
            # On remplit la liste de sujets de gauche à partir de la nouvelle sauvegarde de session
            self.listeSuj()
            # On créé un dictionnaire des enfants 
            for suj in self.sauvSession.keys():
                for par in self.sauvSession[suj]['Parent']:
                    if par in self.listEnfants.keys():
                        self.listEnfants[par].append(suj)
                    else:
                        self.listEnfants[par]=[suj]
            # On créé un dictionnaire des sur-groupes 
            for suj in self.sauvSession.keys():
                for sousG in self.sauvSession[suj]['SousGroupe']:
                    if sousG in self.listSurGroupes.keys():
                        self.listSurGroupes[sousG].append(suj)
                    else:
                        self.listSurGroupes[sousG]=[suj]
            # Copie temporaire des dicos de session
            self.listEnfantsMod=self.listEnfants.copy()
            self.listSurGroupesMod=self.listSurGroupes.copy()

     # Bouton Enregistrer
    def enregistrer(self):
        print("Enregistre")

    # Bouton Enregistrer sous
    def enregistrerSous(self):
        print("Enregistre sous")

        
        
    #Fonctions d'action des boutons cliquables

    # Bouton Nouveau Sujet
    def b1_clicked(self):
        print("Button 1 clicked")

    # Bouton Enregistrer modifications
    def b2_clicked(self):
        print("Button 2 clicked")

    # Bouton Ajouter parent(s)
    def b3_clicked(self):
        for it in self.dispoList_view.selectedItems():
            var=it.text().split("\t")[0]
            self.sauvSessionMod[self.selVar1]['Parent'].append(var)
            print(var)
        self.listeSujParent()
        self.listeSujDispo()
        #self.parentList_view.
        print("Button 3 clicked")
    # Bouton Supprimer parent(s)
    def b4_clicked(self):
        print("Button 4 clicked")

    # Bouton Ajouter sous-groupe(s)
    def b5_clicked(self):
        print("Button 5 clicked")
    # Bouton Supprimer sous-groupe(s)
    def b6_clicked(self):
        print("Button 6 clicked")

    # Bouton Ajouter enfant(s)
    def b7_clicked(self):
        print("Button 7 clicked")
    # Bouton Supprimer enfant(s)
    def b8_clicked(self):
        print("Button 8 clicked")

    # Bouton Ajouter sur-groupe(s)
    def b9_clicked(self):
        print("Button 9 clicked")
    # Bouton Supprimer sur-groupe(s)
    def b10_clicked(self):
        print("Button 10 clicked")
        
        
    # Fonctions d'action liées à la sélection d'éléments
    
    # Sélection d'un élément de la liste de gauche
    def sel1_clicked(self, item):
        # On vérifie qu'il n'y a pas eu de modification sur un élément sélectionné précédemment
        if not self.unsavedMod and item != None:
            # Copie temporaire des dico de session
            
            # ATTENTION !! LA COPIE SEMBLE INEFFICACE ICI
            self.sauvSessionMod.clear()
            self.sauvSessionMod=self.sauvSession.copy()
            self.listEnfantsMod.clear()
            self.listEnfantsMod=self.listEnfants.copy()
            self.listSurGroupesMod.clear()
            self.listSurGroupesMod=self.listSurGroupes.copy()
            # On extrait le nom de la variable
            self.selVar1=item.text().split("\t")[0]
            print("élément [%s] sélectionné" % self.selVar1)
            # On remplit la cellule de Nom
            self.subjName.setText(self.selVar1)
            # On remplit la cellule de Sujet
            self.subject.setText(self.sauvSessionMod[self.selVar1]['Sujet'])
            # On remplit la cellule du Contenu
            self.subjContent_view.setText(self.sauvSessionMod[self.selVar1]['Contenu'])
            # On appelle les fonctions servant à remplir les autres cellules
            self.listeSujParent()
            self.listeSujSousG()
            self.listeSujEnfant()
            self.listeSujSurG()
            self.listeSujDispo()
        
        








if __name__ == "__main__":
    #sauv=lecture.lecture()
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())