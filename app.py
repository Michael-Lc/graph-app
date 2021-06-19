from flask import Flask, render_template, url_for, request, redirect

# from flask_sqlalchemy import SQLAlchemy
from modules.graph import histogram
import numpy as np

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
# db = SQLAlchemy(app)


@app.route("/", methods=["POST", "GET"])
def index():
    seperators = [" ", ", ", ",", "\t"]
    if request.method == "POST":
        data = request.form["data"]
        try:
            interval = float(request.form["class-interval"])
        except:
            interval = None  # defaul value

        for sep in seperators:
            if sep in data:
                datalist = data.split(sep)
                print(datalist)

        graph = histogram(datalist, interval=interval)
    else:
        graph = histogram(list=np.random.uniform(0, 10, 50))
    return render_template("index.html", graph=graph, data=data, interval=interval)


if __name__ == "__main__":
    app.run(debug=True)