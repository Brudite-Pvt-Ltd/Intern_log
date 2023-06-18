my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry.append(int(val))
print(my_arry)

print("Maximum:  " + str(max(my_arry)))
print("Minimum: " + str(min(my_arry)))