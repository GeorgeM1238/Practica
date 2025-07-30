class Student:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def printeaza(self, nume, varsta):
        print(f"Salut,eu sunt {nume}")

    def varsta1(self):
        if self.varsta > 1 and self.varsta < 18:
            print("Studentul este minor")
        elif self.varsta > 18:
            print("Studentul este major")


s1 = Student("Dorin", 14)
s2 = Student("Adrian", 18)
S3 = Student("Robert", 19)


