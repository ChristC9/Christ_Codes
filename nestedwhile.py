a=1
while a<5:
    b=0
    while b<5:
        b+=1
        print(f'a:{a},b:{b}')
    a+=1
print('outside of loop')


for a in range(5):
    if a==3:
        break
    print(a)
print('outside of for loop')

x=1
while x<5:
    if x==4:
        break
    print(x)
    x+=1
print('outside of break while loop')

y=0
while y<6:
    y += 1
    if y==3:
        continue
    print(y)

print('outside of continue while loop')

z=0
while z<5:
    if z==4:
        pass
    print(z)
    z+=1
print('Execution is finished!')