x=15 #x ora è una variabile globale
def esempio():
    global x #senza questo "global" non posso modificare la variabile globale
    x+=2
    return(x)
print(esempio())

x=15
def esempio():
    y=x #y è una variabile locale
    y+=5
    return(y)
print(esempio())

def nuova():
    var=25
    return(var)

prova=nuova()+4
print(prova)


elenco=[2,3,4,'test',6,'pippo',9,8]
fetta=elenco[2:6]

print(elenco[:5])
print(elenco[4:])

lista=[2,3,5,8,9,6,78,89]

for num in range(6):
    print(num)

for num in lista:
    print(num)

numeri=list(range(30,56))

lista_mult=[2,3,'asdfa',8,[2,3,4,'come va',6,7,8],6,'prova',89]

print(lista_mult[3])
print(lista_mult[-2])

print(lista_mult[4][-2])
