import re


def calc(mul_arr):
    result = 0
    for mul in mul_arr:
        mul = mul.split('(')[1].strip(')').split(',')
        result += int(mul[0]) * int(mul[1])
    return result


txt_in = ""
with open('input', 'r') as f:
    for line in f:
        txt_in += str(line.strip('\n'))
muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', txt_in)


print(f'No ctrl: {calc(muls)}')


first = re.search(r'(don\'t\(\)|do\(\))', txt_in)
first_muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', txt_in[0:first.span()[0]])

do_muls = re.findall(r'((do\(\)).*?(don\'t\(\))|(do\(\).*))', txt_in)


muls = []
for mul in do_muls:
    print(f'\n{mul}')
    muls += re.findall(r'mul\(\d{1,3},\d{1,3}\)', mul[0])


do_muls = first_muls + muls
print(f'With ctrl: {calc(do_muls)}')
