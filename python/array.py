import numpy


def arrays(arr):
    originalArr=numpy.array(arr,float)
    reverseArr=originalArr[::-1]
    return reverseArr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

