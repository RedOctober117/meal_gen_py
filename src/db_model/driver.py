from connection import *
from pathlib import Path
# connection = sqlite3.connect("db\\test.db")
flash_path = Path(Path.cwd(), 'src/sql_scripts/flash_build.sql')
non_flash_path = Path(Path.cwd(), 'src/sql_scripts/no_flash_build.sqlite')

def main():
    db_path = Path(Path.cwd(), 'meal_gen.db')
    database = Connection(db_path)
    database.checked_establish_connection()
    print(database.path())
    match match_query_user('Flash database? (y/N): ', ['y', 'n', None], False):
        case 'Y' | 'y':
            flash_db_build(flash_path, database)
        case _:
            pass
 
    # print(tabularize_table('unit_abbreviation', database))

    # insert_into_table('unit_abbreviation', database, 'tsp')
    # insert_into_table('unit_name', database, ['Teaspoon', 'Cookie'], [6, None])
    # insert_into_table('serving_name', database, 'Golden Oreo')
    # insert_into_table('serving_size', database, 3, 7, 2)
    # insert_into_table('serving_size', database, 34, 2, 2)
    # insert_into_table('serving_nutrient', database, 1, 160, 2)
    # insert_into_table('serving_nutrient', database, 2, 7, 2)
    # insert_into_table('serving_nutrient', database, 3, 2, 2)
    # insert_into_table('serving_nutrient', database, 4, 0, 2)
    # insert_into_table('serving_nutrient', database, 5, 0, 3)
    # insert_into_table('serving_nutrient', database, 6, 120, 3)
    # insert_into_table('serving_nutrient', database, 7, 25, 2)
    # insert_into_table('serving_nutrient', database, 8, 0, 2)
    # insert_into_table('serving_nutrient', database, 9, 12, 2)
    # insert_into_table('serving_nutrient', database, 10, 12, 2)
    # insert_into_table('serving_nutrient', database, 11, 1, 2)
    # insert_into_table('serving_nutrient', database, 12, 0, 4)
    # insert_into_table('serving_nutrient', database, 13, 0, 3)
    # insert_into_table('serving_nutrient', database, 13, 0.8, 3)
    # insert_into_table('serving_nutrient', database, 13, 20, 3)

    test = generate_dictionary('unit_abbreviation', tuplefy_inputs('abc', 'def'))
    print([ i for i in test ])
    # print(tabularize_database(database))
    
    database.connection.close()

def tabularize_database(database):
    tables = ['unit_abbreviation', 'unit_name', 'nutrient_name','nutrient_unit','serving_name','serving_size','serving_nutrient','meal_name','meal_composition', 'time_classification', 'meal_time']
    prebuilt_buffer = [ format(f'{tabularize_result(dump_table(string, database))}\n') for string in tables ]
    buffer = ''
    
    for i in range(len(prebuilt_buffer)):
        buffer += format(f'{tables[i]}:\n') + prebuilt_buffer[i]

    return buffer

    def tabularize_result(rows):
    string = ''
    
    for dict in rows:
        string += format(f'{dict}\n')
    # max_spacing = 0
    # for dict in rows:
    #     for value in dict.values():
    #         value = str(value)
    #         max_spacing = len(value) if len(value) > max_spacing else max_spacing

    # lr_padding = max_spacing // 2

    # for key in rows[0].keys():
    #     string += format(f'| {key:^lr_padding} |')
    # string += '\n'
    # for dict in rows:
    #     for values in dict.values():
    #         string += format(f'| {values} |')
    #     string += '\n'
    return string

def tabularize_table(table, conn):
    buffer = format(f'{table}:\n')
    for row in dump_table(table, conn):
        buffer += format(f'{row}\n')
    return buffer


if __name__ == "__main__":
    main()
