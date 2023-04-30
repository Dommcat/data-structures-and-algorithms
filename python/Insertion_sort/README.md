# Insertion Sort: A Step-by-Step Guide and Implementation

###  Insertion sort is a simple and efficient sorting algorithm that is commonly used for sorting small datasets or when the input data is partially sorted. In this blog article, we will walk through the Insertion Sort algorithm using the provided pseudocode and a sample input array.We will visually represent the step-by-step output after each iteration. Finally, we will provide a working implementation of the algorithm based on the pseudocode.

### Here is the sample list we will use: [8, 4, 23, 42, 16, 15]

### Pseudocode

    Insert(int[] sorted, int value)
        initialize i to 0
        WHILE value > sorted[i]
          set i to i + 1
        WHILE i < sorted.length
          set temp to sorted[i]
          set sorted[i] to value
          set value to temp
          set i to i + 1
        append value to sorted

      InsertionSort(int[] input)
        LET sorted = New Empty Array
        sorted[0] = input[0]
        FOR i from 1 up to input.length
          Insert(sorted, input[i])
        return sorted

## Now lets take a look at each step to see what the code is doing:


Step 1: Compare 4 with 8 and insert 4 before 8 in the sorted subarray.


[4, 8, 23, 42, 16, 15]
Step 2: Compare 23 with 8 and insert 23 after 8 in the sorted subarray.


[4, 8, 23, 42, 16, 15]
Step 3: Compare 42 with 23 and insert 42 after 23 in the sorted subarray.


[4, 8, 23, 42, 16, 15]
Step 4: Compare 16 with 42 and insert 16 before 42 in the sorted subarray.


[4, 8, 23, 16, 42, 15]
Step 5: Compare 15 with 42 and insert 15 before 42 in the sorted subarray.


[4, 8, 23, 16, 15, 42]
Output list: [4, 8, 15, 16, 23, 42]

Here is a step-by-step explanation of the insert function with a visual output for the list [8, 4, 23, 42] and the new value 16:

Input list: [8, 4, 23, 42]
New value: 16

Step 1: Compare 16 with 8 and 4.


[8, 4, 23, 42]
    ^  ^
    |  |
    |  compare with 8 and 4
    |
    insert 16 here
Step 2: Compare 16 with 23 and insert 16 before 23 in the sorted subarray.


[8, 4, 16, 23, 42]
         ^
         |
         insert 16 here
Output list: [8, 4, 16, 23, 42]




## Working Implementation of Insertion Sort in Python

[Code insertion sort](insertion_sort.py)

## Challenge Title:
Insertion Sort Blog

## Whiteboard
N/A

## Source:
ChatGPT


https://www.scaler.com/topics/insertion-sort-in-python/
