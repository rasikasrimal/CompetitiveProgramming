def min_time_to_open_cage(l, p, q, s):
    # Create a dictionary to store the last index of each character in the codeword
    last_index = {}
    time = 0

    # Iterate through the codeword from right to left
    for i in range(l - 1, -1, -1):
        char = s[i]

        # Check if the character is already in the last_index dictionary
        if char in last_index:
            # Calculate the time needed to duplicate the substring from the last index to the current index
            duplicate_time = (last_index[char] - i) * q
            time += duplicate_time

            # Update the last index of the character to the current index
            last_index[char] = i
        else:
            # Calculate the time needed to add the character to the codeword
            time += p

            # Add the character to the last_index dictionary with the current index
            last_index[char] = i

    return time

# Input
T = int(input())
results = []

for _ in range(T):
    L, P, Q = map(int, input().split())
    S = input().strip()
    time = min_time_to_open_cage(L, P, Q, S)
    results.append(time)

# Output
for result in results:
    print(result)
