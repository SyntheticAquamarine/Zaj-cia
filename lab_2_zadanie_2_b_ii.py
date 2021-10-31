#Podpunkt I Ver 1
numbers = [1,2,3,4,5]
empty_list = []
def same_numbers(numbers):
    empty_list = [number*2 for number in numbers]
    print(empty_list)
same_numbers(numbers)

#Podpunkt II Ver 2

Lista = []
for i in range(5):
    Lista.append(int(input("Proszę podaj liczbę ")))
Second_Empty_list = []
def list_comprehension(Lista):
    Second_empty_list = [number*2 for number in Lista]
    print(Second_empty_list)
list_comprehension(Lista)

