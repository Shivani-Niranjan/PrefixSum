def prefixSum(array):
    for i in range(1,len(array)):
        array[i]+=array[i-1]
    return array

array=list(map(int,input().strip().split()))
print(prefixSum(array))