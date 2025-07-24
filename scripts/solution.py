import numpy as np
import math 
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

a = input("Enter the first term (a): ")
r_input = input("Enter the common ratio (r), e.g., 0.5 or 1/2: ")

try:
    a = float(a)
    r = float(Fraction(r_input))
except ValueError:
    print("Invalid input for a or r.")
    exit()
t_percent = input("Enter the tolerance (t) in % : ")
try:
    t_percent = float(t_percent)
except ValueError:
    print("Invalid input for tolerance.")
    exit()

if r < 1 and r > -1:
    
    sum_inf = equation.sum_infinite(a, r)
    t = t_percent / 100 * sum_inf
    tol =math.floor(negligibility(a, r, t).calculate_negligibility()) 
    print(tol)

    sum_n = equation.sum(a, r, tol)
    print(f"The sum to infinity is: {sum_inf}")
    print(f"The sum of the first {tol} terms is: {sum_n}")
    print(f"The number of terms needed to achieve the specified tolerance is: {tol}")

    


else:
    print("The common ratio must be between -1 and 1 (exclusive) for the infinite sum to converge.")
    exit()

#code to be optimized