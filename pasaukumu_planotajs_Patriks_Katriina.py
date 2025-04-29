from datetime import date #importē datime, lai var aprēķināt cik dienas līdz festivālam

<<<<<<< Updated upstream
=======
koncerts1 = date(2025, 6, 12)
koncerts2 = date(2025, 7, 21)
koncerts3 = date(2025, 10, 16)

#[date(2025, 6, 6), date(2025, 6, 28), date(2025, 7, 13), date(2025, 8, 5)]
'''festivals1 : date(2025, 6, 6),
        festivals2 : date(2025, 6, 28),
        festivals3 : date(2025, 7, 13),
        festivals4 : date(2025, 8, 5)'''

festivals1 = '6. jūnijs'
festivals2 = '28. jūnijs'
festivals3 = '13. jūlijs'
festivals4 = '5. augusts'



>>>>>>> Stashed changes
datumi = { #vārdnīca ar pasākumu datumiem
    'koncerts' : [date(2025, 6, 12), date(2025, 7, 21) ,date(2025, 10, 16)],
    'festivals': [date(2025, 6, 6), date(2025, 6, 28), date(2025, 7, 13), date(2025, 8, 5)],
    'sacencibas' : [date(2025, 7, 30), date(2025, 9, 2), date(2025, 11, 17)]
}

ietilpiba = { #vārdnīca ar katra pasākuma max ietilpibu
    'koncerts' : 90,
    'festivals': 200,
    'sacencibas' : 120
}

cena = { #vārdnīca ar katra pasākuma biļetes cenu
    'koncerts' : 15,
    'festivals': 8,
    'sacencibas' : 12
}
class Rekini():
    def aprekinat_biletes(skaits, veids): #funkcija ar padotajiem parametriem (ko ievada lietotājs), atgriež kopējo cenu
        biletes_cena_kopa = skaits*cena[veids]
        return biletes_cena_kopa

<<<<<<< Updated upstream

def aprekinat_biletes(skaits, veids): #funkcija ar padotajiem parametriem (ko ievada lietotājs), atgriež kopējo cenu
    biletes_cena_kopa = (skaits)*cena[veids]
    return biletes_cena_kopa

def brivas_vietas(kas): # funkcija atgriež cik brīvas vientas ir izvēlētajā pasākumā
    return(ietilpiba[kas])
        
def dienas_lidz_pasakumam(datums):
    sodien = date.today()
    diff = (datums - sodien).days
    return diff
=======
    def brivas_vietas(veids):
        return ietilpiba[veids]
        
    def laiks():
        from datetime import date

        sodien = date.today()
        datums = date(2025, 7, 30)
        diff = datums - sodien
        print(diff.days)


>>>>>>> Stashed changes


print('Sveicināti pasākumu plānotājā!')

try:
    while True:
        print('Pasākumi veidi: ', '\n1 - Koncerts', '\n2 - Festivals', '\n3 - Sacencibas')
        ievade = int(input('Ievadiet kuru no pasākumiem apmeklēsiet (1, 2 vai 3): '))

        if ievade == 1:
            veids = 'koncerts'
            break
        elif ievade == 2:
            veids = 'festivals'
            break
        elif ievade == 3: 
            veids = 'sacencibas'
            break
        else:
            print('Ievadiet ciparu no 1 līdz 3!')
            print('-'*17)

<<<<<<< Updated upstream
    while True:
        print('Pieejami datumi : ')
        for i,dat in enumerate(datumi[veids],1): #cikls konsolē parādīs pieejamos datumus
            print(f"{i} - {dat}")

        liet_datums = int(input('Ievadiet sev vēlamo datumu: '))
        #validāciju ievadītajam datumam(1,2,3)
=======
        #print(f'{veids} pieejamie datumI: ','\n1  - [veids]')
    #for i in datumi[veids]:
    print(datumi[veids])
>>>>>>> Stashed changes

        if 1<=liet_datums<=len(datumi[veids]):
            izveletais_dat=datumi[veids][liet_datums-1]
            break 
        else:
            print('Ievadiet pieejamu datuma kārtas numuru!')
            print('-'*17)
            
    while True:
        print('Pieejamo biļešu skaits: ', brivas_vietas(veids)) 

<<<<<<< Updated upstream
        bilesu_sk = int(input('Cik biļetes vēlaties: '))

        if bilesu_sk > ietilpiba[veids]:
            print('Nav pietikama pasākuma ietilpība!')
            print('-'*17)
        else:
            break

        
except ValueError:
            print('Lūdzu ievadiet skaitli!')
        

print('-'*17) #Konsolē parāda "čeku"
print('Pasākuma veids: ', veids)
print('Datums: ', izveletais_dat)
print('Dienas līdz pasākumam: ',dienas_lidz_pasakumam(izveletais_dat))
print('Kopējā biļēšau cena: ', aprekinat_biletes(bilesu_sk, veids), 'EUR')
print('\nPaldies par iepirkšanos!')



#pārbaude vai neparsniedz pieejamo bilesu skaitu
'''if veids == 'koncers' and liet_datums == '1':
        izveletais_dat = date(2025, 6, 12)
    elif veids == 'koncers' and liet_datums == '2':
        izveletais_dat = date(2025, 7, 21)
    elif veids == 'koncers' and liet_datums == '3':
        izveletais_dat = date(2025, 10, 16)

    elif veids == 'festivals' and liet_datums == '1':
        izveletais_dat = date(2025, 6, 6)
    elif veids == 'festivals' and liet_datums == '2':
        izveletais_dat = date(2025, 6, 28)
    elif veids == 'festivals' and liet_datums == '3':
        izveletais_dat = date(2025, 7, 13)
    elif veids == 'festivals' and liet_datums == '4':
        izveletais_dat = date(2025, 8, 5)

    elif veids == 'sacencibas' and liet_datums == '1':
        izveletais_dat = date(2025, 7, 30)
    elif veids == 'sacencibas' and liet_datums == '2':
        izveletais_dat = date(2025, 9, 2)
    elif veids == 'sacencibas' and liet_datums == '3':
        izveletais_dat = date(2025, 11, 17)'''
=======
    print( 'Kopējā biļešu cena: ', aprekinat_biletes(bilesu_sk, veids), 'EUR')
   
except ValueError:
        print('Lūdzu ievadiet skaitli!')
>>>>>>> Stashed changes
