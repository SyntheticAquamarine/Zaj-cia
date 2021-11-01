def check(first_names: list, name: str):
    i=0
    for first_name in first_names:
        if first_name == name:
            i+=1
        else:
            continue
    if i!=0:
        return "the list contains the values"
    else:
        return "The list does not contain the values"

test = check(["Kevin", "Zbigniew", "Przemysław", "Kazimierz", "Bolesław"], "Kazimierz")
print(test)        