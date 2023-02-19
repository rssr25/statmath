'''
Written By: Rahul Sharma
First Written on: January 30, 2023 at 16:07
Description: Regression and time series analysis and Mathematical Statistics library
'''

import numpy as np

#TODO: Test todo
class statistics():

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def tstatistic(Z: np.ndarray, mu_0:np.float64) -> np.float64:
        '''
        Description: Student's T-test statistic assumming i.i.d normally distributed data
        Input: Data Z, null hypothesis mu = mu_0
        Output: t-statistic
        '''
        N = len(Z)
        Tn = np.divide(np.multiply(np.square(N), basics.sampleMean(Z) - mu_0), basics.sampleVariance(Z, True))
        return Tn


class basics():

    def __init__(self) -> None:
        pass
    
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

        print(mean)
        print(v - mean)
        subs = np.power(v - mean, 2)
        print(subs)
        return (1/N)*np.sum(subs)

    @staticmethod
    def sampleCovariance(v1:np.ndarray, v2:np.ndarray) -> float:
        '''
        Description: calculates the sample covariance between two lists of data points. Assuming i.i.d. data.
        Input: two lists of equal lengths
        Output: sample covariance of the data
        '''
        assert len(v1) == len(v2), "The vectors should be of equal length"
        N = len(v1)
        mean_v1 = basics.sampleMean(v1)
        mean_v2 = basics.sampleMean(v2)

        print(mean_v1, mean_v2)
        print(v1 - mean_v1)
        print(v2 - mean_v2)
        print((v1-mean_v1) * (v2 - mean_v2))
        print(np.sum((v1-mean_v1) * (v2 - mean_v2)))

        return (1/N)*np.sum((v1-mean_v1) * (v2 - mean_v2))
    
    @staticmethod
    def getRandomNoise(mu, sigma, n):
        
        return np.random.normal(mu, sigma, n)


class rtsa():
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def mse(estimate: list, original: list) -> np.float64:
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

    
    def expectedSquaredDeviation_linearRegression(X: np.ndarray, Y: np.ndarray) -> np.float64:
        
        '''
        Description: find the least squares for LR model of type y = b1 + b2x where x is the independent variable
        Input: (X, Y) random variables
        Output: sum(Y - b1 - b2X)^2 where X and Y are vectors 
        '''
        x_bar = basics.sampleMean(X)
        y_bar = basics.sampleMean(Y)

        b2_hat = np.divide(np.sum(np.multiply(Y - y_bar, X - x_bar)), np.sum(X - x_bar))
        b1_hat  = basics.sampleMean(Y) - b2_hat*x_bar

        return np.sum(Y - b1_hat - b2_hat*X)**2


class mathstats():
    
    def __init__(self) -> None:
        pass
        
    def firstProdedure():
        pass