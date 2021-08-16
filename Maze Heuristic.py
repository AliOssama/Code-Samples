#This program find the shortest path in a maze


#checks if the move is promising
def isPromising(matrix, x, y):
  rows=len(matrix)
  columns=len(matrix[0])
  if 0<=x<rows and 0<=y<columns:
    if matrix[x][y]==0:
      return False
    return True
  return False


#currentDistance keeps track of my path and shortestPath is the max distance until modified once path found
#or returned as the max distance if path was not found
def findPath(matrix, shortestPath, x, y, i, j, currentDistance):
  #if destination found, return the minimum path found
  if i == x and j == y:
    return min(currentDistance, shortestPath)

  # initial modification: once visited, change to 0 
  matrix[i][j] = 0

  # go down
  if isPromising(matrix, i + 1, j):
    shortestPath = findPath(matrix, shortestPath, x, y, i+1, j, currentDistance+1)
  # go up
  if isPromising(matrix, i - 1, j):
    shortestPath = findPath(matrix, shortestPath, x, y, i-1, j, currentDistance+1)
  # go right
  if isPromising(matrix, i, j + 1):
    shortestPath = findPath(matrix, shortestPath, x, y, i, j+1, currentDistance+1)
  # go left
  if isPromising(matrix, i, j - 1):
    shortestPath = findPath(matrix, shortestPath, x, y, i, j-1, currentDistance+1)

  # BackTrack modification: return 0 changed initially back to 1
  matrix[i][j] = 1
  return shortestPath


def main():
  #Using the same matrix in the problem
  matrix = [
          [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
          [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
          [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
          [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
          [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
          [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
  ]

  #print it to start program
  for i in range(len(matrix)):
    print(matrix[i])
  #max distance to stop searching after
  max_distance= 1000

  #take input from 1 to length of matrix (or array inside matrix)+1
  #this means the user does not have to worry about index starting
  #from 0 and can assume it goes from 1 to length
  destX= int(input("Enter x coordinates of destination: "))
  destY=int(input("Enter y coordinates of destination: "))


  #Inputs: matrix, max_distance is the current 1000 and will be changed to the shortest path,
  #destX and destY are input destination coodrinates, first 0 is the current x coordinate, second 0 is the current y coordinate,
  #last 0 is the current distance
  shortestPath = findPath(matrix, max_distance, destX-1, destY-1, 0, 0, 0)

  #max distance means path not found
  if shortestPath != max_distance:
    print("The shortest path from source to destination has length", shortestPath)
  else:
    print("Destination can't be reached from source")

main()
