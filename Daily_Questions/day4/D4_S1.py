my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry.append(int(val))

for i in range(len(my_arry)):
    if my_arry[i]==0:
        print("Yes!0")
        break
    else:
        sum=0
        for j in range(i+1,len(my_arry)):
            sum+=my_arry[j]
            if sum==0:
                print("Yes!")
                break
            
        


