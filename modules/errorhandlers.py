from flask import render_template

# Dict of error "codes" and corresponding messages.
errors = {
    "data-error": "Please make sure you entered valid data",
    "interval-error": "Please make sure you entered a valid class-interval value",
}


def returnError(error, data):
    if error in errors:
        return render_template(
            "index.html",
            graph="",
            data=data,
            error=errors[error],
        )
    # If error code not found send generic error message
    else:
        return render_template(
            "index.html",
            graph="",
            data=data,
            error="There was an issue, please check and try again",
        )
