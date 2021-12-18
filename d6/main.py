DAYS = 1000000

def read_file():
    line_listing = []
    row = []
    f = open("fish.txt", "r")
    content=f.readlines()
    tmp = {}
    maximum = 0
    for line in content:
        fishes = line.split(",")
    return fishes

def create_grouping(fishes):
    current = fishes[0]
    group = []
    buffer = {'start':current,'amount':0,'spawned':0, 'extra':0}
    for i in range(len(fishes)):
        if fishes[i] != current:
            group.append(buffer)
            current = fishes[i]
            buffer = {'start':current,'amount':1,'spawned':0, 'extra':0}
        else:
            buffer["amount"] += 1
    group.append(buffer)
    return group

def ceildiv(a,b):
    return -(a // -b)

def predict_evolution(dataset,pascal_triangle):
    import math

    total_fishes = 0
    for i in range(len(dataset)):
        F = ceildiv(DAYS - (int(dataset[i]["start"]) + 1), 7)
        L = ceildiv(DAYS - (int(dataset[i]["start"]) + 1), 9)
        previous_level_last_day = (int(dataset[i]["start"]) + 1) + 9*(L -1)
        previous_level_first_day = previous_level_last_day - 2 * (len(pascal_triangle[L - 1]) - 1)
        current_level_first_day = previous_level_first_day + 7
        current_level_last_day = (int(dataset[i]["start"]) + 1) + 9*(L)
        previous_fishes = sum(pascal_triangle[L - 1]) * dataset[i]["amount"]
        #print("First day of current will be:",current_level_first_day)
        if current_level_first_day <= DAYS:
            stop_day = 0
            while (current_level_first_day + 2*stop_day) <= DAYS:
                stop_day += 1
            #print("Stop:",stop_day,"Passos:",sum(pascal_triangle[L][0:stop_day]),sum(pascal_triangle[L][0:stop_day])*dataset[i]["amount"],(sum(pascal_triangle[L][0:stop_day])*dataset[i]["amount"])/2)
            current_fishes = previous_fishes + int((sum(pascal_triangle[L][0:stop_day])*dataset[i]["amount"])/2)
        else:
            current_fishes = previous_fishes
        extra_fishes = 0
        next_lines_check = math.floor(((DAYS - (int(dataset[i]["start"]) + 1))*2)/63)
        for extra in range(next_lines_check):
            stop_day = 0
            pascal_line = pascal_triangle[L + extra + 1]
            previous_level_last_day = (int(dataset[i]["start"]) + 1) + 9*(L + extra)
            previous_level_first_day = previous_level_last_day - 2 * (len(pascal_triangle[L + extra]) - 1)
            current_level_first_day = previous_level_first_day + 7
            while (current_level_first_day + 2*stop_day) <= DAYS:
                stop_day += 1
            extra_fishes += int(sum(pascal_line[0:stop_day]) * dataset[i]["amount"] / 2)
            #print("Ciclo: First day of previous will be:",previous_level_first_day)
            #print("Ciclo: First day of current will be:",current_level_first_day)
            #print("Ciclo: Pascal line will be:",pascal_line,"e escolhe: ",pascal_line[0:stop_day])
        #print(i+1,"Previous last day:",previous_level_last_day,"Current level last day:",current_level_last_day)
        #print("First day of previous will be:",previous_level_first_day)
        #print("First day of current will be:",current_level_first_day)
        #print("Pascal line will be:",pascal_triangle[L])
        #print("Previous level fishes be:",previous_fishes)
        #print("Current level fishes be:",current_fishes)
        #print("Extra fishes:",extra_fishes)
        dataset[i]["spawned"] = current_fishes
        dataset[i]["extra"] = extra_fishes
        total_fishes += current_fishes + extra_fishes
        print("===")
    print("Sum is: ", total_fishes)

def generate_binary_pascal_triangle():
    import math

    pascal_triangle = [] 
    N_levels = math.ceil(math.sqrt(DAYS) * 7)

    for i in range(N_levels):  
        pascal_triangle.append([])  
        pascal_triangle[i].append(1*2)  
        for j in range(1, i):  
            pascal_triangle[i].append((pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]))
        if(N_levels != 0):  
            pascal_triangle[i].append(1*2)  
    for i in range(N_levels):  
        print(" " * (N_levels - i), end = " ", sep = " ")  
        for j in range(0, i + 1):  
            print('{0:6}'.format(pascal_triangle[i][j]), end = " ", sep = " ")  
        print()
    print("Niveis:",N_levels)
    return pascal_triangle

def main():
    fishes = read_file()
    fishes.sort()
    dataset = create_grouping(fishes)
    pascal_triangle = generate_binary_pascal_triangle()
    predict_evolution(dataset,pascal_triangle)
    print(dataset)

if __name__ == "__main__":
    main()