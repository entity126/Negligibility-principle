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
    
    def negl_n(self, a, r, n, t):
            n = math.log(tol*(1 - r)/a, r)
            return n   
   
x = equations()
a = float(input("Enter the first term (a): "))
r_input = input("Enter the common ratio (r), e.g., 0.5 or 1/2: ")
try:
    r = float(Fraction(r_input))
except ValueError:
    print("Invalid input for r.")
    exit()
n = int(input("Enter the number of terms (n): "))
t = float(input("Enter the tolerance (t) in % : "))

if r < 1 and r > -1:
    sum_n = x.sum(a, r, n)
    sum_inf = x.sum_infinite(a, r)
    print(f"Sum of first {n} terms: {sum_n}")
    print(f"Sum to infinity: {sum_inf}")
    
else:
    print("The common ratio must be between -1 and 1 (exclusive) for the infinite sum to converge.")
    exit()

#code to be finished 