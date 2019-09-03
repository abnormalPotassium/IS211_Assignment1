def listDivide(numbers,divide=2):
    divisible = 0
    for number in numbers:
        if number%divide == 0:
            divisible += 1
    return divisible

class ListDivideException(Exception):
    pass

def testListDivide():
    if listDivide([1,2,3,4,5]) == 2 and listDivide([2,4,6,8,10]) == 5 and listDivide([30, 54, 63,98, 100], divide=10) == 2 and listDivide([]) == 0 and listDivide([1,2,3,4,5], 1) == 5:
        pass
    else:
        raise ListDivideException

testListDivide()