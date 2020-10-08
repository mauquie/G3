"""
Pas terminé, il reste une erreur à corriger.
"""

import random
import pokerlib



class Partie:
    """Représente la partie en cours."""

    joueurs = []
    joueurs_participants = []
    joueurs_non_participants = []

    def __init__(self, tapis=50, mise=10):
        """Initialisation du nombre de jetons (mise) par joueur et de sa mise"""
        self.tapis = tapis
        self.mise = mise
    
    def ajouter(self, nom="Paulette"):
        """Ajout d'un nouveau joueur"""
        joueur = Joueur(self.tapis, nom)
        self.joueurs.append(joueur)

    def jouer(self):
        """Détermine les joueurs pouvant jouer au prochain coup"""
        for i in range(len(self.joueurs)):
            if self.verif(self.joueurs[i].tapis):
                self.joueurs_participants.append(self.joueurs[i])
            else:
                self.joueurs_non_participants.append(self.joueurs[i])

    def verif(self, tapis_joueur):
        """Détermine si un joueur est participant ou non, complémentaire de la def jouer"""
        if tapis_joueur >= self.mise:
            return True
        return False
                
    def __repr__(self):
        """Affiche le nombre de joueurs total de la partie ainsi que le nombre de joueur participant"""
        return f"La partie comporte {len(self.joueurs)} joueur{' ' if len(self.joueurs) < 2 else 's '} : {[self.joueurs[i].nom for i in range(len(self.joueurs))]}, \ndont {len(self.joueurs_participants)} joueur{' ' if len(self.joueurs_participants) < 2 else 's '} participant au prochain coup : {[self.joueurs_participants[i].nom for i in range(len(self.joueurs_participants))]}"
      


class Joueur:
    """Représente un joueur de la partie."""
    
    def __init__(self, tapis, nom):
        """Donne des atributs à la classe joueur"""
        self.nom = nom
        self.main = []
        self.tapis = tapis
        self.combinaison = None

    def evaluer(self):
        """Donne une valeur à chaque carte"""
        combinaison1 = pokerlib.Combinaison(self.main)
        self.combinaison = combinaison1

    def nouvelle_main(self):
        """Réinitialise la main et la combinaison des joueurs"""
        self.main.clear()
        self.combinaison = None

    def recevoir_cartes(self, carte):
        """Attribue 5 cartes à chaque joueur"""
        self.main.append(carte)
    
    def __repr__(self):
        """Affiche le nom du joueur ainsi que son nombre de jetons et sa main"""
        return f"\n{self.nom} a {self.tapis} jetons et a une main telle que : {[self.main[i] for i in range(len(self.main))]} donc : {'pas de combinaison' if self.combinaison == None else self.combinaison.name()}"




class Coup(Partie):
    """Représente les actions de la partie."""
    
    def __init__(self):
        super().__init__()
        self.gagnant = None

    def abattre(self):
        """Détermine le gagnant de cette manche"""
        main_joueurs = []
        for i in range(len(self.joueurs_participants)):
            main_joueurs.append(self.joueurs_participants[i].combinaison)
        
        combinaison_max = max(main_joueurs)
        for i in range(len(main_joueurs)):
            if main_joueurs[i] == combinaison_max:
                self.gagnant = self.joueurs_participants[i]

        jetons_en_jeu = 0
        for i in range(len(self.joueurs_participants)):
            self.joueurs_participants[i].tapis -= self.mise
            jetons_en_jeu += self.mise
        self.gagnant.tapis += jetons_en_jeu
        



class Croupier(Coup):
    """Représente le croupier de la partie."""

    def __init__(self):
        super().__init__()
        self.paquet = []
    
    def rassembler(self):
        """Reprend toutes les cartes de chaque joueur"""
        for couleur in "PCKT":
            for valeur in [2, 3, 4, 5, 6, 7, 8, 9, "X", "V", "D", "R", "A"]:
                carte = Carte(couleur, valeur)
                self.paquet.append(carte)
    
    def melanger(self):
        """Mélange les cartes"""
        random.shuffle(self.paquet)

    def couper(self):
        """Coupe le paquet en deux"""
        for i in range(random.randint(1, len(self.paquet))):
            self.paquet.append(self.paquet[0])
            self.paquet.pop(0)

    def nouvelle_donne(self):
        """Prépare les cartes à un nouveau tour"""
        self.rassembler()
        self.melanger()
        self.couper()
    
    def distribuer(self, n):
        """Attribue 5 cartes à chaque joueur participant"""
        for i in range(len(self.joueurs_participants)):
            for j in range(n):
                self.joueurs_participants[i].recevoir_cartes(self.paquet[len(self.paquet)-1])
                self.paquet.pop()

    def __repr__(self):
        """Affiche le paquet de carte de la partie"""
        result = []
        for carte in self.paquet:
            result.append(str(carte))
        return "\n".join(result)



class  Carte:
    """Représente une carte à jouer."""

    def __init__(self, couleur="T", valeur=2):
        self.valeur=str(valeur)
        self.couleur=couleur
    

    noms_couleurs = {"T": "trèfle", "K": "carreau", "C": "cœur", "P": "pique"}
    noms_valeurs = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "X": "10", "V": "valet", "D": "dame", "R": "roi", "A": "as"}

    def __repr__(self):
        """Affiche le nom de la carte"""
        return f"{Carte.noms_valeurs[self.valeur]} de {Carte.noms_couleurs[self.couleur]}"
