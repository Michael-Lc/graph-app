from flask import Flask, render_template, request

from modules.graph import histogram
import numpy as np

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    seperators = [" ", ", ", ",", "\t"]

    if request.method == "POST":
        data = request.form["data"]
        formating = {
            "color": request.form["graph_color"],
            "xlabel": request.form["xlabel"],
            "ylabel": request.form["ylabel"],
            "title": request.form["title"],
        }

        try:
            interval = float(request.form["class-interval"])
        except:
            interval = None  # default value

        for sep in seperators:
            if sep in data:
                datalist = data.split(sep)
                print(datalist)

        graph = histogram(datalist, formating=formating, interval=interval)
        return render_template(
            "index.html", graph=graph, data=data, interval=interval, formating=formating
        )
    else:
        graph = histogram(list=np.random.uniform(0, 10, 50))
        formating = {
            "color": "",
            "xlabel": "",
            "ylabel": "",
            "title": "",
        }
        return render_template("index.html", graph=graph, formating=formating)


if __name__ == "__main__":
    app.run(debug=True)