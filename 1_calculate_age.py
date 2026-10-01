def calculate_age (birth_year:int) :
    '''
    tabe-e barayr mohasebe sen ba sal
    '''
    age = 1405 - birth_year 
    print(f'sen-e shoma {age} ast.') #san-e shoma 14 ast.
    return age
age = calculate_age(1391) #sen-e shoma 14 ast.



#b
def calculate_age (birth_year : int , year_type) :
    '''
    tabe-e baraye mohasebe sen ba sal va noe-e sal
    '''
    if year_type == 'miladi' :
        age = 2026 - birth_year
        print(f'sen-e shoma {age} ast.')  
        return age 
    elif year_type == 'shamsi' :
        age = 1405 - birth_year
        print(f'sen-e shoma {age} ast.')
        return age 
    else :
        raise ValueError ('Invalid information')
age = calculate_age(2012 , 'miladi') #sen-e shoma 14 ast.




#c
def calculate_age (birth_year , year_type = 'miladi') :
    '''
    tabe-e baraye mohasebe sen ba sal va noe-e 
    halat-e pish farz --> miladi
    '''
    if year_type == 'miladi' :
       age = 2026 - birth_year
       print(f'sen-e shoma {age} ast.')  
       return age 
    if year_type == 'shamsi' :
        age = 1405 - birth_year
        print(f'sen-e shoma {age} ast.')
        return age 
age = calculate_age(1979) #sen-e shoma 47 ast.




#d
def calculate_age(birth_year) :
    '''
    tabe-e baraye mohasebe sen ba sal va noe-e sal
    '''
    for i in range(1000 , 1405) :
        if i == birth_year :
            age = 1405 - birth_year
            print(f'sen-e shoma {age} ast.')
            return age
    for i in range(1600 , 2026) :
        if i == birth_year :
            age = 2026 - birth_year
            print(f'sen-e shoma {age} ast.')
            return age
    raise ValueError ('Invalid information')
age = calculate_age(2016) #sen-e shoma 10 ast

