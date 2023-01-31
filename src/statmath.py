'''
Written By: Rahul Sharma
First Written on: January 30, 2023 at 16:07
Description: Regression and time series analysis and Mathematical Statistics library
'''
import math

class rtsa():
    
    def __init__(self):
        super.__init__()

    @staticmethod
    def l2Norm(v: list) -> float:
        return math.sqrt(sum([(i)**2 for i in v]))
        
    def l1Norm(v:list) -> float:
        '''
        Description: L1 norm of a vector
        Input: takes a list of values (vector) as an input
        output: l1 norm of the vector
        '''
        return abs(sum(v))

    @staticmethod
    def mse(estimate: list, original: list) -> float:
        '''
        Description: calculates mean-squared error between estimated and original data
        input: two lists
        output: mse between the list of data
        '''

        assert len(estimate) == len(original), "estimates and data are not of equal length"
        N = len(estimate)
        sub = [a-b for a, b in zip(estimate, original)]
        mse = (1/N) * sum([math.pow(k, 2) for k in sub])

        return mse

class mathstats():
    
    def __init__(self):
        super.__init__()
        
    def firstProdedure():
        pass