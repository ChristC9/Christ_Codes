my_shopping_list=['eggs','bread','cheese','butter']
my_shopping_list.sort()
print(my_shopping_list)

my_shopping_list.append('flowers')
print(my_shopping_list)

my_shopping_list.insert(0,'milk')
print(my_shopping_list)

my_shopping_list.remove('bread')
print(my_shopping_list)

my_shopping_list.insert(1,'orange juice')
my_shopping_list.insert(2,'fried chicken')
print(my_shopping_list)

print(my_shopping_list.pop())
print(my_shopping_list.pop())
print(my_shopping_list.pop())
print(my_shopping_list.pop())
print(my_shopping_list.pop())
print(my_shopping_list.pop())
print(my_shopping_list.pop())


my_list1=[20,30,23,44]
def change_list(my_list1):
    my_list1.append(55)
    my_list1.append(70)
    print('Change List is ',my_list1)

#calling the function first and printing the original list later make your original list changes!
#change_list(my_list1)
#print('Original list',my_list1) #list memeber changes bcuz of calling the change list function first!output is [20,30,23,44,55,70]

#if you output the original list first your original list is remained the same without changing anymore!
print('Original List',my_list1) # [20,30,23,44]
change_list(my_list1)#[20,30,23,44,55,70]
