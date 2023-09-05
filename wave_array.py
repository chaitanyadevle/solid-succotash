"""
Given a sorted array arr[] of distinct integers. Sort the array into
 a wave-like array and return it.
In other words, arrange the elements into a sequence such that
 arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
URL : https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

length_of_arr = len(a) - 1
for current in range(0, length_of_arr, 2):
    if current + 1 <= length_of_arr:
        a[current], a[current + 1] = a[current + 1], a[current]
print(a)
