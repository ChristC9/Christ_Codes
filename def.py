def my_fun(x:str):
    return x

print(my_fun(5.6))

print((5+9 == 7*2) and (289641 % 2361 >= 2361) and (982182 / 5233 > 20091) or True)

age=22
print(globals()['age'])#using globals() to retrieve the age(globals()['age'] acts as a dictionary)

y=lambda a:a+10

print(y(20))
