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
						<div className="eight columns" style={rightAlignStyle}>Hi, {username}!</div>
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
	}
});

var MainView = React.createClass({
	getInitialState: function() {
		return {mode: "pantry"};
	},
	render: function() {
		return <div>{this.state.mode}</div>;
	}
});

ReactDOM.render(<Page/>, document.getElementById('content'));