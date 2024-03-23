import atexit
import os
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    flash,
    url_for,
    send_from_directory,
)
from werkzeug.utils import secure_filename
import random
import shutil


app = Flask(__name__)
app.secret_key = "super_secret_key"


@app.route("/")
def upload_form():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
