def secti_cisla(a, b):
    print(a + b)

secti_cisla(5, 7) 

def pozdrav():
    jmeno = input("Zadej své jméno: ")
    print("Ahoj " + jmeno)
pozdrav()

def prumer_pole(pole):
    prumer = sum(pole) / len(pole)
    print("Průměr je:", prumer)

prumer_pole([1, 2, 3, 4, 5])

def petkrat_ahoj():
    for i in range(5):
        print("Ahoj")

petkrat_ahoj()  

def zvirata():
    pole = []
    pole.append("pes")
    pole.append("kočka")
    pole.append("králík")
    for zvire in pole:
        print(zvire)
    print("Počet zvířat v poli:", len(pole))

zvirata()  