import json
import os
from datetime import datetime

from flask import Flask, render_template, url_for, request, redirect, flash, session, send_file
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv


app = Flask(__name__, static_folder="static")
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html", data={"video": "goal2.mp4"})


if __name__ == "__main__":
    app.run(debug=True)
