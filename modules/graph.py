import pandas as pd
from matplotlib.figure import Figure
from random import randint


def histogram(list, file=""):
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    df = pd.DataFrame(list, dtype=float)
    ax.hist(df, bins=5)
    hash = randint(1, 1000)
    # path = f"./static/graphs/histogram{hash}.png"
    path = f"./static/graphs/histogram.png"
    fig.savefig(path, format="png")
    return path