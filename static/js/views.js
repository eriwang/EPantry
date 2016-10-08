var Page = React.createClass({
	render: function() {
		return <div><Header/><MainView/></div>;
	}
});

var Header = React.createClass({
	render: function() {
		return <div><PantryDropdown/><RecipeDropdown/><Logo/><Profile/></div>;
	}
});

var PantryDropdown = React.createClass({
	render: function() {
		return <div>Pantry</div>;
	}
});

var RecipeDropdown = React.createClass({
	render: function() {
		return <div>Recipe</div>;
	}
});

var Logo = React.createClass({
	render: function() {
		return <div>EPantry</div>;
	}
});

var Profile = React.createClass({
	render: function() {
		var username = document.getElementById("username").value;
		return <div>Hi, {username}!</div>;
	}
});

var MainView = React.createClass({
	render: function() {
		return <div>MAIN VIEW</div>;
	}
});

ReactDOM.render(
	<Page/>,
	document.getElementById('content')
);