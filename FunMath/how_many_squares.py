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
