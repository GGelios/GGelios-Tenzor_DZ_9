import password

def test_len():
    '''String length test function.
    Checks that the password string is at least 6 characters long, otherwise returns False
    '''
    assert password.password('96thf') == False

def test_include_numbers():
    '''The function of testing the password for the content of numbers in it.
    Returns False if the password does not contain any digits
    '''
    assert password.password('dftyjd') == False

def test_only_numbers():
    '''The function of testing the password for the content of letters in it.
    Returns False if the password does not contain any letters
    '''
    assert password.password('12334567890') == False

def test_check_password():
    '''The function of testing the password for the content of the word password in it.
    Returns False if the password contains this word in any register
    '''
    assert password.password('password') == False