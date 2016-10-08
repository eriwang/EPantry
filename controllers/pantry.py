from flask import *
import pymongo
from extensions import db

pantry = Blueprint('pantry', __name__, template_folder='templates')

@login.route('/pantry', methods=['GET', 'POST', 'POST'])
def pantry():
  if request.get_json('method') == "GET":
    logged_user = session['username']
    posts = db.posts
