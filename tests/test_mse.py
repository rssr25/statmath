from statmath import rtsa, basics
import numpy as np

def test_mse():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([6, 7, 8, 9, 10])

    assert rtsa.mse(a, b) == 25
    
def test_l2Norm():
    a = np.array([1, 2, 2])
    
    assert basics.l2Norm(a) == 3
    
def test_lNorm():
    a = np.array([1, 2, 3, -4, 5])
    
    assert basics.l1Norm(a) == 7

#TODO: test sample mean and variance
def test_sampleVariance():
    pass

def test_sampleMean():
    pass