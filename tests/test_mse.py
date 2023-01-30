from statmath import rtsa

def test_mse():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    assert rtsa.mse(a, b) == 25
    
def test_l2norm():
    pass
    
def test_lnorm():
    pass