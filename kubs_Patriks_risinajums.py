class Kubs():
    def __init__(self, malas_garums, krasa):
        if malas_garums>=2 and malas_garums<=10:
            self.malas_garums=malas_garums
        else:
            print("Malas garums neatbilst!")
            self.malas_garums=2
        self.krasa=krasa
    def aprekinat_tilpumu(self):
        tilpums=self.malas_garums**3
        return tilpums
    
class Bloks(Kubs):
    def __init__(self, malas_garums, krasa, kubu_skaits,forma):
        super().__init__(malas_garums, krasa)
        if kubu_skaits>=1 and kubu_skaits<=4:
            self.kubu_skaits=kubu_skaits
        else:
            print("Kubu skaits neatbilst!")
            self.kubu_skaits=1
        self.nosaukums=str(self.krasa)+str(self.kubu_skaits) #izveido nosaukumu

        formas_vertibas=[11,12,13,14,22]
        if forma not in formas_vertibas:
            print("Nepareiza forma!")
            self.derigums=0
        else:
            self.derigums=1

    def tilpums(self):
        tilpums=self.malas_garums**3
        bloka_tilpums=tilpums*self.kubu_skaits
        return bloka_tilpums

    def mainit_formu(self,jauna_forma):
        formas_vertibas=[11,12,13,14,22]
        if jauna_forma not in formas_vertibas:
            print("Nepareiza forma!")
            self.derigums=0
        else:
            self.derigums=1


print("Oranžs objekts: ")
orange3=Bloks(5,"oranžs",3,13)
print(orange3.nosaukums, orange3.tilpums())

print("Zils objekts: ")
blue5=Bloks(7,"zila",5,23)
print(blue5.nosaukums, blue5.malas_garums,blue5.derigums)

print("Mainīta forma:")
blue5.mainit_formu(12)
print(blue5.nosaukums, blue5.malas_garums,blue5.derigums)