from flask import *

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    if 'username' in session:
        return render_template("main.html")
    return render_template("landing_page.html")