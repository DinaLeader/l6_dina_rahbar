products = [
{'code' : 'z1' , 'name' : 'zara cloth 121' , 'price' : 30 } ,
{'code' : 'z2' , 'name' : 'zara shoose 100' , 'price' : 45 } ,
{'code' : 'z3' , 'name' : 'zara cloth 451' , 'price' : 35 } ,
{'code' : 'z4' , 'name' : 'zara shoose 300' , 'price' : 55 } ,
{'code' : 'z5' , 'name' : 'zara shoose 231' , 'price' : 60 } ,
{'code' : 'z6' , 'name' : 'zara bag 400' , 'price' : 110 } ,
{'code' : 'z7' , 'name' : 'zara bag 500' , 'price' : 95 }]


def product_check(products , code) :
    '''
    cod-e product-e mored nazar ra daryaft mikoone.
    va esm-e mahsool ro ber migardoone
    '''
    for i in products:
        if i['code'] == code:
            print(i['name'])
            return i['name']

product_check(products, 'z5') #zara shoose 231





#b
def product_check(products , code) :
    '''
    cod-e product-e mored nazar ra daryaft mikoone.
    va etelaat-e mahsool ro bar migardoone
    '''
    for i in products:
        if i['code'] == code:
            print(i['name'])
            return ( i['code'] , i['name'] , i['price'] )

product_check(products, 'z5') #('z5', 'zara shoose 231', 60)


