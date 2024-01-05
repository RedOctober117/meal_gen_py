from collections import namedtuple
from input_validation import *
import sqlite3

def class_factory(cursor, row):
    pass

def namedtuple_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    cls = namedtuple("Row", fields)
    return cls._make(row)

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

# UTILITY FUNCTIONS

def dump_table(table, conn):
    try:
        conn = conn.connection
        with conn:
            rows = conn.execute(f'SELECT * FROM {table}').fetchall()
    except sqlite3.IntegrityError:
        print('ERROR: A matching entry already exists!')
    except sqlite3.OperationalError:
        print(f'ERROR: Table {table} does not exist!')

    return rows

def confirm_commit(rows):
    match match_query_user(f'{rows}\nWould you like to commit these changes? (y/N): ', ['y', 'n', None], False):
        case 'y' | 'Y':
            return True
        case _: 
            print('\nChanges were discarded.')
            return False

def execute_query(query, rows, conn):
    try:
        conn = conn.connection
        with conn:
            if confirm_commit(rows):
                conn.executemany(query, rows)
    except sqlite3.IntegrityError:
        print('ERROR: A matching entry already exists!')
    except sqlite3.OperationalError:
        print(f'ERROR: One or more syntax errors exist at \'{query}\'')

def generate_dictionary(row_tuples): 
    rows = [ i._asdict() for i in [ j for j in row_tuples ] ]
    return tuple(rows)

# unit_abbreviation
def insert_unit_abbreviation(rows, conn):
    execute_query('INSERT INTO unit_abbreviation (abbreviation) VALUES (:abbreviation)', rows, conn)

def insert_unit_name(rows, conn):
    execute_query('INSERT INTO unit_name (name) VALUES (:name)', rows, conn)

def insert_nutrient_name(rows, conn):
    execute_query('INSERT INTO nutrient_name (name) VALUES (:name)', rows, conn)

def insert_nutrient_unit(rows, conn):
    execute_query('INSERT INTO nutrient_unit (unit_name, nutrient_name) VALUES (:unit_name, :nutrient_name)', rows, conn)

def insert_serving_name(rows, conn):
    execute_query('INSERT INTO serving_name (name) VALUES (:name)', rows, conn)

def insert_serving_size(rows, conn):
    execute_query('INSERT INTO serving_size (size, unit_name, serving_name) VALUES (:size, :unit_name, :serving_name)', rows, conn)

def insert_serving_nutrient(rows, conn):
    execute_query('INSERT INTO serving_nutrient (nutrient_name, quantity, serving_name) VALUES (:nutrient_name, :quantity, :serving_name)', rows, conn)

def insert_meal_name(rows, conn):
    execute_query('INSERT INTO meal_name (name) VALUES (:name)', rows, conn)

def insert_meal_composition(rows, conn):
    execute_query('INSERT INTO meal_composition (meal_name, serving_name) VALUES (:meal_name, :serving_name)', rows, conn)

def insert_meal_breakfast(rows, conn):
    execute_query('INSERT INTO meal_breakfast (meal_name) VALUES (:meal_name)', rows, conn)

def insert_meal_lunch(rows, conn):
    execute_query('INSERT INTO meal_lunch (meal_name) VALUES (:meal_name)', rows, conn)

def insert_meal_dinner(rows, conn):
    execute_query('INSERT INTO meal_dinner (meal_name) VALUES (:meal_name)', rows, conn)

def insert_meal_week_history(rows, conn):
    execute_query('INSERT INTO meal_week_history (meal_name) VALUES (:meal_name)', rows, conn)



def generate_unit_abbreviation(rows):
    return generate_dictionary([ UnitAbbreviation(0, j) for j in rows ])



UnitAbbreviation = namedtuple('UnitAbbreviation', ['ID', 'abbreviation'])
UnitName = namedtuple('UnitName', ['ID', 'name', 'unit_abbreviation'])
NutrientName = namedtuple('NutrientName', ['ID', 'name'])
NutrientUnit = namedtuple('NutrientUnit', ['unit_name', 'nutrient_name'])
ServingName = namedtuple('ServingName', ['ID', 'name'])
ServingSize = namedtuple('ServingSize', ['size', 'unit_name', 'serving_name'])
ServingNutrient = namedtuple('ServingNutrient', ['nutrient_name', 'quantity', 'serving_name'])
MealName = namedtuple('MealName', ['ID', 'name'])
MealComposition = namedtuple('MealComposition', ['meal_name', 'serving_name'])
MealBreakfast = namedtuple('MealBreakfast', ['meal_name'])
MealLunch = namedtuple('MealLunch', ['meal_name'])
MealDinner = namedtuple('MealDinner', ['meal_name'])
MealWeekHistory = namedtuple('MealWeekHistory', ['meal_name'])

