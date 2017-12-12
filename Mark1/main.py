from scipy import stats
import scipy.integrate as integrate
import numpy as np
import math
import random
import matplotlib.pyplot as plt


def p𝜏ⁱ(x):
    if x > 0 and x <= math.pi :
        return math.sin(x)/2
    else:
        return 0



class myRV(stats.rv_continuous):
    def _pdf(self, x, *args):
        return np.where(0 < x <= math.pi, [math.sin(x)/2], [0.])

    def _cdf(self, x, *args):
        pass

    def _stats(self):
        return 0., 0., 0., 0.

p = myRV()
print("Математичне сподівання: " + str(p.expect()))



def get_value(f, a, b):
    return integrate.quad(f, a, b)[0]


def variance(x):
    return p𝜏ⁱ(x) * (x - p.expect())**2

print("Дисперсія: " + str(get_value(variance, 0, math.pi)))


def make_discrete(f, a, b, n):
    pⁱ = [0]
    xⁱ = []
    div = (b-a)/n
    for i in range(0, n):
        x = a + i * div
        inte = get_value(f, x, x + div)
        pⁱ.append(inte + pⁱ[-1])
        xⁱ.append(x)
    pⁱ.pop(0)
    return xⁱ, pⁱ


def get_modeled_value(f, a, b, countPoints, expectedValue):
    discrete = make_discrete(f, a, b, countPoints)
    i = 1
    try :
        while discrete[1][i] < expectedValue and i <= len(discrete[1]):
            i += 1

        return discrete[0][i - 1]
    except IndexError:
        return discrete[0][-1]


print("\nModelate:")
a = 0
b = math.pi
n = 20
sum = 0.0
mass = []

m = 20

for _ in range(0, m):
    value = np.random.rand() #random.uniform(0, 1)
    modeled = get_modeled_value(p𝜏ⁱ, a, b, n, value)
    print(modeled)
    sum += modeled
    mass.append(modeled)

print("\nAverage value = ", sum/m)


plt.plot(range(1, m+1), mass, "ro")
plt.xlabel('Modeled values')
plt.ylabel('Iteration')
plt.title('Modeling')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

