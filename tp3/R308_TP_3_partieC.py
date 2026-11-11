  # ---------- Partie C (1re moitié : sauvegarde) ----------
    def sauvegarder(self, fichier="livres.csv"):
        with open(fichier, "w", newline="", encoding="utf-8") as f:
            ecrivain = csv.writer(f)
            ecrivain.writerow(["titre", "auteur", "annee", "disponible", "emprunteur"])
            for livre in self.livres.values():
                ecrivain.writerow([livre.titre, livre.auteur, livre.annee,
                                   livre.disponible, livre.emprunteur])