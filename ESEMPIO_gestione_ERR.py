def divisore(a,b):
    try:
        ris=a/b
        print('risultato=' +str(ris))
    except ZeroDivisionError:
        print('errore divisore = 0')

divisore(9,4)

divisore(7,0)


def moltiplic():
    try:
        a=int(input("metti a: "))
        b=int(input("metti b: "))
        ris=a*b
        print('risultato=' +str(ris))
    except ValueError:
        print('metti mumeri')
    finally:
        print('ciao')
