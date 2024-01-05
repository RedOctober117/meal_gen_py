from connection import *
# connection = sqlite3.connect("db\\test.db")
flash_path = '..\\sql_scripts\\flash_build.sql'
non_flash_path = '..\\sql_scripts\\no_flash_build.sqlite'

def main():
    db_path = '..\\db\\test.db'
    database = Connection(db_path)
    database.checked_establish_connection()
    print(database.path())
    match match_query_user('Flash table? (y/N): ', ['y', 'n', None], False):
        case 'Y' | 'y':
            flash_db_build(flash_path, database)
        case _:
            pass
 
    # print(tabularize_database(database))
    print(tabularize_table('unit_abbreviation', database))
    insert_unit_abbreviation(generate_unit_abbreviation(['abc', 'def']), database)
    
    database.connection.close()

def tabularize_database(database):
    tables = ['unit_abbreviation', 'unit_name', 'nutrient_name','nutrient_unit','serving_name','serving_size','serving_nutrient','meal_name','meal_composition','meal_breakfast','meal_lunch', 'meal_dinner', 'meal_week_history']
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
