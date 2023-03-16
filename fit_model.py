from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
import numpy as np
import math


def func(x, a, b, c):
    return c + a * np.exp(-b * x)


def fit(time_avg_small_obs, x=[]):
    popt, error = curve_fit(func, x, time_avg_small_obs, maxfev = 5000)
    a, b, c = popt
    #print(popt)
    return a, b, c


if __name__ == "__main__":

    xx = [1, 3, 5, 7, 11]
    obs = [6.7142, 4.6016, 2.377, 2.0072, 2.0604]
    print(list(obs))
    fit(obs, x=xx)

    #pyplot.legend()
    #pyplot.show()

"""
[2.6997, 1.5539, 1.1248, 0.8235, 0.742]
[1.5771, 0.9657, 0.7235, 0.532, 0.4258]
[7.1388, 3.851, 2.6335, 1.7553, 1.4703]
[1.1526, 0.737, 0.5731, 0.3779, 0.3053]
[4.1399, 2.3149, 1.6335, 1.1855, 1.0193]
[5.4937, 3.0134, 2.0954, 1.4294, 1.2244]
[4.4701, 2.5832, 1.8695, 1.3552, 1.1824]
[13.3427, 7.4599, 5.1508, 3.8193, 3.4795]
[5.9307, 3.35, 2.3241, 1.7244, 1.5702]
[1.499, 0.8641, 0.6139, 0.4637, 0.4356]
"""

"""
[6.7142, 4.6016, 2.377, 2.0072, 2.0604]
[62.7045, 25.1781, 15.2525, 10.9927, 10.2743]
[11.9939, 4.8691, 3.1651, 2.4602, 2.1821]
[30.2226, 11.6683, 7.525, 5.4474, 4.9812]
[58.2168, 22.3522, 13.6881, 9.7849, 8.8391]
[6.4216, 2.5995, 1.6837, 1.2752, 1.2245]
[29.2068, 11.1685, 6.8192, 5.1762, 4.6323]
[59.5509, 20.9353, 12.7603, 9.6313, 8.4832]
[63.7077, 22.0757, 13.5778, 10.4171, 9.0457]
[30.0318, 10.6582, 6.6872, 5.145, 4.514]
[59.5694, 20.916, 12.9922, 9.9564, 8.7734]
[60.2691, 21.8427, 13.6398, 10.318, 9.1986]
[15.9463, 6.0378, 4.0094, 3.1843, 2.9266]
[15.6861, 5.9959, 3.9774, 3.1274, 2.8591]
[16.5236, 6.3535, 4.2517, 3.3387, 3.0575]
[38.9661, 16.3884, 10.3452, 8.9548, 9.0887]
[6.278, 2.8345, 1.9144, 1.6854, 1.7197]
[1.5381, 0.7066, 0.49, 0.4337, 0.45]
"""