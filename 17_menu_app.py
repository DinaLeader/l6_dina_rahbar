def menu_app():
    '''
    ghaza hay-ee ke sefaresh dadid be sorate list 
    namayesh mide
    '''
    orders = []
    foods = ['Pizza','Pasta','Stake','Salasd','Burger',
             'French Frize','Chiken Sandwich','Soda']
    print(foods)
    while True :
        order = input('Sefaresh-e khod ra vared kond : ')
        if order == 'order' : 
            break
        else :
            orders.append(order)
    print('----ORDERS----')
    print(orders)


menu_app()


