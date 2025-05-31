class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    zero_row = set()
    zero_col = set()

    for r in range(rows):
      for c in range(cols):
        if matrix[r][c] == 0:
          zero_row.add(r)
          zero_row.add(c)
    for r in range(rows):
      for c in range(cols):
        if r in zero_row:
          matrix[r][c] = 0
    for c in range(cols):
      for r in range(rows):
        if c in zero_col:
          matrix[r][c] = 0
    return matrix
