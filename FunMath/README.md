# Square Counting Puzzle Solution

This project provides a solution to the problem of counting all possible squares that can be formed using any four points from a given set of 20 points arranged in a cross pattern. This problem was popularized by a puzzle proposed in 1893.

## Problem Description

Given a set of 20 points arranged in a cross, the challenge is to determine how many squares can be drawn using any four of these points as corners.

## Points

The points are as follows:

<img width="1396" height="858" alt="image" src="https://github.com/user-attachments/assets/a0dbab70-0f15-4031-967f-e7037c1b1c67" />


https://youtu.be/61PHoroHhMQ


## Solution

To solve the problem, we need to consider all possible combinations of four points and check if they form a square. The code provided below implements this solution using a brute-force approach to check all combinations and validate the conditions for forming a square.

## Code

```python
import itertools

def is_square(p1, p2, p3, p4):
    def distance_squared(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    
    points = [p1, p2, p3, p4]
    dists = sorted([distance_squared(points[i], points[j]) for i in range(4) for j in range(i+1, 4)])
    
    return dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and 2 * dists[0] == dists[4]

points = [(3, 1), (4, 1), 
          (3, 2), (4, 2),
          (2, 3), (3, 3), (4, 3), (5, 3),
          (1, 3), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (6, 3),
          (3, 5), (4, 5), 
          (3, 6), (4, 6)]

count = 0
for combination in itertools.combinations(points, 4):
    if is_square(*combination):
        count += 1

print("Total number of squares:", count)

```
## Explanation
The process involves:

- Calculating the squared distances between all pairs of four points.
- Sorting these distances and checking if they meet the conditions for forming a square:
  - The four smallest distances should be equal (sides of the square).
  - The two largest distances should be equal and twice the smallest distance (diagonals of the square).

## Historical Context
This puzzle was first proposed in 1893 with an initial answer of 17 squares. Edward Dudeney later refined the answer to 21 squares. This project uses computational power to verify that the correct answer is indeed 21 squares.
