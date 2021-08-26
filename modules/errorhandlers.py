from flask import render_template


def returnError(error, data):
    if error == "data-error":
        return render_template(
            "index.html",
            graph="",
            data=data,
            error="Please make sure you entered valid data",
        )