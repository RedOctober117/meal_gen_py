import re

def query_user(message: str):
    while True:
        user_input = input(message)
        if user_input == '':
            return (None, message)
        elif user_input > '':
            return (user_input, message)
        else:
            print('No input detected.')

# def verify_parsable(tuple_of_input_and_message):
#     (passed_user_input, message) = tuple_of_input_and_message
#     while True:
#         if passed_user_input.lstrip('-').replace('.', '').isdigit():
#             return float(passed_user_input)
#         else:
#             (passed_user_input, _) = query_user(message)

# def match_query_user(message: str, valid_inputs: [], case_sensitive: bool):
#     if case_sensitive:
#         while True:
#             (user_input, _) = query_user(message)
#             if user_input in valid_inputs:
#                 return user_input
#             else:
#                 print('Invalid token.\n')
#     else:
#         while True:
#             (user_input, _) = query_user(message)
#             # [ return_value in ITERATOR SUBITERATOR ]
#             # Its just a nested for loop bro, dont get confused
#             valid_list = [i for sublist in [ list((y.lower(), y.upper())) for y in valid_inputs if y != None ] for i in sublist]
#             print(valid_list)
#             for s in valid_inputs:
#                 if s not in valid_list:
#                     valid_list.append(s)
#             if user_input in valid_list:
#                 return user_input
#             else:
#                 print('Invalid token.\n')
def match_query_user(message: str, valid_inputs: [], case_sensitive: bool):

    if case_sensitive:
        validation_list = valid_inputs
    else:
        validation_list = [ i for sublist in [ list((s.lower(), s.upper())) for s in valid_inputs if s != None ] for i in sublist ]
        validation_list.append(None) if None in valid_inputs else validation_list
    
    (user_input,_) = query_user(message)
    while user_input not in validation_list:
        print('Invalid token.\n')
        (user_input,_) = query_user(message)

    return user_input