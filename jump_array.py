my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))
print(my_arry)

for i in range(len(my_arry)):
    if my_arry[i] >= len(my_arry)-i:
        print("Minimum jumps required to cross the array is:  " + str(i))
        break
        