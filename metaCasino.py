import random
import math
import sys

print("Bienvenue au  Casino!!!\n")
print("Liste des activités:")

def FoutreLeClientDehors(self,raison):
    print("On vous a jeté hors du Casino. Motif: {}".format(raison))

def infraction(self):
        self.nombreDInfractions += 1
        assert(self.nombreDInfractions != 5)

class BetweenKeyboardAndChairException(Exception):
    #Décrit une exception ayant lieu lorsque le client fait le c**
    def __init__(self,raison):
        self.raison = raison
    
    def __str__(self):
        return self.raison
    
class MetaCasino(type):
    #MetaCasino est une métaclasse singleton
    def __new__(metacls, nom, bases, attributs):
        print("\t{}".format(nom))                   #affichage de la liste des activités
        attributs["Sortez"] = FoutreLeClientDehors
        attributs["pognon"] = 1000                  #argent disponible dans les differentes activités
        attributs["nombreDInfractions"] = 0         #compte les infractions
        attributs["infraction"] = infraction        #incremente nombreDInfractions, retourne une AssertionError lors que nombreDInfractions == 5
        return type.__new__(metacls, nom, bases, attributs)
        
class Roulette(metaclass = MetaCasino):
    #Roulette est classe ayant pour métaclasse MetaCasino
    #L'initialisation lance le jeu
    def __init__(self):
        #on met des self partout pour faire plaisir à python
        print("Roulette: La roulette possède 50 cases numérotées de 0 à 49. Les cases impaires sont noires, les cases paires sont rouges. Si vous tombez sur la case sur laquelle vous avez parié, votre mise est triplée. Si vous tombez sur une case de même couleur, on vous rend 150% de la mise, sinon, la mise est perdue\n")
        while(self.pognon>0):
            #boucle qui s'execute tant que le client/victime(rayez la mension inutile) possède de l'argent
            try:
                print("vous disposez de {}€".format(self.pognon))
                try:
                    numero = self.demanderNumero()
                    mise = self.demanderMise()
                except:
                    print("Erreur dans la saisie, veuillez réessayer...")
                    self.infraction()
                    continue
                self.lancerLaRoulette(numero,mise)
            except AssertionError:      #exception levée après 5 erreurs de frappe
                self.Sortez("Tricherie")
                break
        if(not self.pognon>0):self.Sortez("Vous n'avez plus d'argent")
    
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
        assert(self.nombreDInfractions != 5)
            
                    
class Machine_a_sous(metaclass = MetaCasino):
    #Machine_a_sous est classe ayant pour métaclasse MetaCasino
    #L'initialisation lance le jeu
    def __init__(self):
        try:
            while(self.pognon>=100):
                #boucle qui s'execute tant que le pigeon a suffisament d'argent pour jouer
                print("\nvous avez {}€".format(self.pognon))
                entree = input("Entrez \"tirer\" pour tirer le levier, \"mettre un coup de pied dans la machine\" pour sortir\n")
                if(entree == "tirer"):
                    self.tirerLeLevier()
                elif(entree == "mettre un coup de pied dans la machine"):#c'est mal
                    raise BetweenKeyboardAndChairException("Vous êtes un abruti")#bien fait
                else:
                    self.infraction() #exception levée après 5 erreurs de frappe
                    print("Erreur dans la saisie, veuillez réessayer...")
            self.Sortez("vous n'avez plus assez d'argent")
        except(AssertionError):
            self.Sortez("Tricherie")
        except(BetweenKeyboardAndChairException):
            self.Sortez("déterioration de materiel")
        
    def tirerLeLevier(self):
        self.pognon -= 100
        (a,b,c) = (random.randrange(0,10),random.randrange(0,10),random.randrange(0,10))
        print(a,b,c)
        if(a==b and b==c):
            print("Jackpot!!!!!!")
            self.pognon += 600
        elif(a==b or b==c):
            print("gagné!")
            self.pognon += 200
        else:
            print("perdu!")
            

class Loto(metaclass = MetaCasino):
    #Loto est classe ayant pour métaclasse MetaCasino
    #L'initialisation lance le jeu
    def __init__(self):
        self.Sortez("Activité indisponible")



    
activite = str(input("choisissez l'activité:"))
if(("Roulette" in activite) or ("roulette" in activite)):
    roulette = Roulette()
elif(((("Machine" or "machine") and "a" and "sous")in activite) or ("Machine_a_sous" in activite)):
    machine = Machine_a_sous()
elif(("Loto" in activite) or ("loto" in activite)):
    loto = Loto()


