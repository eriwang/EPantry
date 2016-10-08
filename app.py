from flask import Flask, render_template
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Register the controllers
# app.register_blueprint(controllers.album)
# app.register_blueprint(controllers.albums)
# app.register_blueprint(controllers.pic)
# app.register_blueprint(controllers.main)
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.login)
#app.register_blueprint(controllers.logout)
app.register_blueprint(controllers.pantry)




# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host="0.0.0.0", port=3000, debug=True)
