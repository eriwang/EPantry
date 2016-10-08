from flask import *

logout = Blueprint('logout', __name__, template_folder='templates')

@logout.route('/logout', methods=['POST'])
def logout():

