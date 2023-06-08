my_arry1 = []
my_arry2 = []
arry_union = []

print("\nEnter Q or q to exit")

print("Elements for Array 1 ")
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry1.append(int(val))

print("Elements for Array 2 ")
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry2.append(int(val))

for num in my_arry1:
    arry_union.append(num)

for num in my_arry2:
    if num not in arry_union:
        arry_union.append(num)

print("Array 1:  ", my_arry1)
print("Array 2:  ", my_arry2)
print("Union of both the arrays is:  ", arry_union)

