my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))

m=z=0
print("len of array:  ", len(my_arry))
for i in range(len(my_arry)):
    m += my_arry[i]
    if m < 0:
        m = 0
    if z < m:
        z = m

print("Max Subarray Sum:  ", z)
