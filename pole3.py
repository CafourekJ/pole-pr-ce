cisla = [1, 8, 3, 10, 5, 2]
num = int(input("Jaké číslo by jste chtěli najít v poli ?: "))
if num in cisla:
    print (f"číslo {num} se nachází v poli")
else:
    print(f"číslo {num} se v poli nenachází")