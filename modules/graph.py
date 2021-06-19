import pandas as pd
from matplotlib.figure import Figure
from random import randint
import math


def histogram(list, interval=None, file=""):
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    df = pd.DataFrame(list, dtype=float)
    if not interval:
        numofbins = interval
    else:
        xmax = math.ceil(df.max())
        xmin = math.floor(df.min())
        print("xmax: " + str(xmax))
        numofbins = int((xmax - xmin) / interval)

    print("number of bins: " + str(numofbins))
    ax.hist(df, bins=numofbins, range=(xmin, xmax))
    # hash = randint(1, 1000)
    # path = f"./static/graphs/histogram{hash}.png"
    path = f"./static/graphs/histogram.png"
    fig.savefig(path, format="png")
    return path