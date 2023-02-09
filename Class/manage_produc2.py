products = {'computer': [1000, 20],
            'print': [500, 10],
            'monitor': [200, 15],
            'mouse': [50, 100]
            }

while True:
    print('1. Show Products ')
    print('2. Buy Products')
    print('3. Edit Price')
    print('4. Exit')

    choice = input('Enter your choice: ')
    if choice == '1':
        for name in products:
            print(f'{name}- ${products[name][0]}- #{products[name][1]} items')
        # print(products)

    elif choice == '2':
        name_product = input('Enter name product you want to buy: ')
        if name_product not in products:
            print(f'Product {name_product} does not exist ')
        else:
            quantity = int(input('Enter Quantity to buy product: '))
            if quantity > products[name_product][1]:
                print(
                    f'Not enough items.Only {products[name_product][1]} items left')
            else:
                payment = quantity * products[name_product][0]
                print(f'You have to pay ${payment}')
                products[name_product][1] -= quantity
                print(
                    f'You buy succefully product {name_product} with quantity is {quantity}')

    elif choice == '3':
        name_product = int(input('Enter name product you want edit: '))
        if name_product not in products:
            print(f'Product {name_product} does not exist')
        else:
            new_price = input('Enter price new of product:')
            products[name_product][0] = new_price
            print(
                f'Product {name_product} update price succefully is {new_price}')
    elif choice == '4':
        break
    else:
        print('Invalid Choice !')
