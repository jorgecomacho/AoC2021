filename = 'day2.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def position(lines):
    multiplier = {'down':1, 'up':-1}
    horizontal = 0
    depth = 0
    for line in lines:
        direction, distance = line.strip().split()
        if direction not in multiplier.keys():
            horizontal += int(distance)
            continue
        depth += multiplier[direction] * int(distance)
    return horizontal, depth

def position_aim(lines):
    multiplier = {'down':1, 'up':-1}
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        direction, distance = line.strip().split()
        if direction not in multiplier.keys():
            horizontal += int(distance)
            depth += int(distance) * aim
            continue
        aim += multiplier[direction] * int(distance)
    return horizontal, depth

if __name__ == "__main__":
    lines = read_file(filename)
    x, y = position(lines)
    print(x, y, x*y)
    x, y = position_aim(lines)
    print(x, y, x*y)