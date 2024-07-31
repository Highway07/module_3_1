calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    a = len(string)
    b = str.upper(string)
    c = str.lower(string)
    return(a, b, c)


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
print(string_info('Capybara'))
print(string_info('Armaggedon'))
print(is_contains('Urban',['ban','BaNaN','urBAN']))# Urban ~ urBAN
print(is_contains('cycle',['recycling','cyclic']))# NO matches
print(calls)





    











