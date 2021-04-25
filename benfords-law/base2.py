from benfords_law import BenfordsLaw

SIZE = 1000

# Array of powers of 2
numbers = [1 << exp for exp in range(SIZE)]

# Print frequency distribution of leading digits
print(BenfordsLaw(numbers))
