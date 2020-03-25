
mio_dizionario = {"mia_chiave_uno": "mio_valore", "età": 24, 3.14: "pi_greco", "primi":[1,2,3,5,7]}
mio_dizionario


mio_dizionario["mia_chiave_uno"]


mio_dizionario[3.14]


mio_dizionario["nuova_chiave"] = "nuovo_valore"
mio_dizionario

 
mio_dizionario["età"] = 99
mio_dizionario


"età" in mio_dizionario


"zen" in mio_dizionario


del mio_dizionario["mia_chiave_uno"]
mio_dizionario

if "birra" in mio_dizionario.keys():
    print(mio_dizionario["birra"])
else:
    print("Chiave non trovata!")
    
#il metodo .get su dizionario permette di richiamare il valore di una chiave
#permettendo di restituire un valore di default in caso di errore
mio_dizionario.get("birra","Chiave non trovata, mi spiace!")

nome="Jack"
numero=18
saluto=f"Ciao {nome}, questa è la lezione n{numero}! Benvenuto!"


z=5
calcola=f"Il quadrato di {z} è {z * z}"

serie_numerica = "1492-1984-123311-555"
serie_numerica.split("1")
