from math import ceil


def order_pages_by_printing_rules(pages_to_print, printing_rules):
    matches = []
    for match in set(pages_to_print).difference(printing_rules.keys()):
        matches.append((match, {}))

    for page in set(pages_to_print).intersection(printing_rules.keys()):
        matches.append((page, set(pages_to_print).intersection(printing_rules[page])))

    matches.sort(key=lambda m: len(m[-1]))
    order_of_printing = []
    for page_rule in matches:
        order_of_printing.append(page_rule[0])
    return order_of_printing


with open('input', 'r') as f:
    arr = [list(line.strip('\n')) for line in f]

arr1 = []
arr2 = []

for index, item in enumerate(arr):
    if not item:
        arr1 = [(''.join(char).split('|')) for char in arr[0:index]]
        arr2 = [''.join(char).split(',') for char in arr[index+1:]]
        break

item_rules = {}
for item in arr1:
    if item[-1] in item_rules.keys():
        item_rules[item[-1]].append(item[0])
    else:
        item_rules[item[-1]] = [item[0]]

ok_ordered_mid_p_num_sum = 0
nok_ordered_mid_p_num_sum = 0

for update in arr2:
    pages_to_print_in_order = order_pages_by_printing_rules(update, item_rules)
    if all([j == k for j, k in zip(pages_to_print_in_order, update)]):
        ok_ordered_mid_p_num_sum += int(update[ceil(len(update)/2)-1])
    elif all(j in pages_to_print_in_order for j in update):
        nok_ordered_mid_p_num_sum += int(pages_to_print_in_order[ceil(len(pages_to_print_in_order)/2)-1])
    else:
        print(update)
        print(pages_to_print_in_order)
        break

print(ok_ordered_mid_p_num_sum)
print(nok_ordered_mid_p_num_sum)
