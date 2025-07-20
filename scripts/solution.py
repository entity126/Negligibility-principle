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

    def __init__(self, a, r, n, t):
        self.a = a
        self.r = r
        self.n = n
        self.t = t

        self.numerator = t * (1 - r)
        self.denominator = a
        self.argument = self.numerator / self.denominator
        self.floored_argument = math.floor(self.argument)

    def calculate_negligibility(self):
        self.n = math.log(self.floored_argument) / math.log(r)
        return self.n
    

x = equations()
a = float(input("Enter the first term (a): "))
r_input = input("Enter the common ratio (r), e.g., 0.5 or 1/2: ")


try:
    r = float(Fraction(r_input))
except ValueError:
    print("Invalid input for r.")
    exit()
n = int(input("Enter the number of terms (n): "))
t_percent = float(input("Enter the tolerance (t) in % : "))

if r < 1 and r > -1:
    sum_n = x.sum(a, r, n)
    sum_inf = x.sum_infinite(a, r)
    t = t_percent / 100 * sum_inf

    
    
    
    
    
else:
    print("The common ratio must be between -1 and 1 (exclusive) for the infinite sum to converge.")
    exit()

#code to be finished 