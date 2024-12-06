left_list = []
right_list = []
distances = []

with open("inputs/day1.txt", "r") as file:
    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

left_list.sort()
right_list.sort()

for left, right in zip(left_list, right_list):
    distances.append(abs(left - right))

print(sum(distances))
