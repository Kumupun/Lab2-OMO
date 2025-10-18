import numpy as np

def smpl_iter(x0, epsilon, tau, max_iter):
    A = np.array([
     [4, 3, 1, 0],
     [0, 5, 2, 3],
     [-2, 2, 6, 1],
     [0, 1, 2, 7]
     ], dtype=float)
    
    b = np.array([29, 48, 38, 56], dtype=float)
    x = x0.copy()
    t = tau
    eps = epsilon

    for k in range(max_iter):
        print(f"Ітерація {k+1}:")
        m = A.dot(x) - b
        x_new = x - t * m
        for i, val in enumerate(x_new):
            print(f"x{i} = {val}")
        n = np.max(np.abs(x_new - x))
        print("Похибка:", n)
        if n < eps:
            print(f"Збіжність досягнута за {k+1} ітерацій")
            break
        x = x_new

    return x
   

