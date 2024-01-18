# 1. create k buckets
# 2. put elements into respective buckets and sort them
# 3. concatencate buckets

def bucketSort(arr,k):
    rs = max(arr)+1
    bkt = [[] for i  in range(k)]
    for x in arr:
        i = (k*x)//rs     # classify elements into bucket
        bkt[i].append(x)

    for  i in range(k):
        bkt[i].sort()        #insertion sort works well for smaller arrays
    
    idx = 0
    for i in range(k):
        for j in range(len(bkt[i])):
            arr[idx] = bkt[i][j]
            idx+=1
# TC 
# best case:  k ~ n(uniformaly distributed) -O(n)
 
#  worst case :
#  all element go in one bucket : O(n2) - insertion sort ; O(nlogn) - any nlogn sorting algorithm

