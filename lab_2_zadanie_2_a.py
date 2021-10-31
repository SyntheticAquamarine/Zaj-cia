#Ver 1
names=["Anna","Dominik","Ewa","Lucjan","Krystyna"]

def print_name(names):
    for name in names:
     print(name)
print_name(names)


#Ver 2
lista=[]
for i in range(5):
    lista.append(input("Proszę podaj imie: ").lower().title())

def print_name2(lista):
    for name in lista:
        print(f"Cześć, {name}")
print_name2(lista)