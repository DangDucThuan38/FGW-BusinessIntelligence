products = {} # 1 product includes id and name
id = 0
while True:
    print('1. Add product')
    print('2. Show product')
    print('3. Eidt product')
    print('4. Delete product')
    print('5. Eixt')
    
    choice = input('Enter your choice: ')
    if choice == '1':
        #id = input('Enter id of product: ')
        #name = input('Enter name product:')
        #if id in products:
        #    print(f'The product {name} is in stock')
        #else:
        #    products[id] = name
        #    print(f'Successfully added products {name} to stock')
        
        product_name = input('Enter name products: ')
        if product_name in products.values():
            print(f'Product {product_name} already exist')
            products[id]= product_name 
            id +=1
        else:
            products[id]= product_name
            id +=1

    elif choice =='2':
        #print(products)
        for id,name in products.items():
            print(f'{id}-{name}')
        
    elif choice =='3':
        #id = input('Enter id of product: ')
        #if id not in products:
        #    print(f'Product {id} not added')
        #else:
        #    new_name =input('Enter name products edit:')
        #    products[id] = new_name
        #    print(f'Product {id} edit succefully is {new_name}')
        
        edit_id = input('Enter id of product: ')
        if edit_id not in products:
            print(f'Edit not succefully')
        else:
            new_name =input('Enter name products edit:')
            products[id] = new_name
            print(f'Product {id} edit succefully is {new_name}')
            
    elif choice =='4':
        #id = input('Enter id of product: ')
        #if id not in products:
        #    print(f'Product {id} not in stock')
        #else:
        #    print(f'Product is id:{id}')
        #    del products[id]
        #    print(f'Delete Succefully product {id} out of stock')
        
        del_id = input('Enter Product id to delete: ')
        if del_id not in products:
            print(f'Product with id {del_id} does not exist')
        else:
            del products[del_id]
            print('Product {del_id} deleted')
            
            
            
    elif choice =='5':
        break
    else:
        print('Invalid choice')
    
        
        

        