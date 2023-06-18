my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry.append(int(val))
print(my_arry)
my_arry.sort()
k = int(input("K:  "))
if (k>0 & k<=len(my_arry)):
    print(my_arry[k-1])
else:
    print("Out of Index!")
