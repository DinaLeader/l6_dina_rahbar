def calculate_grade(mark : int):
    '''
    ba tavajoh be nomre vared shode 
    horoof-e marbote namayesh dade mishavad
    '''
    if 90 <= mark <= 100 :
        print('A')
    elif 80 <= mark <= 89 :
        print('B')
    elif 70 <= mark <= 79 :
        print('C')
    elif 60 <= mark <= 69 :
        print('D')
    elif 0 <= mark <= 59 :
        print('F')
    else :
        raise ValueError ('Invalid information')

nomre = calculate_grade(75) #C
nomre = calculate_grade(41) #F
nomre = calculate_grade(100) #A

