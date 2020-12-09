max_length=int(input('Enter Maximum Length '))
numbers=[]
for i in range(0,max_length):
    numbers.append(int(input(f'Enter a number ')))

def sum_of_values(nums=[]):
    sum=0
    for j in range(0,len(nums)):
        sum+=nums[j]
    return sum

print(sum_of_values(numbers))