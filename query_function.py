def query_and_print(query, print_query, cursor):
    """
    Params
    - query is a string : SQL query
    - print_query is a string : business question

    Function perform query and prints results

    Returns none
    """
    results = cursor.execute(query).fetchall()
    print(print_query)
    for row in results:
        print(row)
