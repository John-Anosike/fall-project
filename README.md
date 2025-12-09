# MergeSort Algorithm
<img width="1868" height="844" alt="Screenshot 2025-12-09 120416" src="https://github.com/user-attachments/assets/25d3749b-da75-48bd-9478-b199cb7905c3" />

## Problem Breakdown
- **Decomposition:** The mergesort algorithm can be broken down into two main parts: the merge and the sort. Sorting compares the numbers within two lists and organizes them from least to greatest into a third list, while merging simply takes two of these sorted lists and merges them together.
- **Pattern Recognition:** Merging two lists is pretty straightforward; sorting, on the other hand, takes a bit of explanation. Two pointers are used to navigate through the two lists and compare numbers, and if one number is greater than the other, it gets added to the list first. Then any leftovers are added to the list.
- **Abstraction:** The user should be able to see their list before and after the mergesort, as well as each step where the sorted lists are merged together (as per project requirements). They shouldn't be able to see the finer details like each step in sorting a list, since that would be too much for them to have to read.
- **Algorithm Design:** The user will be able to input a list length and then create a randomized list using said length. Then, they'll be given the option to sort that list. Finally, they'll be able to walk themselves through the steps that it took to merge each sorted partition until the sorted list was produced.

## How to Run
1. Enter a positive integer between 0 and 100,000 for your list length
2. Press "Create List" to create a randomized list utilizing that list length
3. Press "Sort List" to sort the list
4. Adjust the slider below to choose a step to view, then press "View Step" to view the step
