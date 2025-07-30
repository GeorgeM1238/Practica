class Carte:
    def __init__(self, titlu, autor, an):
        self.titlu = titlu
        self.autor = autor
        self.an = an

    def descriere(self):
        print(f"Carte {self.titlu} scrisa de {self.autor} este o carte SF")

class Biblioteca:
    def __init__(self, carti=None):
        # Initialize with an empty list if none provided
        if carti is None:
            self.carti = []
        else:
            self.carti = carti

    def adaugarecarte(self, carte):
        self.carti.append(carte)

    def listare(self):
        for carte in self.carti:
            print(f"{carte.titlu} este scrisa de {carte.autor}")

    def cautare(self, titlu):
        for carte in self.carti:
            if carte.titlu == titlu:
                print(f"Gasit: {carte.titlu} scrisa de {carte.autor}")
                return
        print("Carte negasita")

# Create some books
carte1 = Carte("titlu1", "autor1", 1999)
carte2 = Carte("titlu2", "autor2", 1995)
carte3 = Carte("titlu3", "autor3", 2007)

# Create a biblioteca with initial books
biblioteca = Biblioteca([carte1, carte2, carte3])

# List books
biblioteca.listare()

# Add a new book
carte4 = Carte("titlu4", "autor4", 2010)
biblioteca.adaugarecarte(carte4)

print("\nDupa adaugare:")
biblioteca.listare()

# Search for a book
biblioteca.cautare("titlu2")
biblioteca.cautare("titluX")
