from flask import *
from extensions import User, Pantry, Stock, Item, loadSession

pantry = Blueprint('pantry', __name__, template_folder='templates')

def get_item_dictionary(item):
	print item.date.date()
	return {
		"quantity": item.amount, 
		"itemName": item.stock_name, 
		"unit": item.unit, 
		"date": item.date.date().isoformat()
	}

@pantry.route('/pantry', methods=['GET', 'POST', 'PUT'])
def pantry_route():
	session.clear()
	session['username'] = 'bob@bob.bob'
	username = session['username']
	dbSession = loadSession()
	userQuery = dbSession.query(User.email).filter(User.email == username).first()
	print userQuery
	if not userQuery:
		abort(403)

	pantryQuery = dbSession.query(Pantry.id).filter(Pantry.user_email == username).first()

	if request.method == 'GET':
		items_list = dbSession.query(Item).all()
		#do sorting later
		output_list = [get_item_dictionary(item) for item in items_list]

		return jsonify({"items": output_list})

	if request.method == 'POST':
		operation = request.get_json()['operation']
		item_amount = request.get_json()['amount']
		item_name = request.get_json()['name']


		if operation == "add":
			item_unit = request.get_json()['unit']
			item_data = Item(item_amount, item_unit, item_name)
			dbSession.add(item_data)

			stock_data = Stock.query.filter_by(name = item_name).first()
			stock_data.amount = stock_data.amount + item_amount
			db.session.commit()

		elif operation == "subtract":
			stock_data = Stock.query.filter_by(name = item_name).first()

			if stock_data.amount < item_amount:
				print('Cannot remove more items than there exist in the pantry')

			item_group_query = Item.query.order_by().all(Item.date)
			item_group_data = item_group_query.filter_by(name = item_name).all()

