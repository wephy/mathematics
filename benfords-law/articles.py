import urllib
from bs4 import BeautifulSoup
from benfords_law import BenfordsLaw

URL = r"https://en.wikipedia.org/wiki/Benford%27s_law"  # URL to open

# Extract text from webpage
page = urllib.request.urlopen(URL)
soup = BeautifulSoup(page, "html.parser")
soup = soup.find("div", {"id": "content"})  # For wikipedia pages
text = soup.get_text()


# Function to return whether a string is a valid number
def isnumber(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


# Get all valid numbers from text
numbers = [n for n in text.split() if isnumber(n)]

# Print frequency distribution of leading digits
print(BenfordsLaw(numbers))
