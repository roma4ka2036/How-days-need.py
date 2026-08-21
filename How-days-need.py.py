price = int(input("price: "))
if price < 0:
    print("disable")
elif price == 0:
    print("free")
else:
    profit = int(input("profit: "))
    if profit < 0:
        print("disable")
    elif profit == 0:
        print("find a job")
    else:
        q = 0
        w = 0
        z = 0
        while q == 0:
            z = z + profit
            w = w + 1
            if z >= price:
                break
print(w ,"day")