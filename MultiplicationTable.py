n=int(input('Enter A Number'))
def mul(n):
    return lambda x:x*n
result=mul(n)
for i in range(1,11):
    print(n,' x ',i,' = ',result(i))

#my_tuple=(3,5,6,9,123,42)
#resList=tuple(filter(lambda a:a%3==0,my_tuple))
#print(resList)
#print(type(resList))

my_list=(1,2,3,4,5)
doubleResult=tuple(map(lambda b:b**2,my_list))
print(my_list)
print(type(my_list))