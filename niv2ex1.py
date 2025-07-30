class Animal:
    def __init__(self, culoare, coada, urechi):
        self.culoare = culoare
        self.coada = coada
        self.urechi = urechi

    def sunet(self):
        print("Animal")

class Caine(Animal):
    def __init__(self, culoare, coada, urechi):
        super().__init__(culoare, coada, urechi)

    def sunet(self):
        print("Miau")

    def get_culoare(self):
         return self.culoare  # access public attribute

class Pisica(Animal):
    def __init__(self, culoare, coada, urechi):
        super().__init__(culoare, coada, urechi)

    def sunet(self):
        print("Ham")

    def get_coada(self):
        return self.coada  # fix typo and access public attribute


caine1 = Caine("neagra", "scurta", "lungi")
caine2 = Caine("alba", "lunga", "scurte")
pisica1 = Pisica("maro", "lunga", "scurte")
pisica2 = Pisica("portocaliu", "scurta", "lungi")

list_animale = [caine1, caine2, pisica1, pisica2]

caine1.sunet()        # Miau
pisica1.sunet()       # Ham
print(caine1.get_culoare())  # neagra
print(pisica1.get_coada())   # lunga
