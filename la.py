import numpy as np
import scipy.linalg as linalg

e = 0.01
A = np.array([(5, 1, 2),
              (1, 4, 1),
            (2, 1, 3)])

imax = 0
jmax = 1
max = abs(A[0, 1])  # initial max
Hs = []
while max > e:
    imax = 0  # reinitial max
    jmax = 1
    max = abs(A[0, 1])
    for i in np.arange(0, np.size(A, 0)):   # search new max
        for j in np.arange(i+1, np.size(A, 1)):
            if abs(A[i, j]) > max:
                max = abs(A[i, j])
                imax = i
                jmax = j

    if A[imax, imax] - A[jmax, jmax] != 0:  # count phi
        phi = 0.5 * np.arctan(2*A[imax, jmax] / (A[imax, imax] - A[jmax, jmax]))
    else:
        phi = 0.5 * np.pi / 2

    H = np.zeros(np.size(A)).reshape(np.size(A, 0), np.size(A, 1))  # create rotate matrix
    for i in np.arange(0, np.size(A, 0)):
        if i == imax or i == jmax:
            H[i, i] = np.cos(phi)
        else:
            H[i, i] = 1
    H[imax, jmax] = -np.sin(phi)
    H[jmax, imax] = np.sin(phi)

    Hs.append(H)    # append H to vector of every H from every iterate

    A = np.dot( np.dot(H.transpose(), A), H )

SV = Hs[0]  # multiply all H's
for i in np.arange(1, np.size(Hs, 0)):
    SV = np.dot(SV, Hs[i])

print("------MY------") # so print
print(SV)

for i in np.arange(0, np.size(A, 0)):
    print("eigenvalue ", i, " = ", A[i, i])

print("---LIB---")  # Libs values to compare

eigen_values, eigen_vectors = linalg.eig(A)

print(eigen_vectors)
print("EVal: \n", eigen_values)


  # algorithm here:  http://mathhelpplanet.com/static.php?p=metody-resheniya-zadach-o-sobstvennykh-znacheniyakh-i-vektorakh-matritsy