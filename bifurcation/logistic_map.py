import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Parameters
ITERATIONS = 600
POINTS = 10_000
DRAW = 300
IMAGE_SIZE = (2000, 1000)
IMAGE_FNAME = "bifurcation_diagram.png"

# Create Figure with one axes
fig, ax = plt.subplots(1, 1, figsize=(16, 8))
plt.style.use("Solarize_Light2")

# Set ticks and limits
ax.set_xticks(np.linspace(2, 4, 5))
ax.set_yticks(np.linspace(0, 1, 5))
ax.set_xlim([2, 4])
ax.set_ylim([0, 1])

# Create title and labels
plt.rc("text", usetex=True)
title1 = f"$\\textnormal{{Logistic map}}$" + "\n"
title2 = f"$x_{{n+1}}=\\lambda\\,x_{{n}}\\,(1-x_{{n}})$"
ylabel = f"$\\chi$"
xlabel = f"$\\lambda$"
ax.set_title(title1 + title2, fontsize=25, pad=35)
ax.set_ylabel(ylabel, fontsize=20, rotation=0, labelpad=15)
ax.set_xlabel(xlabel, fontsize=20, rotation=0, labelpad=15)


def logistic_map(r, x):
    return r * x * (1 - x)


# Iterate through each x value starting at 0.5
x = 0.5 * np.ones(POINTS)
r = np.linspace(2, 4, POINTS)
for i in range(ITERATIONS):
    x = logistic_map(r, x)
    if i > ITERATIONS - DRAW:
        ax.plot(r, x, ",k", alpha=0.3)


# Save fig
fig.tight_layout(pad=3)
plt.savefig(IMAGE_FNAME, dpi=300)

# Resize with interpolation
im = Image.open(IMAGE_FNAME)
im = im.resize(IMAGE_SIZE, Image.LANCZOS)
im.save(IMAGE_FNAME)
