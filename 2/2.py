from operator import xor


def safe_unsafe(items):
    lvl_change = [int(j) - int(i) for i, j in zip(items[:-1], items[1:])]
    return (all(i > 0 for i in lvl_change) or all(i < 0 for i in lvl_change)) and all(abs(i) <= 3 for i in lvl_change)


def safe_unsafe_problem_damped(items):
    lvl_change = [j - i for i, j in zip(items[:-1], items[1:])]
    too_big_lvl_change = sum([abs(i) > 3 for i in lvl_change]) > 0
    same_dir = abs(sum([i > 0 for i in lvl_change]) - sum([i < 0 for i in lvl_change])) >= len(items) - 1
    if not (same_dir and not too_big_lvl_change):
        for j, _ in enumerate(items):
            safe = safe_unsafe(items[0:j]+items[j+1:])
            if safe:
                return True
        else:
            return False
    return True


safe_reports = 0
safe_reports_damped = 0
with open('input', 'r') as f:
    for line in f:
        x = line.split()
        x = [int(i) for i in x]
        safe_reports += safe_unsafe(x)
        safe_reports_damped += safe_unsafe_problem_damped(x)

print(f'Num of safe reports: {safe_reports}')
print(f'Num of safe reports with problem dampening: {safe_reports_damped}')
