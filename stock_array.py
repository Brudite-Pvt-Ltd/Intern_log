my_arry = []
while True:
    val = input("Price:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))

a=max(my_arry)
b=min(my_arry)
if my_arry.index(a) < my_arry.index(b):
    print("buy on day: " + str(my_arry.index(b)+1))
    print("sell on day: " + str(my_arry.index(a)+1))
    print("profite:  " + str(a-b))
else:
    print("No sales!")