
# list
input_list = [8, 4, 23, 42, 16, 15]

def insertion_sort(input_list):
  for i in range(1, len(input_list)):#starts for loop that iterates over the indices of the input list, starting from index 1
    value = input_list [i]
    j = i -1
    while j >= 0 and value < input_list[j]:
        input_list [j + 1] = input_list[j]
        j -=1
        input_list[j +1] = value
  return input_list

# Big O - The time complexity of the insertion sort algorithm is O(n^2) in the worst case, where n is the length of the input list.

# The insertion_sort function and the insert function serve different purposes, and can be used together to implement a complete sorting algorithm. Here's why we need both functions:

#
def insert(sorted_list, value):
    i = 0
    while value > sorted_list[i]:
        i += 1
        if i == len(sorted_list):
            break
        sorted_list.insert(i, value)


# Call the insertion_sort function with the test array as an argument
sorted_list = insertion_sort(input_list)

# Print the sorted array
print(sorted_list)



