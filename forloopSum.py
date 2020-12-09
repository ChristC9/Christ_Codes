prices=[3.99,2.99,5.99,5.10]
total=0
for i in prices:
    total+=i
print(total)

menu_dict={'Regular':2.99,'Latte':4.99,'Americano':6.99}
for key,value in menu_dict.items():
    print(key,value)

for even in range(0,100,2):
    if even!=98:
        print(even,end=',')
    else:
        print(even)
print()
for odd in range(1,100,2):
    if odd!=99:
        print(odd,end=',')
    else:
        print(odd)