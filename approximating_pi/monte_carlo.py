import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import StrMethodFormatter, NullFormatter

# Parameters
POINTS = 100_000
FRAMES = 250

# Solarized colours
sol_Base03 = "#002b36"
sol_Red = "#dc322f"
sol_Blue = "#268bd2"

# Create Figure with two axes
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
ax1, ax2 = axes[0], axes[1]
plt.style.use("Solarize_Light2")

# Create scatter plot
sim = ax1.scatter([], [], marker="o", s=1, animated=True)
ax1.axis([-1.05, 1.05, -1.05, 1.05])

# Create circle on ax1
ax1.add_patch(plt.Circle((0, 0), 1, lw=2, color=sol_Base03, fill=False))

# Set scale to logarithmic and adjust ticks
ax2.set_xscale("log")
ax2.xaxis.set_major_formatter(StrMethodFormatter("{x:.0f}"))
ax2.xaxis.set_minor_formatter(NullFormatter())
ax2.axis([1, 2, np.pi - 1, np.pi + 1])
ax2.set_yticks(np.concatenate([np.arange(2, 5, 0.25), [np.pi]]))

# Create line plot
(line,) = ax2.plot([], [], color=sol_Base03, animated=True)
approximations = [[], []]

# Create horizontal line at y=pi
ax2.axhline(np.pi, ls="--", lw=1, color=sol_Red)

# Create text on ax2
pi_text = ax2.annotate(
    "",
    (0.02, 0.95),
    xycoords="axes fraction",
    fontsize=20,
    fontfamily="cmr10",
    color=sol_Base03,
    animated=True,
    usetex=True,
)

# Vectorized function which calculates if a point (x, y) is within the circle
v_in_circle = np.vectorize(lambda x, y: True if x ** 2 + y ** 2 < 1 else False)

# Vectorized function which returns desired colour
v_color = np.vectorize(lambda x: sol_Red if (x is True) else sol_Blue)

# Create points data
throws = (np.random.rand(POINTS, 2) - 0.5) * 2
throws_transposed = np.transpose(throws)
throws_in = v_in_circle(throws_transposed[0], throws_transposed[1])
throws_counts = np.cumsum(throws_in)
throws_colors = v_color(throws_in)


def init():
    return (fig,)


def animate(i):
    # If x value already plotted, render another frame without any changes
    if i in approximations[0]:
        return (fig,)

    # Add first i points to scatter and colour them
    sim.set_offsets(throws[:i, :])
    sim.set_facecolor(throws_colors[:i])

    # Calculate pi approximation and update data
    pi_approx = 4 * throws_counts[i - 1] / (i)
    approximations[1].append(pi_approx)
    approximations[0].append(i)

    # Update pi approximation graph and text
    pi_text.set_text(f"$\\pi\\approx{{{pi_approx:.5f}}}$")
    line.set_data(approximations[0], approximations[1])

    # Set new axis limits
    ax2.axis([1, i + 3, np.pi - 1, np.pi + 1])
    return (fig,)


# Construct animation, using logarithmic steps for x values
fig.tight_layout(pad=3)
log_frames = np.logspace(0, np.log10(POINTS - 1), num=FRAMES).astype(int)
anim = animation.FuncAnimation(
    fig,
    animate,
    init_func=init,
    interval=50,
    frames=np.concatenate(([0], log_frames)),
    blit=True,
)
anim.save("monte_carlo_pi.mp4", fps=24, dpi=300)
