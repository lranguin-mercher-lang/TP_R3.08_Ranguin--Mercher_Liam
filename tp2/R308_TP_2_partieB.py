import random

VIDE = " "


class JoueurHumain:
    def prochain_coup(self, tab, symbole):
        while True:
            try:
                x = int(input(f"Joueur {symbole} - ligne : "))
                y = int(input(f"Joueur {symbole} - colonne : "))
                return (x, y)
            except ValueError:
                print("Entre un nombre entier, pas autre chose.")


class JoueurIA:
    def prochain_coup(self, tab, symbole):
        libres = []
        for x in range(3):
            for y in range(3):
                if tab[x][y] == VIDE:
                    libres.append((x, y))
        return random.choice(libres)