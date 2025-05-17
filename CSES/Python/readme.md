# Missing Number

You are given a list of numbers from 1 to n, but one number is missing. Your task is to find and print the missing number.

## Input
The input consists of two lines:

- The first line contains an integer n.
- The second line contains n - 1 distinct integers between 1 and n.

## Output
Print the missing number.


## Code

```python
n = int(input("Enter integer count n: "))
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
sum1 = n * (n + 1) // 2  # Sum of numbers from 1 to n
sum2 = sum(numbers)

missingNumber = sum1 - sum2
print(missingNumber)
