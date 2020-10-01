import random



class Partie:

    joueurs = []

    def __init__(self, tapis=50):
        self.tapis = tapis
    
    def jouer(self, nom="Paulette"):
        joueur = Joueur(self.tapis, nom)
        Partie.joueurs.append(joueur)

    def __repr__(self):
      return f"La partie comporte {len(Partie.joueurs)} joueurs : \n{[Partie.joueurs[i].nom for i in range(len(Partie.joueurs))]}"
      


class Joueur:
    """Représente un joueur de la partie."""
    
    def __init__(self, tapis, nom):
        self.nom = nom
        self.main = []
        self.tapis = tapis
        self.combinaison = None

    def evaluer(self):
        pass

    def nouvelle_done(self):
        self.main.clear()

    def recevoir_cartes(self, carte):
        self.main.append(carte)
    
    def __repr__(self):
        return f"{self.nom} a {self.tapis} jetons et a une main telle que : {[self.main[i] for i in range(len(self.main))]}"



class Coup(Partie):
    """Représente les actions de la partie."""
    
    def __init__(self):
      super().__init__()

    def distribuer(self):
        Croupier.distribuer(Croupier(), 5)



class Croupier(Coup):
    """Représente le croupier de la partie."""

    def __init__(self):
        super().__init__()
        self.paquet = []
    
    def rassembler(self):
        for couleur in "PCKT":
            for valeur in [2, 3, 4, 5, 6, 7, 8, 9, "X", "V", "D", "R", "A"]:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)
    
    def melanger(self):
        random.shuffle(self.paquet)

    def couper(self):
        for i in range(random.randint(1, len(self.paquet))):
            self.paquet.append(self.paquet[0])
            self.paquet.pop(0)

    def nouvelle_donne(self):
        self.rassembler()
        self.melanger()
        self.couper()
    
    def distribuer(self, n):
        for i in range(len(Partie.joueurs)):
            for j in range(n):
                Coup.joueurs[0].recevoir_cartes(self.paquet[0])
                self.paquet.pop(0)

    def __repr__(self):
        result = []
        for carte in self.paquet:
            result.append(str(carte))
        return "\n".join(result)



class  Carte:
    """Représente une carte à jouer."""

    def __init__(self, valeur=2, couleur="T"):
        self.valeur=valeur
        self.couleur=couleur
    

    noms_couleurs = {"T": "trèfle", "K": "carreau", "C": "cœur", "P": "pique"}
    noms_valeurs = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", "X": "10", "V": "valet", "D": "dame", "R": "roi", "A": "as"}

    def __repr__(self):
        return f"{Carte.noms_valeurs[self.valeur]} de {Carte.noms_couleurs[self.couleur]}"