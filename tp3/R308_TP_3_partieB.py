# ---------- Partie B ----------
class Bibliotheque:
    def __init__(self):
        self.livres = {}        # titre -> Livre
        self.utilisateurs = {}  # nom -> Utilisateur

    def ajouter_livre(self, livre):
        self.livres[livre.titre] = livre

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs[utilisateur.nom] = utilisateur

    def emprunter(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False
        if titre not in self.livres:
            print("Livre inconnu.")
            return False
        if not self.utilisateurs[nom].emprunter_livre(self.livres[titre]):
            print("Livre déjà emprunté.")
            return False
        return True

    def rendre(self, nom, titre):
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False
        if titre not in self.livres:
            print("Livre inconnu.")
            return False
        if not self.utilisateurs[nom].rendre_livre(self.livres[titre]):
            print("Ce livre n'a pas été emprunté par cet utilisateur.")
            return False
        return True

    def afficher_livres(self):
        print("--- Disponibles ---")
        for livre in self.livres.values():
            if livre.disponible:
                livre.afficher()
        print("--- Empruntés ---")
        for livre in self.livres.values():
            if not livre.disponible:
                livre.afficher()