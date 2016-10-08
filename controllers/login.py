from flask import *
from oauth2client import client, crypt

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods=['POST'])
def login_route():
    id_token = request.get_json()['id_token']
    # (Receive token by HTTPS POST)
    CLIENT_ID = '1016070486190-cnlpostiqso9fjoscifbdro2mb7i0u1d.apps.googleusercontent.com'
    try:
        id_info = client.verify_id_token(id_token, CLIENT_ID)
        # If multiple clients access the backend server:
        if id_info['aud'] != CLIENT_ID:
            raise crypt.AppIdentityError("Unrecognized client.")
        if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")
        # if id_info['hd'] != "http://localhost":
        #     raise crypt.AppIdentityError("Wrong hosted domain.")
    except crypt.AppIdentityError:
        print('error')
    userid = id_info['sub']
    session['username'] = request.get_json()['username']
    return jsonify({}), 200