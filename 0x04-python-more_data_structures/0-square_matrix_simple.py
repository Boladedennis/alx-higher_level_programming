def square_values(matrix):
  squared_matrix = []
  for row in matrix:
    new_row = []
    for elem in row:
      new_row.append(elem**2)
    squared_matrix.append(new_row)
  return squared_matrix
