"""
-------------------------------------------
|                 Code RPG                |
|  Quentin Villalonga & Emma De Smeytère  |
-------------------------------------------

"""

import random
from unittest import case
#from typing_extensions import self

class Arme:

    def __init__(self, degat = 2):
        self.__degat = degat
        self.portee = 3

    def getDegat(self):
        return self.__degat

class Epee(Arme):

    def __init__(self, degat = 2):
        super().__init__()

class Baton(Arme):

    def __init__(self, degat = 2):
        super().__init__()

class Arc(Arme):

    def __init__(self, degat = 2):
        super().__init__()
        self.__nbFleches = 50
        self.__nbFlechesMax = 50

class Consommable :

    def __init__(self, nom, quantite):
        self.__nom = nom
        self.__quantite = quantite

    def getNom(self):
        return self.__nom

    def getQuantite(self):
        return self.__quantite
    
    def setQuantite(self, quantite):
        self.__quantite = quantite

class Personnage :

    __niveauMax = 99

    def __init__(self, niveau =1 , force = 10, pv= 100, pvMax = 100, ResistanceMagique= 1, defense = 1,Critique = 8,Agilite = 30 ):
        self.__niveau = niveau
        self.__force = force
        self.__pv = pv
        self.__pvMax = pvMax
        self.__armeEquipe = Arme() #None
        #self.__armesPossede = []

        #Propriétés ajoutées
        self.__ResistanceMagique = ResistanceMagique
        self.__Defense = defense
        self.__Critique = Critique
        self.__Agilite = Agilite

        #Gestion du butin
        self.__inventaire = [Consommable("Potion de Soin", 3)]

    def getNiveau(self):
        return self.__niveau
    
    def gainDeNiveau(self):
        self.__niveau += 1
        self.__pvMax += 5
        self.__force += 3
        self.__Defense += 2
        self.__pv = self.__pvMax
    
    def perteDeNiveau(self):
        self.__niveau -= 1
        self.__pvMax -= 5
        self.__force -= 3
        self.__Defense -= 2
        self.__pv = self.__pvMax
    
    def estVivant(self):
        return self.__pv > 0
    
    def getInventaire(self):
        return self.__inventaire
    
    def ajouterALInventaire(self, objet):
        for k in self.__inventaire:
            if (objet.getNom() == k.getNom()):
                k.setQuantite(k.getQuantite() + objet.getQuantite())
                return 
        self.__inventaire.append(objet)
    
    def retirerDeLInventaire(self, nom, quantite):
        for i in range(len(self.__inventaire)):
            k = self.__inventaire[i]
            if (k.getNom() == nom):
                k.setQuantite(k.getQuantite() - quantite)
                if (k.getQuantite() == 0):
                    self.__inventaire.pop(i)
                return
        print("Erreur -- L'objet n'est pas présent dans l'inventaire")
                                                                     
    def equiperArme(self, arme):
        raise NotImplementedError("Cette méthode est abstraite, donc à rédéfinir par les classes filles")

    def getDefense(self):
        return self.__Defense

    def setDefense(self, defense):
        self.__Defense = defense

    def getAgilite(self):
        return self.__Agilite
    
    def setAgilite(self, valeur):
        self.__Agilite = valeur
    
    def getCrit(self):
        return self.__Critique
    
    def getArmeEquipe(self):
        return self.__armeEquipe


    def attaquer(self, cible):
        n_critique = random.randint(1, 100)
        n_esquive = random.randint(1, 100)

        if (n_critique < self.getCrit() and n_esquive > cible.getAgilite()):
            cible.setHP(cible.getHP() - max(1, 2 * self.__force * self.getArmeEquipe().getDegat() - cible.getDefense()))
        elif(n_critique > self.getCrit() and n_esquive > cible.getAgilite()):
            cible.setHP(cible.getHP() - max(1, self.__force * self.getArmeEquipe().getDegat() - cible.getDefense()))
        else:
            pass
    
    def getForce (self):
        return self.__force

    def getHP (self): #GetHp : montrer les pv
        return self.__pv

    def setHP (self,pv): #SetHp : Limiter les pv a 100 (par exemple) meme si on entre plus
        if ( pv < 0):
            self.__pv = 0
        elif ( pv < self.__pvMax):
            self.__pv = pv
        else:
            self.__pv = self.__pvMax

    def setForce (self, force): #Si on met 3 de force à Claude, sa force est égale à 3.
            self.__force = force

    def getNiveauMax(): #Get = avoir une valeur, GetNiveauMax = avoir valeur de niveau max
        return Personnage.__niveauMax
    
    def getResistanceMagique(self):
        return self.__ResistanceMagique

class Mage (Personnage):

    def __init__(self):
        super().__init__()
        self.__magie = 5

    def attaquer(self, cible):
        n_critique = random.randint(1, 100)
        n_esquive = random.randint(1, 100)

        if (n_critique < self.getCrit() and n_esquive > cible.getAgilite()):
            cible.setHP(cible.getHP() - max(1, 2 * self.__magie * self.getArmeEquipe().getDegat() - cible.getResistanceMagique()))
        elif(n_critique > self.getCrit() and n_esquive > cible.getAgilite()):
            cible.setHP(cible.getHP() - max(1, self.__magie * self.getArmeEquipe().getDegat() - cible.getResistanceMagique()))
        else:
            pass

    def equiperArme(self, arme):
        if (isinstance (arme, Baton)):
            self.__armeEquipe = arme
        else: 
            print("Cette arme n'est pas pour moi.")
    
    def sortDeSoin(self, cible):
        n_critique = random.randint(1, 100)

        if (n_critique < self.getCrit()):
            cible.setHP(cible.getHP() + 2 * self.__magie * self.getArmeEquipe().getDegat())
        else:
            cible.setHP(cible.getHP() + self.__magie * self.getArmeEquipe().getDegat())
    
    def sortDEsquive(self, cible):
        n_critique = random.randint(1, 100)

        if (n_critique < self.getCrit()):
            cible.setAgilite(cible.getAgilite() + 2 * self.__magie * self.getArmeEquipe().getDegat())
        else:
            cible.setAgilite(cible.getAgilite() + self.__magie * self.getArmeEquipe().getDegat())

    def sortDeDefense(self, cible):
        n_critique = random.randint(1, 100)

        if (n_critique < self.getCrit()):
            cible.setDefense(cible.getDefense() + 2 * self.__magie * self.getArmeEquipe().getDegat())
        else:
            cible.setDefense(cible.getDefense() + self.__magie * self.getArmeEquipe().getDegat())

class Guerrier(Personnage):

    def __init__(self):
        super().__init__()

    def equiperArme(self, arme):
        if (isinstance (arme, Epee)):
            self.__armeEquipe = arme
        else: 
            print("Cette arme n'est pas pour moi.")

class Archer(Personnage):

    def __init__(self):
        super().__init__()
        self.__dexterite = 10 

    def equiperArme(self, arme):
        if (isinstance (arme, Arc)):
            self.__armeEquipe = arme
        else: 
            print("Cette arme n'est pas pour moi.")


class RPG:

    def playTheGame():
        #Initialisation du jeu
        batonDeBase = Baton(10)
        
        heros = Mage()
        heros.equiperArme(batonDeBase)
        
        mechant = Mage()
        mechant.equiperArme(batonDeBase)

        compteurDEnnemis = 0
        listeFibo = [1, 2, 3, 5, 8, 13, 21, 34]

        #Deroulement du jeu
        while (heros.getNiveau() > 0):

            #Deroulement d'un combat
            while (heros.estVivant() and mechant.estVivant()):
                print("-------------------------------")
                print("1 -- Attaquer")
                print("2 -- Magie")
                print("3 -- Objet")
                print("4 -- Autre")
                print("")
                print("Que faire ?")
                choix = int(input())

                if (choix == 1):
                    heros.attaquer(mechant)
                
                elif (choix == 2):
                    print("1 -- Sort de soin")
                    print("2 -- Sort de défense")
                    print("3 -- Sort d'esquive")
                    choix = int(input())

                    if (choix == 1):
                        heros.sortDeSoin(heros)
                    
                    if (choix == 2):
                        heros.sortDeDefense(heros)
                    
                    if (choix == 3):
                        heros.sortDEsquive(heros)
                
                elif (choix == 3):
                    if (len(heros.getInventaire()) == 0):
                        print("Vous n'avez pas d'objet !")
                        continue
                    else:
                        print("-- Contenu de l'inventaire --")
                        for i in range(len(heros.getInventaire())):
                            print(i, " : ", heros.getInventaire()[i].getNom(), "x", heros.getInventaire()[i].getQuantite())
                        print("")
                        print("Quel objet utiliser?")
                        choix = int(input())
                        consommableChoisi = heros.getInventaire()[choix]
                        if (consommableChoisi.getNom() == "Potion de Soin"):
                            heros.setHP(heros.getHP() + 50)
                        elif (consommableChoisi.getNom() == "Parchemin maudit"):
                            mechant.setHP(mechant.getHP() - 50)
                        else:
                            print("Saisie invalide")
                            continue
                        heros.retirerDeLInventaire(consommableChoisi.getNom(), 1)
                        

                    
                
                elif(choix == 4):
                    print("Lancer une pierre !")
                    mechant.setHP(mechant.getHP() - 1)
                
                else:
                    print("Saisie invalide")
                    continue

                mechant.attaquer(heros)
                print("Le méchant vous attaque !")
            

                print ("Les HP du heros sont :",  heros.getHP())
                print ("Les HP du méchant sont :", mechant.getHP())

                if (mechant.getHP() <= 0):
                    mechant = Mage()
                    mechant.equiperArme(batonDeBase)
                    
                    #Gestion de l'expérience
                    compteurDEnnemis += 1
                    if (len(listeFibo) > 0):
                        if(compteurDEnnemis >= listeFibo[0]):
                            heros.gainDeNiveau()
                            listeFibo.pop(0)
                            print("Gain de niveau !")
                    else:
                        print("Vous avez gagné !")
                        break

                    unSurDeux = random.random()
                    if (unSurDeux < 0.5):
                        heros.ajouterALInventaire(Consommable("Potion de Soin", 1))
                        print("Vous lootez une potion de soin !")
                    else:
                        heros.ajouterALInventaire(Consommable("Parchemin maudit", 1))
                        print("Vous lootez un parchemin maudit !")
                
                if (heros.getHP() <= 0):
                    heros.perteDeNiveau()
                

            
            


RPG.playTheGame()

