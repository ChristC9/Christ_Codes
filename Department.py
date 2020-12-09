emp=['James',102,'UK']
Dep1=['CS',10]
Dep2=['IT',11]
HOD_CS=[10,'Mr.Holding']
HOD_IT=[11,'Mr.Bewon']
print("Printing Employ Data....")
print(f'Name:{emp[0]}, ID:{emp[1]}, Country:{emp[2]}')
print("Printing Departments")
print('Dep1_Name:{0},'.format(Dep1[0]),'Dep1_ID:{0}'.format(Dep1[1]))
print('Dep2_Name:{0},'.format(Dep2[0]),'Dep2_ID{0}'.format(Dep2[1]))
print("HOD Details")
print('CS_HOD Name:%s, ID:%d'%(HOD_CS[1],HOD_CS[0]))
print('IT_HOD Name:%s, ID:%d'%(HOD_IT[1],HOD_IT[0]))


my_input_list=[]
noOfitems=int(input("Enter the length of the list"))
for i in range(noOfitems):
    my_input_list.append(int(input('Enter the item')))

print("The Elements are:")
for j in range(len(my_input_list)):
    if(j!=noOfitems-1):
        print(my_input_list[j],end=",")
    else:
        print(my_input_list[noOfitems-1])
