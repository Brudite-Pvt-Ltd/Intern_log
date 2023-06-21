my_arry1 = []
my_arry2 = []
print("List 1")
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry1.append(int(val))
print(my_arry1)

print("List 2")
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry2.append(int(val))
print(my_arry2)

my_arry2.extend(my_arry1)
print(my_arry2)
my_arry2 = list(set(my_arry2))
print(my_arry2)