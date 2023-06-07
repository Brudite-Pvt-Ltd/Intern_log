my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))

k = int(input("Value of K:  "))
if k > len(my_arry):
    print("K out of index")
else:
    my_arry.sort()
    print("Kth smallest term of the array is: ", my_arry[k-1])
