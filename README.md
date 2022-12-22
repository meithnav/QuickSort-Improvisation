# Improvised QuickSort using Median of 3

### **TIME COMPLEXITY:** O(log n)

### 1) Data in Pre-Sorted Order(descending)
![image](https://user-images.githubusercontent.com/66678522/177980845-05d2330f-051c-4d0c-a8e3-d98e80927416.png)


### 2) Data in Randomised Order
<img width="662" alt="Screenshot 2022-07-08 at 4 24 53 PM" src="https://user-images.githubusercontent.com/66678522/177980909-189d2a64-3491-4b26-bc83-29dd00c62233.png">

## RESULTS TABLE: 

<img width="900" alt="Screenshot 2022-07-08 at 4 25 14 PM" src="https://user-images.githubusercontent.com/66678522/177980961-27e58e81-8f0f-40a8-849e-a4f1b4cc3a35.png">
* <i>All the values are presented in seconds(time)</i>

## CONCLUSION
Hence, median of 3 partitioning methods can be chosen for selecting the pivotal element in the quick sort as it helps to limit the worst-case of the problem. It is evident from the graphs in the previous sections that, Quicksort using Median of 3, gives a time complexity of O(n logn) even in the worst case where as Quicksort using Lumoto or Hoare’s partition runs in O(n2) time in for the worst-case inputs. When the elements are in random order the Quicksort using Hoare’s partition, Lumoto partition and Quicksort using Median of 3 all show a similar behavior giving a time complexity of O(n log n).

Although Haore’s and Medain of 3 have marginal difference in time, Lumoto on the other hand shows quite a long time to perform the task which increases significantly with the number of elements owing to more swaps required by lumoto compared to the other 2 methods. Hence, we have successfully determined that the selection of pivot as median helps us increase the efficiency of the quicksort algorithm.
