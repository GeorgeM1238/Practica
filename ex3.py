produse = {"Pâine albă": {"pret": 3.00, "tva_vechi": 9, "tva_nou": 11} ,
 "Făină albă": {"pret": 4.50, "tva_vechi": 9, "tva_nou": 11},
 "Mălai": {"pret": 4.00, "tva_vechi": 9, "tva_nou": 11},
 "Orez": {"pret": 8.00, "tva_vechi": 9, "tva_nou": 11},
 "Paste făinoase": {"pret": 6.00, "tva_vechi": 9, "tva_nou": 11},
 "Lapte": {"pret": 6.50, "tva_vechi": 9, "tva_nou": 11},
 "Brânză telemea": {"pret": 35.00, "tva_vechi": 9, "tva_nou": 11},
 "Iaurt": {"pret": 2.50, "tva_vechi": 9, "tva_nou": 11},
 "Ouă": {"pret": 9.00, "tva_vechi": 9, "tva_nou": 11},
 "Carne de pui": {"pret": 18.00, "tva_vechi": 9, "tva_nou": 11},
 "Carne de porc": {"pret": 25.00, "tva_vechi": 9, "tva_nou": 11},
 "Salam / Parizer": {"pret": 20.00, "tva_vechi": 9, "tva_nou": 11},
 "Pește congelat": {"pret": 22.00, "tva_vechi": 9, "tva_nou": 11},
 "Cartofi": {"pret": 4.00, "tva_vechi": 9, "tva_nou": 11},
 "Ceapă": {"pret": 3.50, "tva_vechi": 9, "tva_nou": 11},
 "Morcovi": {"pret": 4.00, "tva_vechi": 9, "tva_nou": 11},
 "Mere": {"pret": 6.00, "tva_vechi": 9, "tva_nou": 11},
 "Banane": {"pret": 8.00, "tva_vechi": 9, "tva_nou": 11},
 "Ulei floarea-soarelui": {"pret": 14.00, "tva_vechi": 9, "tva_nou": 11},
 "Unt": {"pret": 10.00, "tva_vechi": 9, "tva_nou": 11},
 "Zahăr": {"pret": 5.00, "tva_vechi": 9, "tva_nou": 11},
 "Sare": {"pret": 2.00, "tva_vechi": 9, "tva_nou": 11},
 "Cafea": {"pret": 15.00, "tva_vechi": 5, "tva_nou": 11},
 "Detergent": {"pret": 20.00, "tva_vechi": 19, "tva_nou": 21},
 "Săpun": {"pret": 4.00, "tva_vechi": 19, "tva_nou": 21},
 "Hârtie igienică": {"pret": 10.00, "tva_vechi": 19, "tva_nou": 21},
 "Bere": {"pret": 5.00, "tva_vechi": 19, "tva_nou": 21},
 "Apă plată": {"pret": 3.00, "tva_vechi": 9, "tva_nou": 11},
 "Energizant": {"pret": 7.00, "tva_vechi": 19, "tva_nou": 21},
 "Țigări": {"pret": 20.00, "tva_vechi": 20, "tva_nou": 41},
 }


def pret():
    total = 0
    fara_t = 0
    pret_nou = 0
    for key, value in produse.items():
        total = total + value["pret"]
    print(total)

    for key, value in produse.items():
        if value["tva_vechi"] == 9:
            fara_t = fara_t + value["pret"] * (100 / 109)
        elif value["tva_vechi"] == 19:
            fara_t = fara_t + value["pret"] * (100 / 119)
        elif value["tva_vechi"] == 20:
            fara_t = fara_t + value["pret"] * (100 / 120)
            print(fara_t)

            if value["tva_nou"] == 11:
                pret_nou = pret_nou + fara_t * (111 / 100)
            elif value["tva_nou"] == 21:
                pret_nou = pret_nou + fara_t * (121 / 100)
            elif value["tva_nou"] == 41:
                pret_nou = pret_nou + fara_t * (141 / 100)
                print(pret_nou)

pret()
