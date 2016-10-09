use EPANTRY

INSERT INTO user (email) VALUES ("bob@bob.bob");
INSERT INTO pantry(user_email) VALUES ("bob@bob.bob");
INSERT INTO stock (name, amount, unit, pantry_id) VALUES ("apples", "1", NULL, "1");
INSERT INTO item (amount, unit, stock_name) VALUES ("1", "", "apples");
INSERT INTO recipe (name, user_email, recipe_instruct) VALUES ("Apples_Recipes", "bob@bob.bob", "Take 1 apple and your done");
INSERT INTO possible_recipe(stock_name, recipe_name) VALUES ("apples", "Apples_Recipes");
INSERT INTO recipe_requirement(quantity, unit, stock_name, recipe_name) VALUES ("1", NULL, "apples", "Apples_Recipes");