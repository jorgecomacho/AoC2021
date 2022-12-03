filename = 'day3.txt'

def read_file(fname):
    f = open(fname,"r")
    lines = f.readlines()
    return lines

def power_consumption(lines):
    gamma = ''
    epsilon = ''
    for i in range(len(lines[0].strip())):
        count = 0
        for line in lines:
            count += int(line[i])
        if float(count/len(lines)) > 0.5:
            gamma += '1'
            epsilon += '0'
            continue
        gamma += '0'
        epsilon += '1'
    return gamma, epsilon

def most_common(temp_list, index):
    count = 0
    l1 = []
    l0 = []
    for item in temp_list:
        item = item.strip()
        count += int(item[index])
        if item[index] == '1':
            l1.append(item)
        else:
            l0.append(item)
    if float(count/len(temp_list)) >= 0.5:
        return l1
    return l0

def least_common(temp_list, index):
    count = 0
    l1 = []
    l0 = []
    for item in temp_list:
        item = item.strip()
        count += int(item[index])
        if item[index] == '1':
            l1.append(item)
        else:
            l0.append(item)
    if float(count/len(temp_list)) < 0.5:
        return l1
    return l0

def other_science(lines):
    most = lines
    least = lines
    i = 0
    while len(most) > 1:
        most = most_common(most, i)
        i += 1
    i = 0
    while len(least) > 1:
        least = least_common(least, i)
        i += 1
    return most[0], least[0]

def unbinary(num):
    return int(num, 2)

if __name__ == "__main__":
    lines = read_file(filename)
    g, e = power_consumption(lines)
    print(unbinary(g), unbinary(e), unbinary(g)*unbinary(e))
    most, least = other_science(lines)
    print(unbinary(most), unbinary(least), unbinary(most) * unbinary(least))