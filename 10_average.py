def average(marks : list):
    '''
    miyangin-e adad-e yek list.
    '''
    for number in marks:
        if not isinstance(number, (int, float)):
                raise ValueError('Only numbers are allowed')
    ave = 0
    for number in marks :
        ave += number / len(marks)
    print(ave)
    return ave

average([20,10,6,8,13,19]) #12.666666666666666

