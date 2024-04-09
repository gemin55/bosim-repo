from flask import Blueprint, render_template, request
import emoji

from datetime import datetime
import os

import mysql.connector

views = Blueprint('views', __name__)

#referring to the default page via the “/” route
@views.route("/")
def home():
    emoj = emoji.emojize(":lady_beetle:")
    return render_template("index.html", emoj=emoj)

@views.route("/about/")
def about():
    return render_template("about.html")

@views.route("/adminhome/")
def adminhome():
    return render_template("adminhome.html")

@views.route("/help/")
def help():
    return render_template("help.html")

