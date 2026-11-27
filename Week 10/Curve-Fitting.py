import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data = np.genfromtxt("curve-data.csv", delimiter=",")
xdata = data[:,0]
ydata = data[:,1]



def f(x, a, b, c, d):#create cubic function
    return a*x**3 + b*x**2 + c*x + d

fit = curve_fit(f, xdata, ydata)
a = fit[0][0]
b = fit[0][1]
c = fit[0][2]
d = fit[0][3]
print(f"{a}*x**3 + {b}*x**2 + {c}*x + {d}")
plt.title("Curve fitting with cubic function")
plt.xlabel("x values")
plt.ylabel(r"$Y=ax^3+bx^2+cx+d$")
plt.scatter(xdata,ydata)#scatterplot
plt.plot(xdata, f(xdata, a, b, c, d), color="red")#Plots the curve
plt.show()
