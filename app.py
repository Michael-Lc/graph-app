from flask import Flask, render_template, request

from modules.graph import histogram
from modules.errorhandlers import returnError
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    data = request.form
    if request.method == "POST":
        # Check that data is not empty
        data = request.form["data"]
        if len(data) < 1 or data.isspace():
            return returnError("data-error", data=request.form)

        seperators = [" ", ", ", ",", "\t"]  # list of data seperators
        data = data.strip()
        print(request.form)

        # Cast class interval to float
        # else return error message
        interval = request.form["class-interval"]
        if len(interval) > 0 and not interval.isspace():
            try:
                interval = float(request.form["class-interval"])
            except:
                return returnError("interval-error", data=request.form)
        else:
            interval = None  # default value

        # Data splitting
        for sep in seperators:
            if sep in data:
                datalist = data.split(sep)
                print(datalist)

        graph = histogram(list=datalist, interval=interval, args=request.form)
        return render_template("index.html", graph=graph, data=request.form, error="")
    else:
        graph = histogram(
            list=np.random.uniform(0, 10, 50)
        )  # Default random graph values
        return render_template("index.html", graph=graph, data=data, error="")


if __name__ == "__main__":
    app.run(debug=True)