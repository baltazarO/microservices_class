from divisors import divisors

def test_one():
    assert divisors(1) == [1]

def test_two():
    assert divisors(2) == [1,2]

def test_three():
    assert divisors(3) == [1,3]

def test_16():
    assert divisors(16) == [1,2,4,8,16]

def test_10():
    assert divisors(10) == [1,2,5,10]

def test_30():
    assert divisors(30) == [1,2,3,5,6,10,15,30]

def test_77():
    assert divisors(77) == [1,7,11,77]
