# Union of Two Sorted Arrays

A Python implementation for finding the union of two sorted arrays while keeping the result sorted and excluding duplicate values.

## Overview

The program processes both arrays simultaneously using two pointers. At each step, the smaller current value is selected. When both values are equal, the value is added only once and both pointers move forward.

A separate check prevents the same value from being added repeatedly to the result.

## How It Works

The `find_union()` method begins with two pointers:

```python
i = 0
j = 0
```

`i` tracks the current position in the first array, while `j` tracks the current position in the second array.

### Comparing the Arrays

While both arrays still contain unprocessed elements, their current values are compared.

If the value in `nums1` is smaller, it becomes the next candidate:

```python
if nums1[i] < nums2[j]:
    current_value = nums1[i]
    i += 1
```

If the value in `nums2` is smaller, the corresponding element from the second array is selected.

When both values are equal, the shared value is selected and both pointers advance.

### Avoiding Duplicates

Before adding a candidate to the result, the program checks whether it is already the most recently inserted value:

```python
if (
    not union_result
    or union_result[-1] != current_value
):
    union_result.append(current_value)
```

Because the input arrays are sorted, checking only the last result element is sufficient to avoid consecutive duplicates.

## Processing Remaining Elements

The main comparison loop stops when one array has been completely processed.

The program then continues through the remaining elements of the first array:

```python
while i < n:
    if not union_result or union_result[-1] != nums1[i]:
        union_result.append(nums1[i])
    i += 1
```

The same process is performed for the remaining elements of the second array.

## Example

Given:

```python
nums1 = [1, 1, 2, 3, 4]
nums2 = [2, 3, 5, 6]
```

The union is:

```text
[1, 2, 3, 4, 5, 6]
```

The program prints:

```text
1 2 3 4 5 6
```

The sample arrays and function call are included in the main section of the program.

## Algorithm

1. Initialize two pointers at the beginning of both arrays.
2. Compare the current elements.
3. Select the smaller value.
4. If both values are equal, select it once and advance both pointers.
5. Add the selected value only if it differs from the last result value.
6. Process any remaining elements from either array.
7. Return the completed union.

## Complexity

Let `N` and `M` represent the lengths of the two input arrays.

| Metric          | Complexity |
| --------------- | ---------- |
| Time            | O(N + M)   |
| Auxiliary Space | O(N + M)   |

The input arrays are traversed once. The result list can contain up to `N + M` elements.

## Key Concept

This problem demonstrates how sorted input can eliminate the need for repeated searching or sorting. Two pointers move forward through the arrays, while the result list handles duplicate suppression.

## Running the Program

Run the file with:

```bash
python "Union of Two Sorted Arrays.py"
```

Expected output:

```text
1 2 3 4 5 6
```
