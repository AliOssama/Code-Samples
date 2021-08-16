#This program returns the max price can be achieved by cutting the rod


#fill the temp array f and return the last value added indicating the max price
def processing(prices, n):
  #just filling f array with 0 for now
  f = []
  for i in range(n+1):
    f.append(0)
    f[0] = 0
    
  for i in range(1, n+1):
    #maximum value reset to 1
    mval = prices[0]
    for j in range(0,i):
      mval = max(mval, prices[j] + f[i-j-1])
      f[i] = mval
      #print(mval, i, j)
  #return the max price added at the end of the array
  return f[n]


prices = [1, 5, 9, 3, 2]
sizeOfRod = len(prices)
print("max price= " + str(processing(prices, sizeOfRod)))

