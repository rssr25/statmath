from setuptools import setup
setup(
        name= 'statmath', 
        version='0.0.1', 
        description='regression and time series analysis and mathematical statistics library for students and professionals', 
        py_modules=["rtsa", "statistical"],
        package_dir={'': 'src'},
    )