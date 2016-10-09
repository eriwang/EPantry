use EPANTRY

DROP TABLE IF EXISTS recipe_requirement, possible_recipe, item, recipe, stock, pantry, user;

CREATE TABLE user (
  email varchar(256) NOT NULL,
	PRIMARY KEY(email)
	);

CREATE TABLE pantry (
	id int NOT NULL AUTO_INCREMENT,
	user_email varchar(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(user_email) REFERENCES user(email) ON DELETE CASCADE
  );

CREATE TABLE stock (
  name varchar(56) NOT NULL,
	amount int NOT NULL,
	unit varchar(56),
	pantry_id int NOT NULL,
	PRIMARY KEY(name),
	FOREIGN KEY(pantry_id) REFERENCES pantry(id) ON DELETE CASCADE
	);

CREATE TABLE item (
	amount int NOT NULL,
	unit varchar(56) NOT NULL,
	id int NOT NULL AUTO_INCREMENT,
	date timestamp NOT NULL DEFAULT NOW(),
	stock_name varchar(56),
	PRIMARY KEY(id),
	FOREIGN KEY(stock_name) REFERENCES stock(name) ON DELETE CASCADE
	);

CREATE TABLE recipe (
	name varchar(56) NOT NULL,
	user_email varchar(256) NOT NULL,
	recipe_instruct varchar(8000) NOT NULL,
	PRIMARY KEY(name),
	FOREIGN KEY (user_email) REFERENCES user(email) ON DELETE CASCADE
);

CREATE TABLE possible_recipe (
  id int NOT NULL AUTO_INCREMENT,
  stock_name varchar(56) NOT NULL,
  recipe_name varchar(56) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(stock_name) REFERENCES stock(name) ON DELETE CASCADE,
  FOREIGN KEY(recipe_name) REFERENCES recipe(name) ON DELETE CASCADE
);

CREATE TABLE recipe_requirement (
  id int NOT NULL AUTO_INCREMENT,
  quantity int NOT NULL,
  unit varchar(56),
  stock_name varchar(56) NOT NULL,
  recipe_name varchar(56) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY (stock_name) REFERENCES stock(name) ON DELETE CASCADE,
  FOREIGN KEY (recipe_name) REFERENCES recipe(name) ON DELETE CASCADE
);