from flask import Flask, render_template, request

from modules.graph import histogram
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        seperators = [" ", ", ", ",", "\t"]  # list of data seperators
        data = request.form["data"]
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
        return render_template("index.html", graph=graph, data=request.form)
    else:
        graph = histogram(list=np.random.uniform(0, 10, 50))
        # default form data values
        data = [
            ("data", ""),
            ("class-interval", ""),
            ("title", ""),
            ("xlabel", ""),
            ("ylabel", ""),
            ("graph_color", ""),
        ]
        return render_template("index.html", graph=graph, data=data)


if __name__ == "__main__":
    app.run(debug=True)