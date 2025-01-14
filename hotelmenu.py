#Define the menu of restaurant

menu = {
    'Cold Coffee':120,
    'Naga Wings': 150,
    'Burger':200,
    'Sandwitch':130,
    'Kitkat':80,
}
#Greet
print("Welome to Python Restaurant")
print('Cold Coffee:120Tk\nNaga Wings:150Tk\nBurger:200Tk\nSandwitch:130Tk\nKitkat:80Tk')

order_total=0

item_1 = input("Enter the name of item you wanna order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f'your item {item_1} has been added to your order')

else:
    print(f'Ordered item {item_1} is not available right now!')

another_order = input('Do you wanna add another item? (Yes/No)')

if another_order == "Yes":
    item_2= input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'your item {item_2} has been added to order')
    else:
        print(f'Ordered ite {item_2} is not available')
print(f'the total amount of items to pay is {order_total}Tk')