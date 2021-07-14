import pandas as pd
from matplotlib.figure import Figure
from random import randint
import math


def histogram(list, interval=None, args=[]):
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    df = pd.DataFrame(list, dtype=float)
    # default values
    numofbins = None
    range = None
    color = None

    # calculate number of bins if interval is available
    if interval != None:
        xmax, xmin = math.ceil(df.max()), math.floor(df.min())
        # print("xmax: " + str(xmax))
        range = (xmin, xmax)
        numofbins = int((xmax - xmin) / interval)

    # print("number of bins: " + str(numofbins))

    # set graph formating if values are available
    if len(args) != 0:
        ax.set_xlabel(args["xlabel"])
        ax.set_ylabel(args["ylabel"])
        fig.suptitle(args["title"])
        if args["graph_color"] != "":
            color = args["graph_color"]

    ax.hist(df, bins=numofbins, range=range, color=color)
    # hash = randint(1, 1000)
    # path = f"./static/graphs/histogram{hash}.png"
    path = f"./static/graphs/histogram.png"
    fig.savefig(path, format="png")
    return path