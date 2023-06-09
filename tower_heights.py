import random
my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == 'q':
        break
    my_arry.append(int(val))
print(my_arry)
k = int(input("Value of K:  "))
for i in range(len(my_arry)):
    a = random.randint(0, 1)
    if a == 0:
        my_arry[i] = my_arry[i] + k
    else:
        my_arry[i] = my_arry[i] - k
my_arry.sort()
print("Diffs b/w height of shortest and longest tower:  " +
      str(my_arry[len(my_arry)-1]-my_arry[0]))
