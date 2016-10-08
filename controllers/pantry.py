from flask import *
import pymongo
from extensions import User, Pantry, Stock, Item, Ingredients

pantry = Blueprint('pantry', __name__, template_folder='templates')

@pantry.route('/pantry', methods=['GET', 'POST', 'PUT'])
def pantry_route():
	logged_user = session['username']
	log_in_data = User.query.filter_by(User=logged_user).first()
	pantry_data = Pantry.query.filter_by(pantry_id=log_in_data.pantry_id).first()

	if request.get_json()['METHOD'] == "GET":
		items_list = Stock.query.filter_by(item_id = pantry_data.item_id).all()
        #posts = db.posts

	if request.get_json()['METHOD'] == 'POST':
		item_amount = request.get_json()['amount']
		item_name = request.get_json()['name']
		item_data = Item(item_name, item_amount)
		db.session.add(item_data)
		db.commit()
		stock_data = Stock.query.filter_by(item_id = item_name).first()
		stock_data.amount = stock_data.amount + item_amount
