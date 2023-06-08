my_arry = []
while True:
    val = input("Enter element:  ")
    if val.lower() == "q":
        break
    else:
        if int(val) not in [0,1,2]:
            print("Invalid Input.")
            val = input("Enter element:  ")
        else:
            my_arry.append(int(val))
    
# print(my_arry)
my_arry.sort()
print("Array in ascending order:  ", my_arry)