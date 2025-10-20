import numpy as np

def quad(x0):
    A = np.array([
     [1, 2, 0, ],
     [2, 2, 4, ],
     [0, 4, 3 ],
     ], dtype=float)
    
    b = np.array([5, 22, 20], dtype=float)
    x = x0.copy()
    n = len(b)
    S = np.zeros((n, n))
    D = np.zeros(n)

    for i in range(n):
        delta = A[i, i]
        for p in range(i):
            delta -= S[p, i] ** 2 * D[p]
        D[i] = np.sign(delta)
        if D[i] == 0:
            D[i] = 1
        S[i, i] = np.sqrt(abs(delta))
        for j in range(i + 1, n):
            sum_ = 0
            for p in range(i):
                sum_ += S[p, i] * D[p] * S[p, j]
            S[i, j] = (A[i, j] - sum_) / (D[i] * S[i, i])

    print("Матриця S: \n", S)
    print(f"\nМатриця D: \n{np.diag(D)}")

    y = np.linalg.solve(S.T @ np.diag(D), b)
    x = np.linalg.solve(S, y)

    return x
   

