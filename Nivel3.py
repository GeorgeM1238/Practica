class Motor:
    pass

class Masina(Motor):
    def porneste(self):
        print("Masina a pornit")

    def opreste(self):
        print("Masina s-a oprit")

    def __str__(self):
        return "Masina a pornit"
    def __eq__(self, other):
        return
class Carte:
    def __init__(self, titlu, autor, an):
        self.titlu = titlu
        self.autor = autor
        self.an = an

    def descriere(self):
        print(f"Carte {self.titlu} scrisa de {self.autor} este o carte SF")

    def __eq__(self, other):
        return self.titlu == other.titlu and self.autor == other.autor


m1=Masina()
c1=Carte("Carte1","Autor1",2005)
c2=Carte("Carte1","Autor1",2010)
c3=Carte("Carte3","Autor2",2011)

print(c1==c2)

print(str(m1))