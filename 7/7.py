import itertools as it
from multiprocessing import Pool


def calc_equation(equation, opers=''):
    opers = opers if opers else ['+', '*']
    line_nr = equation[0]
    equation = equation[1]
    all_operators = list(it.product(opers, repeat=len(equation[1])-1))

    for op in all_operators:
        eq = [''.join(j) for j in zip(op, equation[1][1:])]
        res = str(equation[1][0])
        for item in eq:
            if '||' in item:
                res += item[2:]
            else:
                res = str(eval(res + item))
            if int(res) > int(equation[0]):
                break
            if res == equation[0] and item == eq[-1]:
                print(f'LINE {str(line_nr).zfill(3)}: {equation[0]}={str(equation[1][0]) + ''.join(eq)}')
                return int(equation[0])

    return 0


if __name__ == "__main__":
    lines = []
    with open('input', 'r') as f:
        for line in f:
            line = line.strip('\n').split(': ')
            line[1] = line[1].split()
            lines.append(line)

    pool = Pool(10)
    results = pool.imap(calc_equation, enumerate(lines))
    print(f'SUM: {sum(results)}')

    inp = [(i, ['+', '*', '||']) for i in enumerate(lines)]

    results = pool.starmap(calc_equation, inp)
    print(f'SUM: {sum(results)}')
