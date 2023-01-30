from statmath import rtsa

def test_mse():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    assert rtsa.mse(a, b) == 25
    
def test_l2norm():
    a = 5
    b = 10
    
    assert rtsa.l2norm(a, b) == 25
    
def test_lnorm():
    a = 5
    b = 10
    
    assert rtsa.lnorm(a, b) == 5