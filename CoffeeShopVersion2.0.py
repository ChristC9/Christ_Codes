menu_dict={'Latte':3.99,'Regular':2.99,'Americano':2.59}
print(list(menu_dict))
while True:
    order=input('Enter Your Order: ')
    if order in menu_dict:
        print(f'{order} costs {menu_dict[order]}')
        cups=int(input(f'How many {order}s do you want? '))
        tax_rate=float(input('What is the tax rate? '))
        sub_total=menu_dict[order]*cups
        print(f'Subtotal: ${sub_total}')
        tax=sub_total*(tax_rate/100)
        print(f'Tax: ${tax:.2f}')
        Total=sub_total+tax
        print(f'Total: ${Total:.2f}')
        break
    else:
        print('Invalid Coffee Type.Please Choose Your Order From Above List')