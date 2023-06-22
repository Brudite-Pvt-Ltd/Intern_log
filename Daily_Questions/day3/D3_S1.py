my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry.append(int(val))
max_end=0
max_far=0
for i in range(len(my_arry)):
    max_end+=my_arry[i]
    if max_far<max_end:
        max_far=max_end
    if max_end<0:
        max_end=0
print(max_far)
    