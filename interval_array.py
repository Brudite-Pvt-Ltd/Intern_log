my_arry = []
i=1
while True:
    l = []
    val = input("Interval " + str(i) + ":  ")
    if val.lower() == 'q':
        break
    a,b = val.split(" ")
    l.append(int(a))
    l.append(int(b))
    my_arry.append(l)
    i += 1
print(my_arry)

my_arry.sort()
print(my_arry)

count = 1
for i in range(len(my_arry)-1):
    if my_arry[i][0] != my_arry[i+1][0]:
        count += 1
print(count)



# h = []
# for i in range(len(my_arry)-1):
#     e = []
#     # print(e)
#     if my_arry[i][0] == my_arry[i+1][0]:
#         e.append(my_arry[i][0])
#         if my_arry[i][1] >= my_arry[i+1][1]:
#             e.append(my_arry[i][1])
#         else:
#             e.append(my_arry[i+1][1])
#     else:
#         continue
#     # print(e)
#     # print("\n")
#     h.append(e)
# print(h)

# ar = []
# for i in range(len(my_arry)-1):
#     x = []
#     if my_arry[i][0] == my_arry[i+1][0]:
#         x.append(my_arry[i][0])
#         x.append(my_arry[i+1][1])
#     else:
#         continue
#     print(x)
    