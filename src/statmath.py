'''
Written By: Rahul Sharma
First Written on: January 30, 2023 at 16:07
Description: Regression and time series analysis and Mathematical Statistics library
'''

class rtsa():
    
    def __init__(self):
        super.__init__()

    @staticmethod
    def l2Norm(a, b) -> float:
        return (a-b)**2

    @staticmethod
    def mse(estimate: list, original: list) -> float:
        '''
        Description: calculates mean-squared error between estimated and original data
        input: two lists
        output: mse between the list of data
        '''

        assert len(estimate) == len(original), "estimates and data are not of equal length"
        N = len(estimate)
        sub = [rtsa.l2Norm(a, b) for a, b in zip(estimate, original)]
        mse = (1/N) * sum(sub)

        return mse

class mathstats():
    
    def __init__(self):
        super.__init__()
        
    def firstProdedure():
        pass