changes = [int(i) for i in open("info.txt", "r").readlines()]
print(sum(changes))

from itertools import accumulate, cycle
seen = set()
print(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))
