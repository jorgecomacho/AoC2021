filename = 'day1-2021.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def depth_trend(lines):
    count = 0
    value = int(lines[0]) 
    for line in lines:
        if int(line) > value:
            count += 1
        value = int(line)
    return count

def slider_count(lines):
    int_lines = [int(i) for i in lines]
    count = 0
    value = sum(int_lines[0:3])
    for i in range(3, len(lines)):
        if sum(int_lines[i-2:i+1]) > value:
            count += 1
        value = sum(int_lines[i-2:i+1])
    return count

if __name__ == "__main__":
    lines = read_file(filename)
    print(depth_trend(lines))
    print(slider_count(lines))
