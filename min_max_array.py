my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))

my_arry.sort()
print("Minimum element is:  ", my_arry[0])
print("Maximun element is:  ", my_arry[len(my_arry)-1])