import sys

if len(sys.argv) != 3:
    print("Usage: python script.py input_file output_file")
    sys.exit(1)

input_name = sys.argv[1]
output_name = sys.argv[2]

matrix = []

with open(input_name, 'r') as infile:
    for line in infile:
        row = line.strip().split('\t')
        matrix.append(row)

maxRows = max(len(row) for row in matrix)
maxCols = len(matrix)

transposed_matrix = [[matrix[rowNr][colNr] if colNr < len(matrix[rowNr]) else '' for rowNr in range(maxCols)] for colNr in range(maxRows)]

with open(output_name, 'w') as outfile:
    for rowNr in range(maxRows):
        for colNr in range(maxCols):
            outfile.write(transposed_matrix[rowNr][colNr])
            if colNr < maxCols - 1:
                outfile.write('\t')
            else:
                outfile.write('\n')
