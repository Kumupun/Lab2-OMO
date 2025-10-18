import numpy as np

def seidel(x0, epsilon, max_iter):
    A = np.array([
     [5, 1, 1, 0],
     [1, 2, 0, 0],
     [1, 0, 4, 2],
     [0, 0, 2, 3]
     ], dtype=float)
    
    b = np.array([17, 8, 28, 23], dtype=float)
    x = x0.copy()
    eps = epsilon

    for k in range(max_iter):
        x_old = x.copy()
        for i in range(len(b)):
            s1 = sum(A[i, j] * x[j] for j in range(i))       #  оновлені
            s2 = sum(A[i, j] * x_old[j] for j in range(i+1, len(b)))  #  старі
            x[i] = (b[i] - s1 - s2) / A[i, i]
        for i, val in enumerate(x):
            print(f"x{i} = {val}")
        n = np.max(np.abs(x - x_old))
        print("Похибка:", n)
        if n < eps:
            print(f"Збіжність досягнута за {k+1} ітерацій")
            break

    return x
   

