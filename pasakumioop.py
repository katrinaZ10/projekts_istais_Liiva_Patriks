from datetime import date
from abc import ABC,abstractmethod


#abstraktā bāzes klase
class Pasakums():
    def __init__(self, nosaukums, datumi, ietilpiba,cena):
        self.nosaukums=nosaukums
        self.datumi=datumi
        self.ietilpiba=ietilpiba
        self.cena=cena

    @abstractmethod
    def aprekinat_cenu(self,biletes_skaits):
        pass

    def brivas_vietas(self):
        return self.ietilpiba

    def dienas_lidz_pasakumam(self,datums):
        return (datums - date.today()).days



#3 apakšklases
class Koncerts(Pasakums):
    def aprekinat_cenu(self,biletes_skaits):
        #atlaide
        if biletes_skaits>5:
            return round(biletes_skaits*self.cena*0.5,0)
        return self.cena*biletes_skaits

#festivals #katra 10ta bez maksas
class Festivals(Pasakums):
    def aprekinat_cenu(self,biletes_skaits):
        bilete = (range(10,210,10))
        if biletes_skaits in bilete:
            return round(biletes_skaits-(biletes_skaits/10)*self.cena,0)
        return self.cena*biletes_skaits
#sacensibas #nav atlaides
class Sacensibas(Pasakums):
    def aprekinat_cenu(self,biletes_skaits):
        return self.cena*biletes_skaits

class PasakumuPlanotajs:
    def __init__(self):
        self.pasakums = {
            'koncerts' : Koncerts('koncerts',[date(2025, 6, 12), date(2025, 7, 21) ,date(2025, 10, 16)],90,15),
            'festivals': Festivals('festivals',[date(2025, 6, 6), date(2025, 6, 28), date(2025, 7, 13), date(2025, 8, 5)],200,8),
            'sacencibas' : Sacensibas('sacensibas',[date(2025, 7, 30), date(2025, 9, 2), date(2025, 11, 17)],120,12)
        }

    def izveleties_pasakumu(self):
       while True:
            try:
                print('Pasākumi veidi: ', '\n1 - Koncerts', '\n2 - Festivals', '\n3 - Sacencibas')
                ievade = int(input('Ievadiet kuru no pasākumiem apmeklēsiet (1, 2 vai 3): '))
                veidi= {1 : 'koncerts',2: 'festivals',3: 'sacensibas'}
                if ievade in veidi:
                    return veidi[ievade]
                else:
                    print('Ievadiet ciparu no 1 līdz 3!')
                    print('-'*17)
        
            except ValueError:
                print('Lūdzu ievadiet skaitli!')

    def izveleties_datumu(self,pasakums): #while true
        while True:
            try:
                print('Pieejami datumi : ')
                for i,dat in enumerate,(pasakums.datumi,1): #cikls konsolē parādīs pieejamos datumus
                    print(f"{i} - {dat}")

                liet_datums = int(input('Ievadiet sev vēlamo datumu: '))
                #validāciju ievadītajam datumam(1,2,3)

                if 1<=liet_datums<=len(pasakums.datumi):
                    return pasakums.datumi[liet_datums-1]
                    
                else:
                    print('Ievadiet pieejamu datuma kārtas numuru!')
                    print('-'*17)
            except ValueError:
                print('Lūdzu ievadiet skaitli!')

    def izveleties_biletes(self,pasakums):#while true #except
        while True:
            try:
                print('Pieejamo biļešu skaits: ', pasakums.brivas_vietas())
                bilesu_sk = int(input('Cik biļetes vēlaties: '))
                #nevar būt < par 0
                if bilesu_sk<0<=pasakums.brivas_vietas():
                    return bilesu_sk
                else:
                    print('Nav pietikama pasākuma ietilpība!')
                    print('-'*17)
            except ValueError:
                print('Lūdzu ievadiet skaitli!')

    def sakt(self):

        veids=self.izveleties_pasakumu()
        pasakums=self.pasakumi[veids]
        # datumam un bilesu skatitam
        
        datums=self.izveleties_datumu(pasakums)
        biletes=self.izveleties_biletes(pasakums)


        print('-'*17) #Konsolē parāda "čeku"
        print('Pasākuma veids: ', pasakums) #nosaukums
        print('Datums: ', pasakums.datums)
        print('Dienas līdz pasākumam: ',pasakums.dienas_lidz.dienas_lidz_pasakumam)
        print('Kopējā biļēšau cena: ', pasakums.aprekinat_cenu(biletes), 'EUR')
        print('\nPaldies par iepirkšanos!')

    

    
