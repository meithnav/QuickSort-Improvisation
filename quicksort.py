import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import os


def makePlot(time_data, order_type):
    df = pd.DataFrame(time_data)
    df.set_index("N", inplace=True)

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["HOARE"], label="HOARE", marker='o')
    plt.plot(df.index, df["LUMOTO"], label="LUMOTO", marker='o')
    plt.plot(df.index, df["MEDIAN"], label="MEDIAN", marker='o')

    plt.title(f"TIME REQUIRED V.S ARRAY SIZE ({order_type.upper()} ORDERED)")
    plt.xlabel("NO. OF ELEMENTS")
    plt.ylabel("TIME ELAPSED (seconds)")
    plt.legend()
    plt.grid()

    
    os.makedirs("plots", exist_ok=True)
    plt.savefig(f"plots/quicksort_{order_type}.png")
    plt.show()



def generateNum(N, order_type="random"):
    arr=[]

    if order_type=="random": # RANDOMLY
        for i in range(N):
            arr.append(random.randint(0, 10000))

    elif order_type=="descending": #DECREASING
        arr = [ele for ele in range(N, 0, -1) ]

    else: #INCREASING
        arr = [ele for ele in range(1, N+1) ]
    
    
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




def quicksort(N=100, order_type="random"):

    arr = generateNum(t, order_type)
    print("\nNO. OF ELEMENTS : ", N)
    HoareTime, LumotoTime, MedianTime = 0, 0, 0
   
    # Make 3 copies
    arr_hoare = arr.copy()
    arr_lumoto = arr.copy()
    arr_median = arr.copy()

    startMedian = time.perf_counter()
    median_arr = medianQuicksort(arr_median, 0, len(arr_median) - 1)
    endMedian = time.perf_counter()
    MedianTime = endMedian - startMedian
    print(f"TIME ELAPSED FOR MEDIAN : {MedianTime:0.9f} seconds")

    startHoare = time.perf_counter()
    hoare_arr = HoareQuicksort(arr_hoare, 0, len(arr_hoare) - 1)
    endHoare = time.perf_counter()
    HoareTime = endHoare - startHoare
    print(f"TIME ELAPSED FOR HOARE : {HoareTime:0.9f} seconds")

    startLumoto = time.perf_counter()
    lumotto_arr = LumotoQuicksort(arr_lumoto, 0, len(arr_lumoto) - 1)
    endLumoto = time.perf_counter()
    LumotoTime = endLumoto - startLumoto
    print(f"TIME ELAPSED FOR LUMOTO : {LumotoTime:0.9f} seconds")


    return HoareTime, LumotoTime, MedianTime





########################
########################

# TYPE="random"
TYPE = "ascending"
# TYPE="descending"

# SIZES = [100, 200, 500, 700, 1000, 1500, 2000, 2500, 3000, 5000, 7000, 10000, 15000, 20000, 25000, 30000, 50000, 70000, 100000, 150000, 200000, 250000, 300000, 500000, 700000, 1000000, 1500000, 2000000, 2500000, 3000000, 5000000]

SIZES = [100, 200, 500, 700]

time_data = {"N": [], "HOARE": [], "LUMOTO": [], "MEDIAN": []}

for t in SIZES:
    
    HoareTime, LumotoTime, MedianTime = quicksort(t, order_type=TYPE)

    time_data["N"].append(t)
    time_data["HOARE"].append(HoareTime)
    time_data["LUMOTO"].append(LumotoTime)
    time_data["MEDIAN"].append(MedianTime)

# print("\n\n", time_data)
makePlot(time_data, order_type=TYPE)



