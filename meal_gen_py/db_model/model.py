from collections import namedtuple
from meal_gen_py.db_model.input_validation import *
import sqlite3

## Data flow model
## Input: collection of inputs from user. One collection per field, ie. unit_abbreviation would be ('input1', 'input2'), unit_name would be (('name1', ''name2'), ('abbrev_id1', 'abbrev_id2'))
## Zip: inputs are zipped by zip(*inputs), creating rows from each field collection
## Dictionary: zipped rows are collected into a dictionary, with keys defined by the appropriate namedtuple
## Execution: dictionary is executed in a handmade query with .executemany()

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
        return rows
    except sqlite3.IntegrityError:
        print('ERROR: A matching entry already exists!')
    except sqlite3.OperationalError:
        print(f'ERROR: Table {table} does not exist!')


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

## LOGIC FLOW:
## User input is taken for each field of the relevant table. The input is passed into `insert_table()`, where each param is 
## is each possible field. Said parameters are tupled and passed to a dictionary generator

# def collect_input(*inputs):
#     return zip(*inputs)

table_insertion_query_templates = {
                            'unit_abbreviation': 'INSERT INTO unit_abbreviation (abbreviation) VALUES (:abbreviation)',
                            'unit_name': 'INSERT INTO unit_name (name, unit_abbreviation) VALUES (:name, :unit_abbreviation)',
                            'nutrient_name': 'INSERT INTO nutrient_name (name) VALUES (:name)',
                            'nutrient_unit': 'INSERT INTO nutrient_unit (unit_name, nutrient_name) VALUES (:unit_name, :nutrient_name)',
                            'serving_name': 'INSERT INTO serving_name (name) VALUES (:name)',
                            'serving_size': 'INSERT INTO serving_size (size, unit_name, serving_name) VALUES (:size, :unit_name, :serving_name)',
                            'serving_nutrient': 'INSERT INTO serving_nutrient (nutrient_name, quantity, serving_name) VALUES (:nutrient_name, :quantity, :serving_name)',
                            'meal_name': 'INSERT INTO meal_name (name) VALUES (:name)',
                            'meal_composition': 'INSERT INTO meal_composition (meal_name, serving_name, quantity) VALUES (:meal_name, :serving_name, :quantity)',
                            'time_classification': 'INSERT INTO time_classification (classification) VALUES (:classification)',
                            'meal_time': 'INSERT INTO meal_time (meal_name, time_classification) VALUES (:meal_name, :time_classification)'
                            }

def tuplefy_inputs(*inputs):
    tuplify_inputs = lambda i: i if isinstance(i, list) else [i]
    return list(map(tuplify_inputs, inputs))

def insert_into_table(table, conn, *inputs):
    inputs = tuplefy_inputs(*inputs)
    rows = generate_dictionary(table, zip(*inputs))
    execute_query(table_insertion_query_templates.get(table), rows, conn)
    return rows

# Tuples with `0` are placeholder IDs, as IDs are handled by the database and NEVER INSERTED MANUALLY
def generate_dictionary(table, rows):

    def unit_abbreviation(rows):
        return [ UnitAbbreviation(0, *j) for j in rows ]
    def unit_name(rows):
        return [ UnitName(0, j, i) for (j, i) in rows ]
    def nutrient_name(rows):
        return [ NutrientName(0, *j) for j in rows ]
    def nutrient_unit(rows):
        return [ NutrientUnit(j, i) for (j, i) in rows ]
    def serving_name(rows):
        return [ ServingName(0, *j) for j in rows ]
    def serving_size(rows):
        return [ ServingSize(j, i, k) for (j, i, k) in rows ]
    def serving_nutrient(rows):
        return [ ServingNutrient(j, i, k) for (j, i, k) in rows ]
    def meal_name(rows):
        return [ MealName(0, *j) for j in rows ]
    def meal_composition(rows):
        return [ MealComposition(j, i, k) for (j, i, k) in rows ]
    def time_classification(rows):
        return [ TimeClassification(0, *i) for i in rows ]
    def meal_time(rows):
        return [ MealTime(i, j) for (i, j) in rows ]
    
    dictionary_generation_templates = {'unit_abbreviation': unit_abbreviation,
                                       'unit_name': unit_name,
                                       'nutrient_name': nutrient_name,
                                       'nutrient_unit': nutrient_unit,
                                       'serving_name': serving_name,
                                       'serving_size': serving_size,
                                       'serving_nutrient': serving_nutrient,
                                       'meal_name': meal_name,
                                       'meal_composition': meal_composition,
                                       'time_classification': time_classification,
                                       'meal_time': meal_time,
                                       }
    
    rows = [ i._asdict() for i in [ j for j in dictionary_generation_templates[table](rows) ] ]
    return tuple(rows)

UnitAbbreviation = namedtuple('UnitAbbreviation', ['ID', 'abbreviation'])
UnitName = namedtuple('UnitName', ['ID', 'name', 'unit_abbreviation'])
NutrientName = namedtuple('NutrientName', ['ID', 'name'])
NutrientUnit = namedtuple('NutrientUnit', ['unit_name', 'nutrient_name'])
ServingName = namedtuple('ServingName', ['ID', 'name'])
ServingSize = namedtuple('ServingSize', ['size', 'unit_name', 'serving_name'])
ServingNutrient = namedtuple('ServingNutrient', ['nutrient_name', 'quantity', 'serving_name'])
MealName = namedtuple('MealName', ['ID', 'name'])
MealComposition = namedtuple('MealComposition', ['meal_name', 'serving_name'])
TimeClassification = namedtuple('TimeClassification', ['ID', 'classification'])
MealTime = namedtuple('MealTime', ['meal_name', 'time_classification'])


