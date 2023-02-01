from statmath import rtsa, basics
import numpy as np
import math

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

#TODO: test sample mean, variance and covariance

def test_sampleMean():
    a = np.array([46, 69, 32, 60, 52, 41])
    assert basics.sampleMean(a) == 50

def test_sampleVarianceEstimated():
    a = np.array([46, 69, 32, 60, 52, 41])
    
    assert math.isclose(basics.sampleVariance(a, True), 177.2)


def test_sampleVarianceNotEstimated():
    a = np.array([46, 69, 32, 60, 52, 41])
    
    assert math.isclose(basics.sampleVariance(a, False), 147.66666666666666) 


def test_sampleCovariance():
    a = np.array([510, 480, 495])
    b = np.array([560, 505, 540])

    assert math.isclose(basics.sampleCovariance(a, b), 275)