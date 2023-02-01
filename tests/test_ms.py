from statmath import mathstats, basics, rtsa
import numpy as np
import math

def test_mse2():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([6, 7, 8, 9, 10])

    assert rtsa.mse(a, b) == 25