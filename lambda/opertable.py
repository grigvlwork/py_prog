def print_operation_table(operation, num_rows=9, num_columns=9):
    table = [[str(operation(i, j)) for j in range(1, num_columns + 1)]
             for i in range(1, num_rows + 1)]
    for row in table:
        print('\t'.join(row))
