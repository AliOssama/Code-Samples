def shellSort(array):

    h = len(array)
    interval = 4*3+1
    while interval > 0:
  
        for i in range(interval,h):
            temp = array[i]
            j = i
            while  j >= interval and array[j-interval] >temp:
                array[j] = array[j-interval]
                j -= interval
  
            array[j] = temp
        interval= (interval -1) //3
  

array = [ 6,1,4,2,3,5,10,9,11,7,13,15,14]

print ("Before sorting: ", array)  
shellSort(array) 
print ("Array after sorting: ", array)

