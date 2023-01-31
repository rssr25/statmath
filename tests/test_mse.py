from statmath import rtsa

def test_mse():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    assert rtsa.mse(a, b) == 25
    
def test_l2Norm():
    a = [1, 2, 2]
    
    assert rtsa.l2Norm(a) == 3
    
def test_lNorm():
    a = [1, 2, 3, -4, 5]
    
    assert rtsa.l1Norm(a) == 7