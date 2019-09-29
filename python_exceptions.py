import datetime
def validate_date(date_string):
    date_values = [int(value) for value in date_string.split('-')]
    year, month, date = date_values
    try:
        actual_date = datetime.date(year=year, month=month, day=date)
        return actual_date
    except ValueError as error_message:
        raise ValueError(error_message)
        print("print me")
        
    # except ValueError as error_message:
    #     return error_message

# def convert_to_int(date_string):
#     date_string_list = date_string.split('-')
#     actual_date = []
#     for value in date_string_list:
#         try:
#             actual_date.append(int(value))
#         except ValueError as error_message:
#             return error_message


print(validate_date('2019-02-29'))

