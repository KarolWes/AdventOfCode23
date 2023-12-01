
def main(path):
    part2(path)


def part1(path):
    f = open(path, "r")
    data = f.read().split("\n")
    state = 0
    for line in data:
        if line != '':
            sign = line[0]
            val = int(line[1:])
            if sign == '+':
                state += val
            else:
                state -= val
    print(state)


def part2(path):
    f = open(path, "r")
    data = f.read().split("\n")
    state = 0
    all_states = {0}
    while True:
        for line in data:
            if line != '':
                sign = line[0]
                val = int(line[1:])
                if sign == '+':
                    state += val
                else:
                    state -= val
                if state in all_states:
                    print(state)
                    return
                else:
                    all_states.add(state)
    print(state)
