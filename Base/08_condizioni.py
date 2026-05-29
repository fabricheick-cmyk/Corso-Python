"""
# Condizione If(se) elif(altrimenti se) else(altrimenti)

if condizione: 
    Codice
else:
    Codice

if condizione:
     Codice
elif condizione:
     Codice:
else:
    Codice                 
"""

cliente = input("Hai una prenotazione")
if cliente == "si":
    print("ok")
else:
    print("Non ci sono posti")

# Risultato esame
Studenti = input("inserisci il nome dello studente")
votoesame = int(input("inserisci il voto dello studente (da 1 a 33): "))

if votoesame >= 18:
    print("Esame Superato")
elif votoesame >= 28:
    print("Ottimo Lavoro")    
elif votoesame > 30:
    print("Lode")
else:
    print("Bocciato")

print       