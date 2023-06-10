my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))
print(my_arry)
my_arry.sort()
for i in range(len(my_arry)-1):
    if my_arry[i] == my_arry[i+1]:
        print(my_arry[i])