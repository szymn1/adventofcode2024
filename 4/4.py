import re
import numpy as np
from math import floor


def find_str_right_down_diag(in_arr, pattern_arr):
    counter = 0

    if len(pattern_arr) <= 1:
        for j, _ in enumerate(in_arr):
            for y in in_arr[j]:
                print(f'{pattern_arr[0]} CMP : {y}')
                if y == pattern_arr[0]:
                    print(f'{in_arr}: {in_arr.shape}')
                    print(f'{pattern_arr}: {len(pattern_arr)}')
                    print(f'MATCH: {pattern_arr[0]} at {j}\n')
                    counter += 1
        return counter
    else:
        for j, x in enumerate(in_arr):
            print(f'j: {j}')
            for k, y in enumerate(in_arr[j]):
                print(f'k: {k}')
                if in_arr[j, k] == pattern_arr[0]:
                    print(f'{in_arr}: {in_arr.shape}')
                    print(f'{pattern_arr}: {len(pattern_arr)}')
                    print(f'MATCH: {pattern_arr[0]} at {j}, {k}\n')
                    counter += find_str_right_down_diag(
                        in_arr[j:j+len(pattern_arr), k:k+len(pattern_arr)], pattern_arr[1:])
    return counter


def findall_right(in_arr, re_pattern):
    counter = 0
    for row in in_arr:
        counter += len(re.findall(re_pattern, ''.join(row)))
        counter += len(re.findall(re_pattern, ''.join(row[::-1])))
    return counter


def findall_diag(in_arr, re_pattern):
    counter = 0
    main_diag = np.diag(in_arr)
    counter += len(re.findall(re_pattern, ''.join(np.diag(in_arr))))
    counter += len(re.findall(re_pattern, ''.join(np.diag(in_arr))[::-1]))
    for j in range(1, len(main_diag)):
        upper_diag = ''.join(np.diag(in_arr, j))
        lower_diag = ''.join(np.diag(in_arr, -j))
        for diag in (upper_diag, upper_diag[::-1], lower_diag, lower_diag[::-1]):
            counter += len(re.findall(re_pattern, diag))
    return counter


def findall_x(in_arr, pattern_str):
    found_x = 0
    x_arr_dim = len(pattern_str)
    pattern = re.compile(pattern_str)
    pattern_inv = re.compile(pattern_str[::-1])
    for j, row in enumerate(in_arr[1:-1, 1:-1], start=1):
        for k, _ in enumerate(row, start=1):
            if in_arr[j, k] == pattern_str[floor(x_arr_dim/2)]:
                diag_x = ''.join(np.diag(in_arr[j-1:j+x_arr_dim-1, k-1:k+x_arr_dim-1]))
                diag_inv_x = ''.join(np.diag(np.flipud(in_arr[j-1:j+x_arr_dim-1, k-1:k+x_arr_dim-1])))
                if ((re.search(pattern, diag_x) or re.search(pattern_inv, diag_x)) and
                        (re.search(pattern, diag_inv_x) or re.search(pattern_inv, diag_inv_x))):
                    found_x += 1
    return found_x


with open('input', 'r') as f:
    arr = np.array([list(line.strip('\n')) for line in f])

pattern = re.compile(r'XMAS')

word_count = 0
word_count += findall_right(arr, pattern)
word_count += findall_right(arr.T, pattern)
word_count += findall_diag(arr, pattern)
word_count += findall_diag(np.flipud(arr), pattern)

print(f'WORD MATCH: {word_count}')
print(f'X MATCH: {findall_x(arr, 'MAS')}')

