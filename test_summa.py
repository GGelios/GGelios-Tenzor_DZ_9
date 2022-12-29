import summa

def ValueError_0():
    '''Exception handling check function.
    In the case when the exception handles correctly, it returns 0
    '''
    assert summa.summa(['abc']) == 0

def numbers():
    '''Data entry validation function.
    If we enter a list containing int values, it should return the sum of these values to us
    '''
    assert summa.summa([5]) == 5