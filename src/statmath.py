'''
Written By: Rahul Sharma
First Written on: January 30, 2023 at 16:07
Description: Regression and time series analysis and Mathematical Statistics library
'''
import math

class basics():

    def __init__(self):
        super.__init__()
    
    @staticmethod
    def l2Norm(v: list) -> float:
        return math.sqrt(sum([(i)**2 for i in v]))
    
    @staticmethod
    def l1Norm(v:list) -> float:
        '''
        Description: L1 norm of a vector
        Input: takes a list of values (vector) as an input
        output: l1 norm of the vector
        '''
        return abs(sum(v))

    @staticmethod
    def sampleMean(v: list) -> float:
        '''
        Description: Calculates sample mean of list of data points
        Input: v: list of data
        Output: Sample mean of the data
        '''
        return sum(v)/len(v)
    
    @staticmethod
    def sampleVariance(v:list, estimatedData: bool) -> float:
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
        subs = [math.pow(i - mean, 2) for i in v]
        return (1/N)*sum(subs)

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
        mse = (1/N) * sum([math.pow(k, 2) for k in sub])

        return mse

class mathstats():
    
    def __init__(self):
        super.__init__()
        
    def firstProdedure():
        pass