listA = [1,2,3,4,5,6,7,8,9]
listB = [2,4,6,8,10,12,14]

def function(first_list: list, second_list):
    final_list = first_list + second_list
    final_list = list(dict.fromkeys(final_list))
    final_list = [argument**3 for argument in final_list]
    print(final_list)

function(listA,listB)

