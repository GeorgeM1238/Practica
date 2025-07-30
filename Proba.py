'''def inmultire_lista(lista_de_val):
    total = 1
    for valoare in lista_de_val:
        total = total * valoare
        return total
        print(inmultire_lista([2, 3, 4, 5]))
'''
from ipaddress import summarize_address_range

'''
def sal_brut(salariu_net):
    salariu=(55/100)*salariu_net
    return salariu

print(sal_brut(5000))
'''

'''
def sal_brut(salariu_net):
    if salariu_net >= 0 and salariu_net <= 3000:
        salariu = (60 / 100) * salariu_net
        return salariu
    elif salariu_net > 3000 and salariu_net <= 8000:
        salariu = (55/ 100) * salariu_net
        return salariu
    elif salariu_net > 8000:
        salariu = (50 / 100) * salariu_net
        return salariu
    print(sal_brut(6000))
'''

#2

def pensie(suma):


    for i in range(36):
        total = total + suma
    if i % 12 == 0:
        total = total + (10 / 100) * total
        print(total)

        print(pensie(300))
