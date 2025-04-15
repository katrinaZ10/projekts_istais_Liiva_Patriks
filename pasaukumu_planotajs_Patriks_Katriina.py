from datetime import date #importē datime, lai var aprēķināt cik dienas līdz festivālam

#[date(2025, 6, 6), date(2025, 6, 28), date(2025, 7, 13), date(2025, 8, 5)]
'''festivals1 : date(2025, 6, 6),
        festivals2 : date(2025, 6, 28),
        festivals3 : date(2025, 7, 13),
        festivals4 : date(2025, 8, 5)'''

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

def aprekinat_biletes(skaits, veids): #funkcija ar padotajiem parametriem (ko ievada lietotājs), atgriež kopējo cenu
    biletes_cena_kopa = (skaits)*cena[veids]
    return biletes_cena_kopa

def brivas_vietas(kas): # funkcija atgriež cik brīvas vientas ir izvēlētajā pasākumā
    return(ietilpiba[kas])
        
def laiks():
    sodien = date.today()
    datums = date('')
    diff = datums - sodien
    print(diff.days)


print('Sveicināti pasākumu plānotājā!')
try:
    while True:
        print('Pasākumi veidi: ', '\n1 - Koncerts', '\n2 - Festivals', '\n3 - Sacencibas')
        veids = int(input('Ievadiet kuru no pasākumiem apmeklēsiet (1, 2 vai 3): '))

        if veids == 1:
            veids = 'koncerts'
            break
        elif veids == 2:
            veids = 'festivals'
            break
        elif veids == 3: 
            veids = 'sacencibas'
            break
        else:
            print('Ievadiet no 1 līdz 3 ciparu!')
    
    for i in datumi[veids]:
        print(i)

    liet_datums = input('Ievadiet sev vēlamo datumu (kārtas skaitli): ')
    if veids == 'koncers' and liet_datums == '1':
        print('Datums ',datumi.get('koncerts'[1]))
    

    print('Pieejamo biļešu skaits: ', brivas_vietas(veids)) 

    bilesu_sk = int(input('Cik biļetes vēlaties: '))

    print('-'*17) #Konsolē parāda "čeku"
    print('Pasākuma veids: ', veids)
    print('Datums: ')
    print('Dienas līdz pasākumam: ')
    print('Kopējā biļēšau cena: ', aprekinat_biletes(bilesu_sk, veids))
    print('\nPaldies par iepirkšanos!')

except ValueError:
        print('Lūdzu ievadiet skaitli!')

