import numpy as np
from collections import OrderedDict, Counter


# Class to show frequency distribution of leading digits
class BenfordsLaw:
    def __init__(self, numbers, digital=False):
        self.digital = digital  # are numbers already in single digit form
        self.numbers = np.array(numbers, dtype=np.float)
        self.digits = self.leading_digits()
        self.counts = self.digit_counts()

    def __str__(self):
        # Return table of occurances
        table = ""
        for key in self.counts:
            percentage = round(self.counts[key] / len(self.digits) * 100, 1)
            table += f"{key:.0f}:  {percentage:04.1f}%\n"
        return table

    # Function to return first significant digit of a number
    def most_significant_digit(self, n):
        if n == 0:
            return np.NaN
        if n < 0:
            n = np.abs(n)
        # Loop until a single digit remains
        while n <= 10:
            n *= 10
        while n >= 10:
            n //= 10
        return n

    def leading_digits(self):
        if self.digital:
            return np.floor(self.numbers)
        else:
            # Vectorize most_significant_digit function
            vmost_significant_digit = np.vectorize(self.most_significant_digit)
            # Apply vectorized function and filter out NaNs
            digits = vmost_significant_digit(self.numbers)
            digits = digits[~np.isnan(digits)]
        return np.floor(digits)

    def digit_counts(self):
        # Sorted dict to store count of each digit
        counts = OrderedDict(sorted(Counter(self.digits).items()))
        return counts
