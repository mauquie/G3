"""
Pas terminé, il reste une erreur à corriger.
"""

from collections import namedtuple


Card = namedtuple('Card', ['color', 'fig'])

CardValues = dict(zip('23456789XVDRA', range(2, 15)))

HandNames = {
    1:'Hauteur',
    2:'Paire',
    3:'Deux paires',
    4:'Brelan',
    5:'Suite',
    6:'Couleur',
    7:'Full',
    8:'Carré',
    9:'Quinte flush',
    10:'Quinte flush royale'}

Levels = {
    (1,1,1,1,1):1,
    (2,1,1,1):2,
    (2,2,1):3,
    (3,1,1):4,
    (3,2):7,
    (4,1):8}


class Combinaison:
    def __init__(self, cardlist):
        cards = [Card(c.couleur, c.valeur) for c in cardlist]
        figures,colors = zip(*[(c.fig,c.color) for c in cards])
        # teste si c'est une couleur
        flush = len(set(colors)) == 1
        # teste si c'est une suite
        values = sorted([CardValues[fig] for fig in set(figures)])
        straight = (len(values)==5) and (values[0]+4 == values[4])
        # calcule le nombre d'occurences de chaque figure
        nvals=dict().fromkeys(figures, 0)
        for f in figures:
            nvals[f]+=1
        # détermine la force de la main
        if straight and flush:
            self.level = (10 if values[4]==CardValues['A'] else 9)
        elif flush:
            self.level = 6
        elif straight:
            self.level = 5
        else:
            self.level = Levels[tuple(sorted(nvals.values(), reverse=True))]
        # trie les cartes pour une comparaison éventuelle
        self.cards = sorted(cards, key=lambda c:CardValues[c.fig]+(15*nvals[c.fig]), reverse=True)

    def name(self):
        return HandNames[self.level]

    def __lt__(self, other):
        if self.level != other.level:
            return self.level < other.level
        else:
            return [CardValues[c.fig] for c in self.cards] < [CardValues[c.fig] for c in other.cards]

    def __gt__(self, other):
        if self.level != other.level:
            return self.level > other.level
        else:
            return [CardValues[c.fig] for c in self.cards] > [CardValues[c.fig] for c in other.cards]

    def __eq__(self, other):
        if other == None:
            pass
        else:
            if self.level != other.level:
                return False
            else:
                return [CardValues[c.fig] for c in self.cards] == [CardValues[c.fig] for c in other.cards]

    def __repr__(self):
        return ' '.join([c.color + c.fig for c in self.cards])


class Duck:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    def __repr__(self):
        return self.valeur + self.couleur

def testmodule():
    cards = [
        [Duck(str(i), 'P' if i<5 else 'T') for i in [2,3,4,5,5]],
        [Duck('X','C') for _ in range(3)] + [Duck('R','P') for _ in range(2)]]
    for c in cards: print(c)
    hands = [Combinaison(c) for c in cards]
    for h in hands: print(h, h.name())
    print(hands[0] > hands[1])
    hands.sort(reverse=True)
    for h in hands: print(h, h.name())


if __name__ == '__main__':
    testmodule()
