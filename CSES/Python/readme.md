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



# Longest DNA Repetition

You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

## Input
The only input line contains a string of n characters.

## Output
Print one integer: the length of the longest repetition.

## Code

```python
def longest_consecutive_repeat(sequence: str) -> int:
    if not sequence:
        return 0

    max_count = 1
    current_count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1

    return max_count

dna_sequence = input("Enter DNA Sequence: ").strip().upper()
result = longest_consecutive_repeat(dna_sequence)
print(result)
