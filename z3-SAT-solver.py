
# Import the libraries
from z3 import *

# We will check if the following (simple) formula is satisfiable
# f = (x1 or x3 or x2) and (~X2 or x4 or x1)

# Define the Boolean variables
x1 = Bool("x1")
x2 = Bool("x2")
x3 = Bool("x3")
x4 = Bool("x4")

# First clause: (x1 or x3 or x2)
c1 = Or([x1, x3, x2])

# Second Clause: (~X2 or x4 or x1)
c2 = Or([Not(x2), x4, x1])

# c1 & c2 anded together
c1_and_c2 = And([c1, c2])

# Initiate and call the solver
s = Solver()

# Add the clause to the solver
s.add(c1_and_c2)

# Check
print(s.check())

# Get the values that satisfied the equation/
print(s.model())






