Regular_price=2.99
Latte_price=3.99
Americano_price=2.59
menu_dict={'Latte':Latte_price,'Regular':Regular_price,'Americano':Americano_price}
print(list(menu_dict))

order=input("Enter your order:")
if order in menu_dict:
    print(f'{order} costs ${menu_dict[order]}')
else:
    print('Invalid choice')