import numpy as np
import math 
import matplotlib.pyplot as plt  
from fractions import Fraction

class equations():

    def sum(self, a, r, n):
            sum = a*(1-pow(r, n)) / (1 - r)
            return sum
    
    def sum_infinite(self, a, r):
            sum = a / (1 - r)
            return sum
    
    def actual_tol(self, a, r, n):
            tol = a*pow(r, n)/(1 - r)
            return tol
    
   
class negligibility():

    def __init__(self, a, r, t):
        self.a = a
        self.r = r
        self.t = t

        
        self.argument = t * (1 - r) / a

    def calculate_negligibility(self):
        if self.argument <= 0 or self.r <= 0 or self.r == 1:
            print("Error: Invalid argument for logarithm or common ratio. Check your inputs.")
            exit()
        self.n = math.log(self.argument) / math.log(self.r)
        return self.n
    

equation = equations()

a = 5
r_input = 0.1

try:
    a = float(a)
    r = float(Fraction(r_input))
except ValueError:
    print("Invalid input for a or r.")
    exit()
t_percent = 0.001
try:
    t_percent = float(t_percent)
except ValueError:
    print("Invalid input for tolerance.")
    exit()

if r < 1 and r > -1:
    # Terms of the first 50 terms
    first_50_terms = a * np.power(r, np.arange(50))
    print(f"First 50 terms: {first_50_terms}")

    sum_inf = equation.sum_infinite(a, r)
    t = t_percent / 100 * sum_inf
    tol = math.floor(negligibility(a, r, t).calculate_negligibility())
    print(tol)

    # Store terms in a numpy array
    terms_array = a * np.power(r, np.arange(tol))
    # Or, as a Python list:
    terms_list = [a * r**k for k in range(tol)]

    sum_n = equation.sum(a, r, tol)
    print(f"The sum to infinity is: {sum_inf}")
    print(f"The sum of the first {tol} terms is: {sum_n}")
    print(f"The number of terms needed to achieve the specified tolerance is: {tol}")
    print(f"Terms as numpy array: {terms_array}")
    print(f"Terms as list: {terms_list}")

    # Plotting the terms
    plt.plot(first_50_terms, marker='o', linestyle='-', color='r')
    plt.plot(terms_array, marker='o', linestyle='-', color='b')
    plt.title('Terms of the Geometric Series')
    plt.xlabel('Term Index')
    plt.show()
    


else:
    print("The common ratio must be between -1 and 1 (exclusive) for the infinite sum to converge.")
    exit()

#code to be optimized