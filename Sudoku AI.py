import time


def read_file(text_file):
    f = open(text_file)
    lst = []
    for i in range(9):
        word = f.readline()
        for j in word:
            if j != "\n":
                lst.append(int(j))
    f.close()
    return lst


def print_table(array):
    for i in range(81):
        print(array[i],end="")
        if (i+1) % 3 == 0:
            print("\t",end="")
            if (i+1) % 9 == 0:
                print()
                if i == 26 or i == 53:
                    print()
    return


def generate_column(nth):
    variable = nth
    column = []
    for i in range(9):
        variable += 9
        if variable > 80:
            variable -= 81
        column.append(variable)
    return sorted(column)


def generate_row(nth):
    if 0 <= nth <= 8:
        row = [i for i in range(0,9)]
    elif 9 <= nth <= 17:
        row = [i for i in range(9, 18)]
    elif 18 <= nth <= 26:
        row = [i for i in range(18, 27)]
    elif 28 <= nth <= 35:
        row = [i for i in range(27, 36)]
    elif 36 <= nth <= 44:
        row = [i for i in range(36, 45)]
    elif 45 <= nth <= 53:
        row = [i for i in range(45, 54)]
    elif 54 <= nth <= 62:
        row = [i for i in range(54, 63)]
    elif 63 <= nth <= 71:
        row = [i for i in range(63, 72)]
    elif 72 <= nth <= 80:
        row = [i for i in range(72, 81)]
    else:
        row = []
    return sorted(row)


def generate_block(nth):
    all_block = []
    for i in range(0,7,3):
        all_block.append(block_rule(i))
    for i in range(27,34,3):
        all_block.append(block_rule(i))
    for i in range(54,61,3):
        all_block.append(block_rule(i))
    for sub_block in all_block:
        if nth in sub_block:
            return sorted(sub_block)


def block_rule(n):
    array = []
    for i in range(n,n+3):
        array.append(i)
        array.append(i+9)
        array.append(i+18)
    return sorted(array)


def full(array):
    for i in range(81):
        if array[i] == 0:
            return False
    return True


def find_blank(array):
    blank_space = []
    for i in range(81):
        if array[i] == 0:
            blank_space.append(i)
    if len(blank_space) > 0:
        return blank_space, True
    else:
        return None, False


def available_number(nth, array):
    row = generate_row(nth)
    column = generate_column(nth)
    block = generate_block(nth)
    unavailable = set()
    available = []
    for i in row:
        if array[i] != 0:
            unavailable.add(array[i])
    for i in block:
        if array[i] != 0:
            unavailable.add(array[i])
    for i in column:
        if array[i] != 0:
            unavailable.add(array[i])
    for i in range(1,10):
        if i not in unavailable:
            available.append(i)
    if len(available) > 0:
        return sorted(available), True
    else:
        return None, False


def solved(array):
    if full(array):
        return True
    square = -1
    if find_blank(array)[1]:
        available_blank = find_blank(array)[0]
        square = available_blank[0]
    if available_number(square, array)[1]:
        for i in available_number(square, array)[0]:
            array[square] = i
            if solved(array):
                return True
            array[square] = 0
    return False


start = time.time()
lst = read_file("Sudoku.txt")
print_table(lst)
print("\n")
print("Solution:")
if solved(lst):
    print_table(lst)
elapsed = time.time() - start
print("Result found in %f seconds"%(elapsed))
