# Driver: Ismarie Birriel
# Navigator: Derrick Jeffers

# select_columns function returns a list containing several rows with the
# data that matches that column number in each row.

def select_columns(data, cols):
    data_in_rows = []
    row_data = []
    i = 0
    for row in data:
        row_data= []
        for i in cols:
            row_data.append(row[i])
        data_in_rows.append(row_data)
        i += 1
    return data_in_rows


data = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]
print(select_columns(data, [0,1,3]))
# [[1, 2, 4], [2, 4, 8], [3, 6, 12]]
