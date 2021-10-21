import re

def counter(expr):
    indexes = []
    while True:
        r = re.search(r'd(\d+)', expr)
        if r == None: break
        expr = expr[:r.start()] + 'i[' + str(len(indexes)) + '][0]' + expr[r.end():]
        indexes.append([0, int(r.group(1))])
    return cntr(expr, indexes, 0)

def cntr(expr, indexes, level):
    if level >= len(indexes): return {eval(expr, {}, {'i': indexes}): 1}
    result = {}
    for indexes[level][0] in range(1, indexes[level][1] + 1):
        for key, val in cntr(expr, indexes, level + 1).items(): result[key] = result[key] + val if key in result else val
    return result

res = counter(input())
all = sum(res.values())
for key in sorted(res.keys()): print('{:d} {:.2f}'.format(key, res[key] * 100 / all))
