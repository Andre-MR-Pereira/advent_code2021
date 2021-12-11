BINARY_INPUT_SIZE = 12 #12
def read_file():
    matrix = []
    f = open("diagnostic.txt", "r")
    content=f.readlines()
    for line in content:
        matrix.append(line.rstrip("\n"))
    return matrix

def CB(matrix):
    gamma_binary = ''
    epsilon_binary = ''
    for column in range(BINARY_INPUT_SIZE):
        true_counter = 0
        false_counter = 0
        for row in range(len(matrix)):
            if matrix[row][column] == '1':
                true_counter += 1
            else:
                false_counter += 1
        if true_counter > false_counter:
            gamma_binary += '1'
            epsilon_binary += '0'
        else:
            gamma_binary += '0'
            epsilon_binary += '1'

    return [bin2dec(gamma_binary),bin2dec(epsilon_binary)]

def merge_step(matrix):
    O2_binary_list = []
    CO2_binary_list = []
    
    true_counter = 0
    false_counter = 0
    for row in range(len(matrix)):
        if matrix[row][0] == '1':
            true_counter += 1
        else:
            false_counter += 1
    if true_counter >= false_counter:
        decision_flag = '1'

    if true_counter < false_counter:
        decision_flag = '0'

    for row in range(len(matrix)):
        if matrix[row][0] == decision_flag:
            O2_binary_list.append(matrix[row])
        else:
            CO2_binary_list.append(matrix[row])  

    return [O2_binary_list,CO2_binary_list]

def filtering_step(O2_binary_list,CO2_binary_list):

    for column in range(1,BINARY_INPUT_SIZE):
        if len(O2_binary_list) == 1 and len(CO2_binary_list) == 1:
            return [bin2dec(O2_binary_list.pop()),bin2dec(CO2_binary_list.pop())]
        true_counter_O2 = 0
        false_counter_O2 = 0
        true_counter_CO2 = 0
        false_counter_CO2 = 0
        for row in range( len(O2_binary_list) if len(O2_binary_list) > len(CO2_binary_list) else len(CO2_binary_list)):
            if  row<len(O2_binary_list) and O2_binary_list[row][column] == '1' :
                true_counter_O2 += 1
            else:
                if row<len(O2_binary_list):
                    false_counter_O2 += 1
            if row<len(CO2_binary_list) and CO2_binary_list[row][column] == '1':
                true_counter_CO2 += 1
            else:
                if row<len(CO2_binary_list):
                    false_counter_CO2 += 1

        if true_counter_O2 >= false_counter_O2:
            decision_flag_O2 = '0'

        if true_counter_O2 < false_counter_O2:
            decision_flag_O2 = '1'

        if true_counter_CO2 >= false_counter_CO2:
            decision_flag_CO2 = '1'

        if true_counter_CO2 < false_counter_CO2:
            decision_flag_CO2 = '0'

        O2_holder = []
        CO2_holder = []
        for row in range(len(O2_binary_list) if len(O2_binary_list) > len(CO2_binary_list) else len(CO2_binary_list)):
            if row<len(O2_binary_list) and O2_binary_list[row][column] != decision_flag_O2:
                O2_holder.append(O2_binary_list[row])
            if row<len(CO2_binary_list) and CO2_binary_list[row][column] != decision_flag_CO2:
                CO2_holder.append(CO2_binary_list[row])
        
        if len(O2_holder) > 0:
            O2_binary_list = O2_holder
        if len(CO2_holder) > 0:
            CO2_binary_list = CO2_holder

    return [bin2dec(O2_binary_list.pop()),bin2dec(CO2_binary_list.pop())]

def bin2dec(binary):
    return int(binary,2)

def P1():
    inputs = read_file()
    results = CB(inputs)
    gamma = results[0]
    epsilon = results[1]
    print(gamma*epsilon)

def P2():
    inputs = read_file()
    lists = merge_step(inputs)
    O2_binary_list = lists[0]
    CO2_binary_list = lists[1]
    measurements = filtering_step(O2_binary_list,CO2_binary_list)
    print(measurements)
    print(measurements[0]*measurements[1])

if __name__ == "__main__":
    #P1()
    P2()