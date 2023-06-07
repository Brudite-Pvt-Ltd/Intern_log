my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))

print("Array before reversing:  ", my_arry)
my_arry = my_arry[::-1]
print("Array after reversing:  ", my_arry)
