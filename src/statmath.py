'''
Written By: Rahul Sharma
First Written on: January 30, 2023 at 16:07
Description: Regression and time series analysis and Mathematical Statistics library
'''

import numpy as np

class basics():

    def __init__(self):
        super.__init__()
    
    @staticmethod
    def l2Norm(v: np.ndarray) -> np.float64:
        return np.sqrt(np.sum(v**2))
    
    @staticmethod
    def l1Norm(v: np.ndarray) -> np.float64:
        '''
        Description: L1 norm of a vector
        Input: takes a list of values (vector) as an input
        output: l1 norm of the vector
        '''
        return np.abs(np.sum(v))

    @staticmethod
    def sampleMean(v: np.ndarray) -> np.float64:
        '''
        Description: Calculates sample mean of list of data points
        Input: v: list of data
        Output: Sample mean of the data
        '''
        return np.mean(v)
    
    @staticmethod
    def sampleVariance(v: np.ndarray, estimatedData: bool) -> np.float64:
        '''
        Description: Calculates sample variance of list of data points
        Input: v: list of data, estimatedData: True/False if the data in list is estimated or not
        Output: Sample variance of the data
        '''
        mean = basics.sampleMean(v)
        if estimatedData:
            N = len(v) - 1 #sample variance when data is estimated
        else:
            N = len(v)
        subs = np.power(v - mean, 2)
        return (1/N)*np.sum(subs)

    @staticmethod
    def sampleCovariance(v1:list, v2:list) -> float:
        '''
        Description: calculates the sample covariance between two lists of data points. Assuming i.i.d. data
        Input: two lists of equal lengths
        Output: sample covariance of the data
        '''
        assert len(v1) == len(v2), "The vectors should be of equal length"
        mean_v1 = basics.sampleMean(v1)
        mean_v2 = basics.sampleMean(v2)
        
        #TODO: finish this


class rtsa():
    
    def __init__(self):
        super.__init__()

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
        mse = (1/N) * np.sum(np.power(sub, 2))

        return mse

class mathstats():
    
    def __init__(self):
        super.__init__()
        
    def firstProdedure():
        pass