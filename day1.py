# Part One
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

# Part Two

similarity_score = 0

for location_id in left_list:
    if location_id in right_list:
        similarity_score += location_id * right_list.count(location_id)

print(similarity_score)