#This program shows the efficiancy of a heuristic development 
#This function inputs an array of coins values and the length of that array
def coinValue(coinsV, n):
    #initially comparing the far left and right coins
    num1=coinsV[0]
    num2=coinsV[n-1]
    #this will be our max profit
    maxValue=0

    #i is the year and will be the index as well
    for i in range(1, n+1):
        maxValue += min(num1*i, num2*i)
        if num1 < num2:
            num1=coinsV[i]
        elif num2 < num1:
            num2=coinsV[n-1-i]
    return maxValue


#Example of use
coins=[1,2,3,4]
n=len(coins)
print(coinValue(coins, n))
