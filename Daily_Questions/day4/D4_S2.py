my_arry = [3, 1, 2, 1, 2, 3, 3]
# while True:
#     val = input("Element:  ")
#     if val.lower() == "q":
#         break
#     my_arry.append(int(val))

k=int(input("K:  "))

s_arry=list(set(my_arry))

count=0

for i in range(len(my_arry)):
    for j in s_arry:
        if j == my_arry[i]:
            count+=1
if count > int(k//len(my_arry)):
    print("Yes! " + str(my_arry[i]))
