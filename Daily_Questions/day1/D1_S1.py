my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry.append(int(val))
print(my_arry)
my_arry.reverse()
print(my_arry)