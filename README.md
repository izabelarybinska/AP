# AP

## Assignment: Search Challenge

Search.py implements the functions linear_search and binary_search.
These functions both count how many comparisons they make while searching for a target value. 
It tests both algorithms on sorted lists of increasing size while searching for a value which cannot be found in the list.

It prints a table that shows the comparison of the search algorithms.

The results printed when run are:

| Number of elements | Linear Search | Binary Search |
|--------------------|---------------|----------------|
| 10                  | 10            | 3              |
| 100                 | 100           | 6              |
| 1,000               | 1,000         | 9              |
| 10,000              | 10,000        | 13             |
| 100,000             | 100,000       | 16             |

## Comprehension questions

**1. What is the Big O complexity of linear search?**

The complexity is O(n). With linear search the number of comparisons grows at the same exact rate as the list size.
It searches for the value by going through each element.

**2. What is the Big O complexity of binary search?**

The complexity here is O(log n), which means the comparisons grow very slowly in comparison to the list size.
This is because each comparison cuts the remaining search area in half.

**3. Why does binary search require sorted data?**

THe data needs to be sorted because binary search works by looking at the middle item and checking whether the value is greater
or less than the target value. If the data isn't sorted, binary search won't work because it operates under the assumption that
the values in the first half of the list are lower than the target, and the values in the second half are higher.
Thats how it decides which direction to continue the search in.

**4. Which algorithm scales better?**
Binary search scales better. The larger the lists get, the less efficient linear search becomes, as it will always check every list item.
Because the binary search works by comparing the middle number first and eliminating half of the list based on the result, it is able to perform more efficiently with large datasets.