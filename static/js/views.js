var Page = React.createClass({
	render: function() {
		return <div><Header/><MainView/></div>;
	}
});

var Header = React.createClass({
	render: function() {
		var style = {marginTop: "10%"};
		return <div>
					<div className="row" style={style}>
						<Logo/>
					</div>
					<div className="row">
						<PantryTab/>
						<RecipeTab/>
						<Profile/>
					</div>
				</div>;
	}
});

var PantryTab = React.createClass({
	render: function() {
		return <div className="two columns button">Pantry</div>;
	}
});

var RecipeTab = React.createClass({
	render: function() {
		return <div className="two columns button">Recipe</div>;
	}
});

var Logo = React.createClass({
	render: function() {
		var style = {textAlign: "center"};
		return <div className="twelve columns" style={style}><h1>EPantry</h1></div>;
	}
});

var Profile = React.createClass({
	render: function() {
		var username = document.getElementById("username").value;
		var style = {textAlign: "right"};
		return <div className="eight columns" style={style}>Hi, {username}!</div>;
	}
});

var MainView = React.createClass({
	render: function() {
		return <div>MAIN VIEW</div>;
	}
});

ReactDOM.render(<Page/>, document.getElementById('content'));