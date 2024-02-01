-- This script creates the meal_gen database. It should include all the relevant data. 
-- There are two types of table: source and composition. Source tables maintain a ID and primary key. Composition tables maintain may contain a ID, primary key, and 1..* foreign keys

DROP TABLE IF EXISTS meal_time;
DROP TABLE IF EXISTS time_classification;
DROP TABLE IF EXISTS meal_composition;
DROP TABLE IF EXISTS meal_name;
DROP TABLE IF EXISTS serving_nutrient;
DROP TABLE IF EXISTS serving_size;
DROP TABLE IF EXISTS serving_name;
DROP TABLE IF EXISTS nutrient_unit;
DROP TABLE IF EXISTS nutrient_name;
DROP TABLE IF EXISTS unit_name;
DROP TABLE IF EXISTS unit_abbreviation;

-- Source table
CREATE TABLE unit_abbreviation (
  ID INTEGER PRIMARY KEY,
  abbreviation VARCHAR(10) UNIQUE
);

-- Composition table
CREATE TABLE unit_name (
  ID INTEGER PRIMARY KEY,
  name VARCHAR(50),
  unit_abbreviation INTEGER,
  FOREIGN KEY (unit_abbreviation) REFERENCES unit_abbreviation(ID)
);

-- Source table
CREATE TABLE nutrient_name (
  ID INTEGER PRIMARY KEY,
  name VARCHAR(50)
);

-- Composite table
CREATE TABLE nutrient_unit (
  unit_name INTEGER NOT NULL,
  nutrient_name INTEGER NOT NULL,
  FOREIGN KEY (unit_name) REFERENCES unit_name(ID),
  FOREIGN KEY (nutrient_name) REFERENCES nutrient_name(ID)
);

-- Source table
CREATE TABLE serving_name (
  ID INTEGER PRIMARY KEY,
  name VARCHAR(50) 
);

-- Composite table
CREATE TABLE serving_size (
  size DECIMAL(5,2) NOT NULL,
  unit_name INTEGER NOT NULL,
  serving_name INTEGER NOT NULL,
  FOREIGN KEY (serving_name) REFERENCES serving_name(ID),
  FOREIGN KEY (unit_name) REFERENCES unit_name(ID)
);

-- Composite table
CREATE TABLE serving_nutrient (
  nutrient_name INTEGER NOT NULL,
  quantity DECIMAL(5,2) NOT NULL,
  serving_name INTEGER NOT NULL,
  FOREIGN KEY (nutrient_name) REFERENCES nutrient_name(ID),
  FOREIGN KEY (serving_name) REFERENCES serving_name(ID)
);

-- Source table
CREATE TABLE meal_name (
  ID INTEGER PRIMARY KEY,
  name VARCHAR(5,2)
);

-- Composite table
CREATE TABLE meal_composition (
  meal_name INTEGER NOT NULL,
  serving_name INTEGER NOT NULL,
  quantity DECIMAL(5,2) DEFAULT 1,
  FOREIGN KEY (meal_name) REFERENCES meal_name(ID),
  FOREIGN KEY (serving_name) REFERENCES serving_name(ID)
);

-- Composite table
CREATE TABLE time_classification (
  ID INTEGER PRIMARY KEY,
  classification VARCHAR(50)
);

CREATE TABLE meal_time (
  meal_name INTEGER NOT NULL,
  time_classification NOT NULL,
  FOREIGN KEY (meal_name) REFERENCES meal_name(ID),
  FOREIGN KEY (time_classification) REFERENCES time_classification(ID)
);

/*
==============================================
HERE BEGINS THE INSERTION QUERY SECTION
==============================================
*/

INSERT INTO unit_abbreviation (abbreviation) VALUES
  ('kcal'),
  ('g'),
  ('mg'),
  ('mcg'),
  ('Tbsp');

INSERT INTO unit_name (name, unit_abbreviation) VALUES
  ('Kilocalorie', 1),
  ('Gram', 2),
  ('Milligram', 3),
  ('Microgram', 4),
  ('Tablespoon', 5);
  
INSERT INTO nutrient_name (name) VALUES
  ('Calories'),
  ('Total Fat'),
  ('Saturated Fat'),
  ('Trans Fat'),
  ('Cholesterol'),
  ('Sodium'),
  ('Total Carbohydrates'),
  ('Dietary Fiber'),
  ('Total Sugars'),
  ('Added Sugars'),
  ('Protein'),
  ('Vitamin D'),
  ('Calcium'),
  ('Iron'),
  ('Potassium');

INSERT INTO nutrient_unit (unit_name, nutrient_name) VALUES
  (1, 1),
  (2, 2),
  (2, 3),
  (2, 4),
  (3, 5),
  (3, 6),
  (2, 7),
  (2, 8),
  (2, 9),
  (2, 10),
  (2, 11),
  (3, 12),
  (3, 13),
  (3, 14),
  (3, 15);

INSERT INTO serving_name (name) VALUES
  ('Sweet Cream Butter Salted');

INSERT INTO serving_size (size, unit_name, serving_name) VALUES
  (1, 5, 1);

INSERT INTO serving_nutrient (nutrient_name, quantity, serving_name) VALUES 
  (1, 100, 1);

INSERT INTO meal_name (name) VALUES
  ('Grilled Cheese');

INSERT INTO meal_composition (meal_name, serving_name, quantity) VALUES
  -- inserted Sweet Cream Butter Salted twice for two servings of it
  (1, 1, 2);


-- INSERT INTO servings (serving_name, serving_size, serving_unit, serving_cal, serving_fat_tot, serving_fat_sat, serving_fat_trans, serving_chol, serving_sod, serving_carb_tot, serving_fiber_diet, serving_sugar_tot, serving_sugar_add, serving_prot, serving_vit_d, serving_calcium, serving_iron, serving_potas) VALUES
--   ('Sweet Cream Butter Salted', 1, 'Tbsp', 100, 11, 7, 0, 30, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0),
--   ('Nature''s Own White Bread', 1, 'Slice', 60, 1, 0, 0, 0, 90, 12, 0, 2, 2, 2, 0, 50, 1, 0),
--   ('Cheese', 1, 'Slice', 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100);