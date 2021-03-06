import time
import random


def generateNum(N):
    arr=[]

    # RANDOMLY
    for i in range(N):
        arr.append(random.randint(0, 10000))

   
    # DECREASING
    # arr = [ele for ele in range(N, 0, -1) ]

    return arr


def swap(A, i, j):
    A[i] , A[j] = A[j], A[i]


def randomiseArr(arr):

    # METHOD 1:
    # random.shuffle(arr)

    # METHOD 2:
    for i in range(len(arr)-1 , 0 , -1):
        j = random.randint(0, i-1) 
        swap(arr , i,j)

    # print("AFTER SHUFFLE : ", arr)
    return arr


def HoarePartition(array, low, high) -> int:
    pivot = array[low]
    (i, j) = (low - 1, high + 1)
 
    while True:
 
        while True:
            i = i + 1
            if array[i] >= pivot:
                break
 
        while True:
            j = j - 1
            if array[j] <= pivot:
                break
 
        if i >= j:
            return j
 
        swap(array, i, j)


def HoareQuicksort(array, low, high):
    if low < high:
        pivot = HoarePartition(array, low, high)
        HoareQuicksort(array, low, pivot)
        HoareQuicksort(array, pivot + 1, high)
    return array


def Lumotopartition(array, lo, hi):
    pivot = array[hi]

    i = lo - 1
    for j in range(lo, hi):
        if array[j] < pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i + 1]
    array[i + 1] = array[hi]
    array[hi] = temp
    return i + 1


def LumotoQuicksort(array, lo, hi):
    if lo < hi:
        p = Lumotopartition(array, lo, hi)
        LumotoQuicksort(array, lo, p - 1)
        LumotoQuicksort(array, p + 1, hi)
    return array



def medianThreePartition(array, low , high) -> int:
    if high-low+1>2:
        index = random.randint(low+1, high-1)
    else:
        return low

    # MEDIAN INDEX
    if array[low]>=array[high] and array[low]>=array[index]:
        if array[index]>array[high]:
            return high
        else:
            return index
    
    elif array[index]>=array[high] and array[index]>=array[low]:
        if array[low]>array[high]:
            return high
        else:
            return low

    elif array[high]>=array[index] and array[high]>=array[low]:
        if array[index]>array[high]:
            return low
        else:
            return index
    

def medianQuicksort(array, lo, hi):
    if lo < hi:
        p = medianThreePartition(array, lo, hi)
        medianQuicksort(array, lo, p - 1)
        medianQuicksort(array, p + 1, hi)
    return array




def quicksort():

    N = 200
    arr = generateNum(N)
    # arr = list(map(int, input("ENTER THE LIST OF NUMBERS : ").split() ))

    # RANDOMISE
    # arr = randomiseArr(arr)


    print("\nNO. OF ELEMENTS : ", len(arr))
   
    startHoare = time.perf_counter()
    hoare_arr = HoareQuicksort(arr, 0, len(arr) - 1)
    endHoare = time.perf_counter()
    # print("SORTED ARRAY USING HOARE : {s} ".format( s= " ".join( str(ele) for ele in  HoareQuicksort(arr, 0, len(arr) - 1))))
    print(f"TIME ELAPSED FOR HOARE : {endHoare - startHoare:0.9f} seconds")


    startLumoto = time.perf_counter()
    lumotto_arr  =LumotoQuicksort(arr, 0, len(arr) - 1)
    endLumoto = time.perf_counter()
    # print("SORTED ARRAY USING LUMOTO : {s} ".format( s= " ".join( str(ele) for ele in  LumotoQuicksort(arr, 0, len(arr) - 1))))
    print(f"TIME ELAPSED FOR LUMOTO : {endLumoto - startLumoto:0.9f} seconds")


    startMedian = time.perf_counter()
    median_arr = medianQuicksort(arr, 0, len(arr) - 1)
    endMedian = time.perf_counter()
    # print("SORTED ARRAY USING MEDIAN : {s} ".format( s= " ".join( str(ele) for ele in  medianQuicksort(arr, 0, len(arr) - 1))))
    print(f"TIME ELAPSED FOR Median : {endMedian - startMedian:0.9f} seconds")
         

quicksort()
