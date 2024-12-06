input_path = "inputs/day3.txt"
sum = 0

def is_valid(instruction):
    instruction = instruction[4:-1]
    try:
        num1, num2 = instruction.split(",")
        if num1.isdigit() and num2.isdigit():
            return True
    except Exception:
        return False

def get_instructions(line):
    positions = []
    instructions = []
    start = 0
    while (start_index := line.find("mul(", start)) != -1:
        close_index = line.find(")", start_index)
        positions.append((start_index, close_index))
        start = start_index + 1

    for position in positions:
        start_index, close_index = position[0], position[1]
        instructions.append(line[start_index:close_index+1])

    instructions = [x for x in instructions if is_valid(x)]
    return instructions

def get_numbers(instruction):
    numbers = [int(x) for x in instruction[4:-1].split(",")]
    return numbers

with open(input_path, "r") as file:
    for line in file:
        instructions = get_instructions(line)
        for instruction in instructions:
            numbers = get_numbers(instruction)
            product = numbers[0] * numbers[1]
            sum += product

print(sum)