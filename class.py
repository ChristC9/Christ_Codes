import json
class Details:
    age=' '
    name=' '


details=Details()
details.age=int(input('Enter Your Age: '))
details.name=input('Enter Your Name: ')
print(details.name,' ',details.age)
print(getattr(details,'age'))


Jlist=dir(json)
print(Jlist)