from scipy.constants import physical_constants
from benfords_law import BenfordsLaw

# Array of physical constants
numbers = [constant[1][0] for constant in physical_constants.items()]

# Print frequency distribution of leading digits
print(BenfordsLaw(numbers))
