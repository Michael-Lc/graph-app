import pandas as pd
from matplotlib.figure import Figure
from random import randint
import math


def histogram(list, formating={}, interval=None):
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    df = pd.DataFrame(list, dtype=float)
    numofbins = interval
    range = None
    color = None

    if interval != None:
        xmax = math.ceil(df.max())
        xmin = math.floor(df.min())
        print("xmax: " + str(xmax))
        range = (xmin, xmax)
        numofbins = int((xmax - xmin) / interval)

    print("number of bins: " + str(numofbins))

    if len(formating) != 0:
        ax.set_xlabel(formating["xlabel"])
        ax.set_ylabel(formating["ylabel"])
        fig.suptitle(formating["title"])
        if formating["color"] != "":
            color = formating["color"]

    ax.hist(df, bins=numofbins, range=range, color=color)
    # hash = randint(1, 1000)
    # path = f"./static/graphs/histogram{hash}.png"
    path = f"./static/graphs/histogram.png"
    fig.savefig(path, format="png")
    return path