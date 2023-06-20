my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    elif int(val) not in [0,1,2]:
        print("Invalid element")
    else:
        my_arry.append(int(val))
my_arry.sort()
print("Array in Ascending order:  ", my_arry)