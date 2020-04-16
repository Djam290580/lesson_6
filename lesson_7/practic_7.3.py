matrix = [[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]]

def printMatrix ( matrix ):
   for row in matrix:
      for x in row:
          print ( "{:4d}".format(x), end = "" )
      print ()

printMatrix(matrix)