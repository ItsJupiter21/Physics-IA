def filter_rows_by_first_column(input_file, output_file):
    """Filters rows from an input file where the first column is 1.0 and writes them to an output file.

    Args:
        input_file: The path to the input file.
        output_file: The path to the output file.
    """

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            row = line.strip().split(',')
            if row[0] == '1.0':
                f_out.write(line)

# Example usage:
for i in range(0,10,1):
    input_file = 'on'+str(i)+'.csv'  # Replace with your actual input file path
    output_file = 'of'+str(i)+'.txt'  # Replace with your desired output file path

    filter_rows_by_first_column(input_file, output_file)
