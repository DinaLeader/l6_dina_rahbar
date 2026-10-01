def check_stock(products: dict[str , int] , product) :
    '''
    voroodi-ye aval nam-e product va tedad-e mojoodi ast.
    voroodi dovom product-e mored-e nazar.
    aya az mahsool-e mored nazar mojood as? T/F
    '''
    if products[product] == 0:
        print('False')
    else:
        print('True')


check_stock({'lipstick' : 0 , 'sunscreen' : 4 , 'eyeshadoe' : 10}, 'sunscreen') #True
check_stock({'lipstick' : 0 , 'sunscreen' : 4 , 'eyeshadoe' : 10}, 'lipstick') #False

