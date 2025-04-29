from datetime import date
class Pasakums():
    def __init__(self, veids, datums, skaits):
        print('Sveicināti pasākumu plānotājā!')
        while True:
            print('Pasākumi veidi: ', '\n1 - Koncerts', '\n2 - Festivals', '\n3 - Sacencibas')
            ievade = int(input('Ievadiet kuru no pasākumiem apmeklēsiet (1, 2 vai 3): '))

            if ievade == 1:
                self.veids = 'koncerts'
                break
            elif ievade == 2:
                self.veids = 'festivals'
                break
            elif ievade == 3: 
                self.veids = 'sacencibas'
                break
            else:
                print('Ievadiet ciparu no 1 līdz 3!')
                print('-'*17)
        
        while True:
            print('Pieejami datumi : ')
            for i,dat in enumerate(datumi[veids],1): #cikls konsolē parādīs pieejamos datumus
                print(f"{i} - {dat}")

            liet_datums = int(input('Ievadiet sev vēlamo datumu: '))
            #validāciju ievadītajam datumam(1,2,3)

            if 1<=liet_datums<=len(datumi[veids]):
                izveletais_dat=datumi[veids][liet_datums-1]
                break 
            else:
                print('Ievadiet pieejamu datuma kārtas numuru!')
                print('-'*17)
        self.datums=izveletais_dat
        while True:
            print('Pieejamo biļešu skaits: ', self.brivas_vietas(veids)) 

            self.skaits = int(input('Cik biļetes vēlaties: '))

            if self.skaits > self.ietilpiba:
                print('Nav pietikama pasākuma ietilpība!')
                print('-'*17)
            else:
                break

    '''ietilpiba = { #vārdnīca ar katra pasākuma max ietilpibu
    'koncerts' : 90,
    'festivals': 200,
    'sacencibas' : 120
    }

    cena = { #vārdnīca ar katra pasākuma biļetes cenu
        'koncerts' : 15,
        'festivals': 8,
        'sacencibas' : 12
    }

    datumi = { #vārdnīca ar pasākumu datumiem
            'koncerts' : [date(2025, 6, 12), date(2025, 7, 21) ,date(2025, 10, 16)],
            'festivals': [date(2025, 6, 6), date(2025, 6, 28), date(2025, 7, 13), date(2025, 8, 5)],
            'sacencibas' : [date(2025, 7, 30), date(2025, 9, 2), date(2025, 11, 17)] }
    '''
            
    def dienas_lidz_pasakumam(datums):
        return 

    def aprekinat_biletes(skaits, veids): #funkcija ar padotajiem parametriem (ko ievada lietotājs), atgriež kopējo cenu
        return 

    def brivas_vietas(kas): # funkcija atgriež cik brīvas vientas ir izvēlētajā pasākumā
        return
    
    


class Koncerts(Pasakums):
    def __init__(self, veids, datums,cena, ietilpiba):
        super().__init__(veids, datums)
        self.ietilpiba=ietilpiba
        ietilpiba=90
        self.cena=cena
        cena=15
        while True:
            print('Pieejamo biļešu skaits: ', self.brivas_vietas(veids)) 

            self.skaits = int(input('Cik biļetes vēlaties: '))

            if self.skaits > self.ietilpiba:
                print('Nav pietikama pasākuma ietilpība!')
                print('-'*17)
            else:
                break

    def dienas_lidz_pasakumam(self):
        sodien = date.today()
        diff = (self.datums - sodien).days
        return diff
    def aprekinat_biletes(self): #funkcija ar padotajiem parametriem (ko ievada lietotājs), atgriež kopējo cenu
        biletes_cena_kopa = (self.skaits)*self.cena
        return biletes_cena_kopa

    def brivas_vietas(self): # funkcija atgriež cik brīvas vientas ir izvēlētajā pasākumā
        return(self.ietilpiba)
'''
    print('-'*17) #Konsolē parāda "čeku"
    print('Pasākuma veids: ', veids)
    print('Datums: ', izveletais_dat)
    print('Dienas līdz pasākumam: ',dienas_lidz_pasakumam(izveletais_dat))
    print('Kopējā biļēšau cena: ', aprekinat_biletes(bilesu_sk, veids), 'EUR')
    print('\nPaldies par iepirkšanos!') '''

pasakums1=Koncerts(Pasakums)
pasakums1.dienas_lidz_pasakumam()