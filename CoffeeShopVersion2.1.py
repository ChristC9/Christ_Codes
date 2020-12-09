menu={'Latte':3.99,'Regular':2.99,'Americano':3.59}
def display_menu():
    print('- Menu -')
    for k,v in menu.items():

        print('     ',k ,': $',v)

display_menu()

def calculate_subtotal(c,menuprice):
    return c*menuprice

def calculate_tax(tRate):
    return calculate_subtotal(cups,menu[order])*(tRate/100)

def calculate_total():
    print(f'Total: ${calculate_subtotal(cups,menu[order])+calculate_tax(tax_rate):.2f}')


while True:
    order=input('Enter Your Order ')
    if order in menu:
        cups=int(input(f'How many {order} do you want? '))
        tax_rate=float(input('What is the tax_rate? '))
        print(f'Sub Total: $',calculate_subtotal(cups,menu[order]))
        print(f'Tax: ${calculate_tax(tax_rate):.2f}')
        calculate_total()
        break
    else:
        print('Invalid coffee type.Please choose your order from the menu')

