emp_num = int(input("Enter num of employees:  ")) 
a = []
for i in range(emp_num):
    b = int(input("Employee " + str(i+1) + " trusts on employee:  "))
    a.append(b)

a.sort()
print(a)
b=list(set(a))
print(b)
c = []

for i in b:
    count = 0
    for j in a:
        if i==j:
            count += 1
        else:
            count += 0
    c.append(count)

print(c)
d = max(c)
print("mole is:  ",b[c.index(d)])
