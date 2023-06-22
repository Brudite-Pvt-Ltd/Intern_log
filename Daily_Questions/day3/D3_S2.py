my_arry = []
while True:
    val = input("Element:  ")
    if val.lower() == "q":
        break
    my_arry.append(int(val))
buy=min(my_arry)
sell=max(my_arry)
if my_arry.index(buy)<my_arry.index(sell):
    print("Can't make any profit!")
else:
    print(f'buy on day: %d price: %d. Sell on day: %d price: %d.\n Profit: %d'%(my_arry.index(buy)+1,buy, my_arry.index(sell)+1,sell,sell-buy))