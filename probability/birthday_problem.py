import matplotlib.pyplot as plt
from PIL import Image

# Parameters
IMAGE_SIZE = (1750, 1000)
IMAGE_FNAME = "birthday_problem.jpg"

# Solarized colours
sol_Base03 = "#002b36"
sol_Red = "#dc322f"

# Create Figure with one axes
fig, ax = plt.subplots(1, 1, figsize=(14, 8))
plt.style.use("Solarize_Light2")

# Create title and labels
plt.rc("text", usetex=True)
title = f"$\\textnormal{{The birthday problem}}$"
ylabel = f"$\\textnormal{{probability of birthday match}}$"
xlabel = f"$\\textnormal{{number of people}}$"
ax.set_title(title, fontsize=25, pad=35, color=sol_Base03)
ax.set_yticks([0, 0.5, 1])
ax.set_yticks([0.25, 0.75], minor=True)
ax.set_ylabel(ylabel, fontsize=20, rotation=90, labelpad=15)
ax.set_xlabel(xlabel, fontsize=20, rotation=0, labelpad=15)


def p_share_birthday(people):
    complement = 1 / (365 ** people)
    for k in range(people):
        complement *= 365 - k
    return 1 - complement


# Create horizontal line at y=0.5
ax.axhline(y=0.5, linewidth=1, color=sol_Red)

# Add points to scatter
for n in range(1, 101):
    ax.scatter(n, p_share_birthday(n), color="k", s=5)

# Save fig
fig.tight_layout(pad=3)
fig.savefig(IMAGE_FNAME, dpi=300)

# Resize with interpolation
im = Image.open(IMAGE_FNAME)
im = im.resize(IMAGE_SIZE, Image.LANCZOS)
im.save(IMAGE_FNAME)
