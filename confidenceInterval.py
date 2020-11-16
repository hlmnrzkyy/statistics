# a function to find confidence interval:
# confidenceInterval(var1, var2, var3, var4)
#
# the function's variable:
# var1 = n or population
# var2 = sample mean
# var3 = sigma or standard deviation
# var4 = desired confidence level (80, 85, 90, 95, etc.)
#
# the result is a list:
# [lower value, upper value]
#
# to run this script, you must install python 3.7 or latest version with module :
# numpy, and
# scipy
import numpy as np
from scipy.integrate import simps

def confidenceInterval(var1, var2, var3, var4):
    def f1(x, mu, sigma):
        # result = 2*x
        result = (1.0 / (sigma * np.sqrt(2.0 * np.pi))) * (np.exp((-1.0) * (1.0 / 2.0) * ((x - mu) / sigma) ** 2))
        return result

    n = float(var1)
    mu = float(var2)
    sigma = float(var3) / np.sqrt(n)
    confidenceLevel = float(var4) / 100
    z = 0

    while z < 3.49:
        xList = []
        x = mu - z * sigma
        xList.append(x)
        while x < (mu + (((z * sigma) - 0.01))):
             x += 0.01
             xList.append(x)

        x = np.asarray(xList)
        y = f1(x, mu, sigma)

        I = simps(y, x)
        if round(I, 2) == confidenceLevel:
            zFinal = z
            iFinal = I
        z += 0.01

    lowerLimit = mu - (zFinal * sigma)
    upperLimit = mu + (zFinal * sigma)
    confidenceInterval = [lowerLimit, upperLimit]
    return confidenceInterval

# example to use this code (uncomment the script below):
# print(confidenceInterval(25, 145, 35, 90))
