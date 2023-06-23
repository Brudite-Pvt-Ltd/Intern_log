my_arry = []

while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry.append(int(val))
print(my_arry)
water = 0
curr_max = my_arry[0]
for i in range(1,len(my_arry)-1):

    if curr_max<my_arry[i]:
        curr_max = my_arry[i+1]

    water += curr_max-my_arry[i]

print(f'Total water: %d' % (water))
