my_arry = []

while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry.append(int(val))

k=int(input("K:  "))
ele=[]
index_ele=[]
for i in range(len(my_arry)):
    if my_arry [i] <= k:
        ele.append(my_arry[i])
    else:
        continue

for i in range(len(my_arry)):
    for j in ele:
        index_ele.append(my_arry.index(j))

index_ele=list(set(index_ele))

index_ele.sort()
count=0
for i in range(len(index_ele)-1):
    if index_ele[i]+1-index_ele[i+1]!=0:
        count+=1
    else:
        continue
print(f'Minimun swaps required: %d' %(count))