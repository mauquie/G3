class Partie:
    
    def __init__(self):
        self.joueurs = []

    def jouer(self):
        pass


class Joueur:
    
    def __init__(self, nom="Paulette"):
        self.nom = nom
        self.main = []
        self.tapis = int
        self.combinaison = "" #Combinaison

    def evaluer(self):
        pass

    def nouvelle_done(self):
        pass

    def recevoir_cartes(self):
        pass


class Coup:
    
    def __init__(self):
        pass

    def abattre(self):
        pass

    def distribuer(self):
        pass


class Croupier:
    
    def __init__(self):
        self.paquet = []

    def nouvelle_done(self):
        pass

    def rassembler(self):
        pass

    def melanger(self):
        pass

    def couper(self):
        pass

    def distribuer(self):
        pass


class  Carte:
    
    def __init__(self):
        self.couleur = 1