def find_max(numbers: list):
    '''
    peyda kardan-e bozorg tarin adad-e yek list.
    '''
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise ValueError('Only numbers are allowed')
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    print(biggest)
    return biggest

find_max([10,8,50,43,9,19]) #50

