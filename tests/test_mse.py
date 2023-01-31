from statmath import rtsa, basic

def test_mse():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    assert rtsa.mse(a, b) == 25
    
def test_l2Norm():
    a = [1, 2, 2]
    
    assert basic.l2Norm(a) == 3
    
def test_lNorm():
    a = [1, 2, 3, -4, 5]
    
    assert basic.l1Norm(a) == 7

#TODO: test sample mean and variance
def test_sampleVariance():
    pass

def test_sampleMean():
    pass