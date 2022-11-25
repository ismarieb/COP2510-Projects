# Driver: Ismarie Birriel
# Navigator: Derrick Jeffers

# Each line in a data file is retrieved and put in a list, where each line
# adds another list of data into a main list with data from each line.

def read_data_table(file):
    lines = []
    with open (file, 'r') as my_file:
        for row in my_file:
            data_row = row.rstrip()
            line = list(data_row.split(' '))
            lines.append(line)
    return lines

print(read_data_table('small_data.txt'))
        
        
