my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))

my_arry.sort()
print("Array is:  ", my_arry)