"""" int, str, float, bool"""
Nome: str = 'Mattia'
Cognome: str = 'Umberto'
Eta = 45


print('Ciao mi chiamo ' + Nome + ' ' + Cognome + ' e ho + ' + str(Eta) + 'anni')
print(f'ciao mi chiamo {Nome} {Cognome} e ho {str(Eta)} anni')
print('Studente' , Nome, Cognome, Eta)



Nome = 'Lamine'
Cognome = 'Diop'
Altezza = 1.82
print(f'Mein name ist {Nome} {Cognome} und ich bin {str(Altezza)} cm gross ')


a = 2
b = 5
c = a > b 

# Stampa del tipo di data
print(type(Nome))         # class str
print(type(Cognome))      # class str
print(type(Eta))          # class int
print(type(Altezza))      # class float
print(type(c))            # class bool

