import numpy as np

def complete_sums(n, k):
    sums = [0] * (k + 1)
    sums[0] = 1  # s0 always = 1

    for i in range(1, n + 1):
        for j in range(k, 0, -1):
            sums[j] += i * sums[j - 1]

    return sums

def actual_sums(lst, k):
    sums = [0] * (k + 1)
    sums[0] = 1  # s0 always = 1

    for num in lst:
        for j in range(k, 0, -1):
            sums[j] += num * sums[j - 1]

    return sums

def compute_coeff(actual, complete, k):
    coeffs = [0] * (k + 1)
    coeffs[0] = 1
    coeffs[1] = complete[1] - actual[1]

    for i in range(2, k + 1):
        coeff = complete[i] - actual[i]
        for j in range(1, i):
            coeff -= actual[j] * coeffs[i - j]
        coeffs[i] = coeff

    return coeffs

lst = [1, 5, 15]
k = 12
n = len(lst) + k

actual = actual_sums(lst, k)
complete = complete_sums(n, k)
coefficients = compute_coeff(actual, complete, k)
roots = np.roots(coefficients)
print("The missing numbers are:")
for root in roots:
    print(f"{root* -1:.0f}")