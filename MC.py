import numpy as np
import matplotlib.pyplot as plt

kB = 1.38 * 10 ** (-23)
G = 10

T = 500
N = 13  # number of particles
L = 20  # size of box
tmax = 1000000

e = 4.8**(-10)  # charge of every particle
m = 9.1 * 10**(-11)  # mass

x = np.zeros(N)  # initial coordinates
y = np.zeros(N)

for q in np.arange(0, N):   # drops points to x**4
    x[q] = (np.random.random_sample() - 0.5) * 2 * L
    y[q] = np.random.random_sample() * (L**2 - (x[q])**2) + (x[q])**2


def calc(a, b, n, d=(0, 0)):     # calculate potential energy of single particle (d - for move)
    U = 0
    R = 0
    for j in np.arange(0, N):
        if j != n:
            R += 1 / np.sqrt((a[n] + d[0] - a[j]) ** 2 + (b[n] + d[1] - b[j]) ** 2)  # SUM_j Rij
    U = e * R + (b[n] + d[1]) * m * G

    return U
xt = np.zeros(N)
yt = np.zeros(N)

for t in np.arange(0, tmax):    # time...
    for i in np.arange(0, N):   # for i-th particle do
        U1 = calc(x, y, i)   # calc its energy
        d = [0, 0]
        d[0] = 0.1 * (np.random.random_sample() - 0.5)  # random move
        d[1] = 0.1 * (np.random.random_sample() - 0.5)
        if y[i] + d[1] > (x[i] + d[0]) ** 2:        # is it still in x**2 ?
            U2 = calc(x, y, i, d)  # calc delta U
            dU = U2 - U1

            p = 0  # probability
            if dU < 0:
                p = 1
            else:
                p = np.exp(-dU / (kB * T))

            if np.random.random_sample() < p:   # move it
                x[i] += d[0]
                y[i] += d[1]
    if t / tmax * 100 == (t*100) // tmax:
        print("Processing....", t*100/tmax, "%")

    if t == tmax/10:
        xt = x
        yt = y


plt.plot(x, y, 'go')  # , xt, yt, 'ro')
#plt.xlim(-L, L)
#plt.ylim(0, L**2)
plt.savefig('500K.png')
