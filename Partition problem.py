'''
Ali Ali, Michael Ramage, Josh West, Minh Vu
Parition Problem

Brute force gave memory errors for long times and small inputs. Results below are for 2 mins with a random list of 10 numbers.

Number of Brute Force Runs : 372997614
Average Brute Force Runtime: 6.879262147555817e-08 (2 minutes)

Number of Greedy Runs : 381365333
Average Greedy Runtime: 6.098838454538701e-08 (2 minutes)

Number of Greedy Runs : MemoryError (15 minutes)
Average Greedy Runtime : MemoryError (15 minutes)

Note: Greedy algorithm is FAR FAR more tolerant of larger sized lists. Easily solved size 50,000 in under a minute.

Time Complexity:
Brute Force: runtime 2^n, but upfront generation of powersets using itertools library utility function combination is O(r (n choose r))https://stackoverflow.com/questions/53419536/what-is-the-computational-complexity-of-itertools-combinations-in-python.
We exclude the generation of powerset from brute force's time complexity because technically we can separate it out and pass it in to the function as an upfront, pre-runtime cost. We did not implement the powerset function or the combinations utility function that it depends on (itertools combinations). 

Greedy: n (this could be 2*n if we sort)
'''
from random import *
from itertools import chain, combinations, permutations
from collections import Counter
import sys
from time import *

def avg(list1):
    mean = sum(list1)/len(list1)
    return mean

#used for benchmarking
def timer(function,runtime):
    times =[]
    start = time()
    while time()-start<runtime:
        end = time()
        function
        times.append(time()-end)
    return len(times),avg(times)
    
#(https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset)
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))

def setdiff(arr, s2):
    arr = Counter(arr)
    s2 = Counter(s2)

    diff = arr - s2
    return list(diff.elements())

def brute(items):
    print("brute forcing...")
    s = []

    best_diff = sys.maxsize  #max integer/infinity; diff can't start at 0
    best_s1 = [] 
    best_s2 = []
    ps = list(powerset(items))

    for sub in ps:
        curr_s1 = list(sub) #current subset is s1
        curr_s2 = setdiff(items, curr_s1) #s2 is the complement of s1
        curr_diff = abs(sum(curr_s2) - sum(curr_s1))
        #print("s1: ",curr_s1,"\ns2: ",curr_s2) #uncomment to see process
        #print("difference: ",curr_diff,"\n") #uncomment to see process
        if curr_diff < best_diff:
            best_s1 = curr_s1 #update best_s1
            best_s2 = curr_s2 #update best_s2
            best_diff = curr_diff #update best_diff

    return best_s1, best_s2, best_diff

#complexity of n
def greedy(arr):
    print("greedy...")

    #sorting adds complexity of n
    #arr = sorted(arr) #allows s1 to have all the least values
    sumOfArray = sum(arr)
    goal = sumOfArray // 2
    tempArr = []
    tempSum = 0
    i = 0
    #while set difference != 0 and not out of bounds
    while abs(tempSum - goal) != 0 and i < len(arr):
        tempArr.append(arr[i])
        tempSum = sum(tempArr)

        if tempSum > goal:
            tempArr.remove(arr[i])

        i += 1
        #print(tempArr) #uncomment to see process
        
    s1 = setdiff(arr,tempArr) #complement of s2
    s2 = tempArr
    diff = abs(sum(s1) - sum(s2))
    #print("s1: ",s1,"\ns2: ",s2) #uncomment to see process
    #print("difference: ",diff) #uncomment to see process
    return s1, s2, diff

def main():
    arr = [1,5,11,5] #answer [11], [1,5,5]
    size = 4 #change this to change size of random list
    randy = [randint(0, 100) for x in range(size)] 

    #benchmarking brute force algo
    #brute_runs, brute_time = timer(brute(randy),900)
    #print("# Brute Runs: ",brute_runs,"Average Brute Time: ",brute_time)

    #benchmarking greedy algo
    #greedy_runs, greedy_time = timer(greedy(randy),900)
    #print("# Greedy Runs: ",greedy_runs,"Average Greedy Time: ",greedy_time)

    print("Solution: ",brute(arr),"\n") #prints brute solution
    print("Solution: ",greedy(arr)) #prints greedy solution

main()
