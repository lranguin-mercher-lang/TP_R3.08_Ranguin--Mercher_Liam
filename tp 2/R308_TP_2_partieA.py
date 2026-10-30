def grille () : 
    return [[" " , " " , " "], [" " , " " , " "], [" " , " " , " "]]

def afficher(g):
    for ligne in g:
        print("|" .join(ligne) )

def jouer(g, ligne, colonne, symbole):
    g[ligne][colonne] = symbole
g = grille()

jouer(g, 0, 2, "O")
afficher(g)

if g[0][0] == g[0][1] and g[0][1] == g[0][2] and g[0][0] != " ":
    print("gagné")

