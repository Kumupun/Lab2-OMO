import quad 
import simpl_iter
import seidel
import numpy as np

def print_menu():
    print("Menu:")
    print("1. Find solution using Simple Iteration method")
    print("2. Find solution using Quadratic method")
    print("3. Find solution using Seidel's method")
    print("4. Exit")

def main():
    print_menu()
    c= input("Choose an option (1-3): ")
    if c == '1':
        print("Simple Iteration Method Selected.")
        print("Enter initial guess :")
        x0 = np.array(list(map(float, input().split())))
        epsilon = float(input("Enter epsilon: "))
        tau = float(input("Enter factor tau: "))
        max_iter = int(input("Enter maximum number of iterations: "))
        result = simpl_iter.smpl_iter(x0, epsilon, tau, max_iter)
        if result is not None:
            for i, val in enumerate(result):
                print(f"x{i} = {val}")
        else:
            print("No root found.")
        return 0
    
    elif c == '2':
        print("Quadratic Method Selected.")
        print("Enter initial guess :")
        x0 = np.array(list(map(float, input().split())))
        result = quad.quad(x0)
        if result is not None:
            for i, val in enumerate(result):
                print(f"x{i} = {val}")
        else:
            print("No root found.")
        return 0
    
    elif c == '3':
        print("Seidel's Method Selected.")
        print("Enter initial guess :")
        x0 = np.array(list(map(float, input().split())))
        epsilon = float(input("Enter epsilon: "))
        max_iter = int(input("Enter maximum number of iterations: "))
        result = seidel.seidel(x0, epsilon, max_iter)
        if result is not None:
            for i, val in enumerate(result):
                print(f"x{i} = {val}")
        else:
            print("No root found.")
        return 0
    
    elif c == '4':
        print("Exiting the program.")
        return 0
    return 0
main()