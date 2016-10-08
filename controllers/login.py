from flask import *
from oauth2client import client, crypt

login = Blueprint('login', __name__, template_folder='templates')

@login.route('/login', methods=['POST'])
def login():
  id_token = request.get_json('id_token')
# (Receive token by HTTPS POST)

  try:
    idinfo = client.verify_id_token(token, CLIENT_ID)
    # If multiple clients access the backend server:
    if idinfo['aud'] not in [ANDROID_CLIENT_ID, IOS_CLIENT_ID, WEB_CLIENT_ID]:
        raise crypt.AppIdentityError("Unrecognized client.")
    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise crypt.AppIdentityError("Wrong issuer.")
    if idinfo['hd'] != APPS_DOMAIN_NAME:
        raise crypt.AppIdentityError("Wrong hosted domain.")
  except crypt.AppIdentityError:
    # Invalid token
  userid = idinfo['sub']