#-*-coding:utf8;-*-
#qpy:console
#qpy:2
"""
@author: Ernest
@date: 2014/03/15
"""
import random
import math

print("Bienvenue au  Casino!!!\n")
print("Liste des activités:")

def FoutreLeClientDehors(self,raison):
    print("On vous a jeté hors du Casino. Motif: {}".format(raison))
    
class MetaCasino(type):
    def __new__(metacls, nom, bases, attributs):
        print("\t{}".format(nom))
        attributs["Sortez"] = FoutreLeClientDehors
        attributs["pognon"] = 1000
        attributs["nombreDInfractions"] = 0
        return type.__new__(metacls, nom, bases, attributs)
        
class Roulette:
    __metaclass__ = MetaCasino
        
    def __init__(self):
        #on met des self partout pour faire plaisir à python
        print("Roulette: La roulette possède 50 cases numérotées de 0 à 49. Les cases impaires sont noires, les cases paires sont rouges. Si vous tombez sur la case sur laquelle vous avez parié, votre mise est triplée. Si vous tombez sur une case de même couleur, on vous rend 150% de la mise, sinon, la mise est perdue\n")
        while(self.pognon>0):
            print("vous disposez de {}€".format(self.pognon))
            try:
                numero = self.demanderNumero()
                mise = self.demanderMise()
            except:
                print("Erreur dans la saisie, veuillez réessayer...")
                try:
                    self.infraction()
                except:
                    break
                continue
            self.lancerLaRoulette(numero,mise)
        self.Sortez("Vous n'avez plus d'argent")
    
    def demanderNumero(self):
        numero = int(input("Sur quel numéro miser? "))
        if(numero >= 50):
            print("Il n'y a que les numeros de 0 à 49 sur la roulette")
            raise ValueError
        return numero
            
    def demanderMise(self):
        mise = int(input("Combien miser?"))
        if(self.pognon<mise):
            print("Vous n'avez pas suffisament d'argent!!!")
            raise ValueError
        return mise
        
    def lancerLaRoulette(self,_numero,_mise):
        resultat = random.randrange(0,50)
        if(_numero % 2 == 1):
            couleurChoisie = "noire"
        else:
            couleurChoisie = "rouge"
        if(resultat %2 == 1):
            couleurTiree = "noire"
        else:
            couleurTiree = "rouge" 
        print("\nresultat:{}\n".format(resultat))
        if(resultat == _numero):
            self.pognon += _mise*3
            print("jackpot!!!!!\n")
        elif(couleurChoisie == couleurTiree):
            self.pognon += math.ceil(_mise * 0.5)
            print("vous avez choisi la case {0} de couleur {1}, or, la boule est tombée sur une case {1} donc gagné!!!\n".format(_numero,couleurChoisie))
        else:
            self.pognon -= _mise
            print("vous avez choisi la case {0} de couleur {1}, or, la boule est tombée sur une case {2} donc perdu!!!\n".format(_numero,couleurChoisie,couleurTiree))
        
        
    def infraction(self):
        self.nombreDInfractions += 1
        if(self.nombreDInfractions == 5):
            self.Sortez("Tricherie")
            raise ValueError
                    
class Machine_a_sous:
    __metaclass__ = MetaCasino
    pass
    
activite = str(input("choisissez l'activité:"))
if("Roulette" in activite):
    roulette = Roulette()


