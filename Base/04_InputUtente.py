# Inserimento dati dell'utente
print("\n=========== Ciao Benvenuto ============\n")
Nome = input("Inserisci il tuo nome: ")
Cognome = input(f"Inserisci il tuo cognome {Nome}")
Eta = int(input(f"Quanti anni hai?"))
Altezza = float(input("Quanto sei alto?"))

# Stampa dati utente
print(f"\nciao {Nome} {Cognome} hai {Eta} e sei alto {Altezza} cm")