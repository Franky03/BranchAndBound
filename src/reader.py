import os
from math import sqrt, floor, pi, cos, acos

class Instance:
    def __init__(self, filename):
        self.file = os.path.join(filename)

        with open(self.file, 'r') as f:
            self.lines = [line.strip() for line in f.readlines() if line.strip()]
        
        self.n, self.m = map(int, self.lines[0].split()) # n variables, m constraints

        self.obj_coeffs = list(map(float, self.lines[1].split())) # objective coefficients in the objective function
        
        self.constraints = []
        for i in range(2, 2 + self.m):
            parts = list(map(float, self.lines[i].split()))
            a = parts[:-1] # restriction coefficients
            b = parts[-1] # right-hand side

            # example: 2x1 + 3x2 <= 5 
            # a = [2, 3], b = 5

            self.constraints.append((a, b))

    def get_instance(self):
        return self.n, self.m, self.obj_coeffs, self.constraints
