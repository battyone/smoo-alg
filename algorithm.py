"""
Algorithm for solving stochastic multi-objective optimization problem

author Perestoronin Daniil
"""

import math

z1 = [
    [0.1, 0.4, 0.5, 0.8, 1.0],
    [0.3, 0.5, 0.6, 0.8, 0.9],
    [0.1, 0.3, 0.5, 1.0, 1.1],
    [0.2, 0.3, 0.4, 1.0, 1.2]
]

z2 = [
    [3, 15, 25, 40, 50],
    [5, 10, 25, 35, 40],
    [5, 15, 25, 30, 60],
    [10, 15, 20, 35, 50]
]


def print_matrix(m):
    for row in m:
        for el in row:
            print(el, end=' ')
        print()


def max_element(m):
    max_el = None
    for row in m:
        for el in row:
            if max_el is None or el > max_el:
                max_el = el
    return max_el


def normalize(m, k=1):
    rows = len(m)
    cols = len(m[0])
    max_el = max_element(m)
    norm_m = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            norm_m[i][j] = k * m[i][j] / max_el
    return norm_m


def removal_uncertainties(z, lam):
    rows = len(z)
    cols = len(lam)
    unc_m = [[0 for x in range(cols)] for y in range(rows)]

    def z1(xs):
        return sum(xs)

    def z2(xs):
        return math.sqrt(sum(xs))

    for i in range(0, rows):
        for j in range(0, cols):
            unc_m[i][j] = (1 - lam[j]) * z1(z[i]) + lam[j] * z2(z[i])
    return unc_m


print_matrix(z1)
print()
print_matrix(z2)
print()

z1n = normalize(z1, 10)
z2n = normalize(z2, 10)
print_matrix(z1n)
print()
print_matrix(z2n)
print()

lam = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
z1u = removal_uncertainties(z1n, lam)
z2u = removal_uncertainties(z2n, lam)
print_matrix(z1u)
print()
print_matrix(z2u)
print()
