from flask import render_template, Blueprint, flash

main_ui = Blueprint('main_ui', __name__)

@main_ui.route('/')
def index():
    flash("Welcome To Our Website!")
    return render_template("index.html"
                            )