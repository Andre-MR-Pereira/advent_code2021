WINDOW_SIZE = 3

def windowed_prefix_sum(depths):
    size = len(depths)
    P = [0] * size
    buffer = [0] * WINDOW_SIZE
    for i in range(WINDOW_SIZE):
        buffer[i] = depths[i]
    buffer = prefix_sum(buffer)
    for i in range(len(buffer)):
        P[i] = buffer[i]
    for i in range(WINDOW_SIZE, len(depths)):
        P[i] = P[i - 1] + depths[i] - depths[i - WINDOW_SIZE]
    return_size = len(depths) - WINDOW_SIZE + 1
    window_sum = [0] * return_size
    for i in range(return_size):
        window_sum[i] = P[i + WINDOW_SIZE - 1]
    return window_sum

def global_subtractor(depths):
    size = len(depths)
    subtracted = [0] * size
    logical_subtracted = [0] * size
    subtracted[size-1] = 0
    logical_subtracted[size-1] = 0
    for i in range(1, size):
        subtracted[i] = depths[i - 1] - depths[i]
        if (subtracted[i] < 0):
            logical_subtracted[i] = 1
    return [subtracted,logical_subtracted]

def prefix_sum(A):
    size = len(A)
    P = [0] * size
    P[0] = A[0]
    for i in range(1, size):
        P[i] = P[i - 1] + A[i]
    return P

def count_total(P, x, y):
    return (P[y] - P[x - 1] if x > 0 else P[y])

def read_file():
    inputs = []
    f = open("depths.txt", "r")
    input=f.readlines()
    for line in input:
        inputs.append(int(line))
    return inputs

def P1():
    input_depths = read_file()
    depth_interpretation = global_subtractor(input_depths)
    result = prefix_sum(depth_interpretation[1])
    print(input_depths)
    print("There are " + str(result[len(result) - 1]) + " measurements that are larger than the previous measurement.")

def P2():
    input_depths = read_file()
    windowed_depths = windowed_prefix_sum(input_depths)
    depth_interpretation = global_subtractor(windowed_depths)
    result = prefix_sum(depth_interpretation[1])
    print("There are " + str(result[len(result) - 1]) + " measurements that are larger than the previous measurement.")


if __name__ == "__main__":
    #P1()
    P2()