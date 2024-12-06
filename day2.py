# Part One

safe_reports = 0

def is_increasing(report):
    before = report[0]
    for level in report[1:]:
        if level <= before:
            return False
        before = level
    return True

def is_decreasing(report):
    before = report[0]
    for level in report[1:]:
        if level >= before:
            return False
        before = level
    return True

def max_diff(report):
    result = 0
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff > result:
            result = diff
    return result

def is_safe(report):
    return max_diff(report) in range(1, 4) and (is_increasing(report) or is_decreasing(report))

with open("inputs/day2.txt", "r") as file:
    for line in file:
        report = [int(x) for x in line.split()]
        if is_safe(report):
            safe_reports += 1
        else:
            # Part Two
            for x in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(x)
                if is_safe(report_copy):
                    safe_reports += 1
                    break

print(safe_reports)

