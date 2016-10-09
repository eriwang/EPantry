from flask import *
from extensions import User, Pantry, Stock, Item, loadSession

pantry = Blueprint('pantry', __name__, template_folder='templates')

@pantry.route('/pantry', methods=['GET', 'POST', 'PUT'])
def pantry_route():
	logged_user = session['username']
	log_in_data = User.query.filter_by(User=logged_user).first()
	pantry_data = Pantry.query.filter_by(pantry_id=log_in_data.pantry_id).first()
	session = loadSession()

	if request.method == 'GET':
		items_list = session.query(Item).all()
		#do sorting later
		output_list = []
		for item in items_list:
			item_data = {"quantity": item.amount,"itemName":item.stock_name, "unit": unit, "date":item.date.date().isocalendar()}
			output_list.append(item_data)

		return jsonify({"items":output_list})

	if request.method == 'POST':
		operation = request.get_json()['operation']
		item_amount = request.get_json()['amount']
		item_name = request.get_json()['name']


		if operation == "add":
			item_unit = request.get_json()['unit']
			item_data = Item(item_amount, item_unit, item_name)
			session.add(item_data)

			stock_data = Stock.query.filter_by(name = item_name).first()
			stock_data.amount = stock_data.amount + item_amount
			db.session.commit()

		elif operation == "subtract":
			stock_data = Stock.query.filter_by(name = item_name).first()

			if stock_data.amount < item_amount:
				print('Cannot remove more items than there exist in the pantry')

			item_group_query = Item.query.order_by().all(Item.date)
			item_group_data = item_group_query.filter_by(name = item_name).all()

