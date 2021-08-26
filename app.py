from flask import Flask, render_template, request

from modules.graph import histogram
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    # default form data values
    data = [
        ("data", ""),
        ("class-interval", ""),
        ("graph-title", ""),
        ("xlabel", ""),
        ("ylabel", ""),
        ("graph_color", ""),
    ]

    if request.method == "POST":
        data = request.form["data"]
        # Check that data is not empty
        if len(data) < 1 or data.isspace():
            return render_template(
                "index.html",
                graph="",
                data=data,
                error="Please make sure you entered valid data",
            )

        seperators = [" ", ", ", ",", "\t"]  # list of data seperators
        data = data.strip()
        print(request.form)
        # Cast class interval to float
        # else set default value of None
        try:
            interval = float(request.form["class-interval"])
        except:
            interval = None  # default value

        # Data splitting
        for sep in seperators:
            if sep in data:
                datalist = data.split(sep)
                print(datalist)

        graph = histogram(list=datalist, interval=interval, args=request.form)
        return render_template("index.html", graph=graph, data=request.form, error="")
    else:
        graph = histogram(list=np.random.uniform(0, 10, 50))
        return render_template("index.html", graph=graph, data=data, error="")


if __name__ == "__main__":
    app.run(debug=True)