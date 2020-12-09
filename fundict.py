def dict_fun(**kwargs):
    print(kwargs)

dict_fun(Fruits='Orange',Drinks='Cola',Food='Noodle')


def fun_sum(*args):
    sum = 0
    for i in range(len(args)):
        sum=sum+args[i]
    print(sum)

fun_sum(10,20,30)


test1=0.04
print(bool(test1))


count=0
while count<5:
    print('Hello')
    count+=1