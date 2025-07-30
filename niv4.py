class Forma:
    def arie(self):
        pass

class Dreptunghi(Forma):
    def arie(self):
        pass

class Cerc(Forma):
    def arie(self):
        pass


class Cont:
    def retragere(self):
        print("s-au depus bani in cont")
    def depunere(self):
        print("s-a verificat soldul in cont")
    def sold(self):
        print("s-au retras bani din cont")


class ContEconomii(Cont):
    def depunere(self):
        print("s-au depus bani in c e")
    def sold(self):
        print("s-a verificat soldul in c e")
    def retragere(self):
        print("s-au retras bani din c e")
class ContCurent(Cont):
    def depunere(self):
        print("s-au depus bani in c c")
    def sold(self):
        print("s-a verificat soldul in c c")
    def retragere(self):
        print("s-au retras bani din c c")



c=Cont()
ce=ContEconomii()
cc=ContCurent()

c.depunere()
ce.sold()
cc.retragere()