var Page = React.createClass({
	render: function() {
		return <div><Header func={this.setMainViewProp}/><MainView ref="mainView"/></div>;
	},
	setMainViewProp: function(property) {
		this.refs.mainView.setState({mode: property}) //.MainView.setState({selected: property});
	}
});

var Header = React.createClass({
	render: function() {
		var marginTopStyle = {marginTop: "10%"};
		var centerAlignStyle = {textAlign: "center"};
		var rightAlignStyle = {textAlign: "right"};
		var username = document.getElementById("username").value;
		return <div>
					<div className="row" style={marginTopStyle}>
						<div className="twelve columns" style={centerAlignStyle}><h1>EPantry</h1></div>
					</div>
					<div className="row">
						<div className="two columns button" onClick={this.handlePantryClick}>Pantry</div>
						<div className="two columns button" onClick={this.handleRecipeClick}>Recipe</div>
						<div className="six columns" style={rightAlignStyle}>Hi, {username}!</div>
						<div className="two columns button" onClick={this.signOut}>Logout</div>
					</div>
				</div>;
	},
	handlePantryClick: function() {
		console.log("Pantry clicked");
		this.props.func("pantry");
	},
	handleRecipeClick: function() {
		console.log("Recipe clicked");
		this.props.func("recipe");
	},
	signOut: function() {
		ajaxPost("/logout", 
			{}, 
			function(data, textStatus, jqXHR) {
				console.log("Logout successful.");
				location.reload();
			},
			function(jqXHR, textStatus, errorThrown) {
				console.log(errorThrown);
		}
	);
	}
});

var MainView = React.createClass({
	getInitialState: function() {
		return {mode: "pantry"};
	},
	render: function() {
		if (this.state.mode == "pantry") {
			return <PantryView/>
		}
		else if (this.state.mode == "recipe") {
			return <RecipeView/>;
		}
		else {
			return <div>wtf</div>;
		}
	}
});

var PantryView = React.createClass({
	getInitialState: function() {
		return {items: []};
	},
	componentDidMount: function() {
		this.getPantryFromServer();
	},
	getPantryFromServer: function() {
		ajaxGet("/pantry", 
			{},
			function(data, textStatus, jqXHR) {
				this.setState({items: data["items"]});
			}.bind(this),
			function(jqXHR, textStatus, errorThrown) {
				console.log(errorThrown);
			}
		);
	},
	render: function() {
		var lightBlueText = {color: "#add8e6"};
		return <div style={lightBlueText}>
					<p>Here are the items you have in your pantry:</p>
					<PantryItemList data={this.state.items}/>
				</div>;
	}
});

var PantryItemList = React.createClass({
	render: function() {
		var i = 0;
		var items = this.props.data.map(function(item) {
			return <li key={i++}>{item.itemName}: {item.quantity} {item.unit}</li>
		});
		return <ul>{items}</ul>
	}
});

var RecipeView = React.createClass({
	render: function() {
		return <div>hi</div>;
	}
});

ReactDOM.render(<Page/>, document.getElementById('content'));