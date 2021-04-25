import numpy as np
from benfords_law import BenfordsLaw

SIZE = 1_000_000  # How many random numbers to generate

# Array of random numbers between 0 and 1
random_numbers = np.random.rand(SIZE)

# Apply 10 ** x and get first digit
numbers = np.power(10, random_numbers)

# Print frequency distribution of leading digits
print(BenfordsLaw(numbers, digital=True))
