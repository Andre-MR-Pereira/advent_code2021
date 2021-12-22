def read_file():
    f = open("given.txt", "r")
    content=f.readlines()
    inputs_list = []
    outputs_list = []
    for line in content:
        digit_dictionary = {'1': [],'4': [],'7': [],'8': [],'235': [],'069': []}
        buffer = line.split("|")
        inputs = buffer[0].split(" ")
        inputs = inputs[0:len(inputs)-1]
        outputs = buffer[1].split(" ")
        outputs = outputs[1:len(outputs)]
        outputs[len(outputs)-1] = outputs[len(outputs)-1].rstrip("\n")
        for digit in inputs:
            create_dictionary_entry(digit,digit_dictionary)
        inputs_list.append(digit_dictionary)
        outputs_list.append(outputs)
    return [inputs_list,outputs_list]


def create_dictionary_entry(digit,digit_dictionary):
    if len(digit) == 2:
        digit_dictionary['1'].append(digit)
    elif len(digit) == 3:
        digit_dictionary['7'].append(digit)
    elif len(digit) == 4:
        digit_dictionary['4'].append(digit)
    elif len(digit) == 5:
        digit_dictionary['235'].append(digit)
    elif len(digit) == 6:
        digit_dictionary['069'].append(digit)
    elif len(digit) == 7:
        digit_dictionary['8'].append(digit)
    else:
        print("Unknown digit")

def count_entries(outputs):
    ones = 0
    fours = 0
    sevens = 0
    eights = 0
    distincts = 0
    for i in range(len(outputs)):
        for k in range(len(outputs[i])):
            if len(outputs[i][k]) == 2:
                ones += 1
            elif len(outputs[i][k]) == 3:
                sevens += 1
            elif len(outputs[i][k]) == 4:
                fours += 1
            elif len(outputs[i][k]) == 7:
                eights += 1
            else:
                distincts += 1

    print("Ones:",ones,"Fours:",fours,"Sevens:",sevens,"Eigths:",eights,"Distincts:",distincts)
    print("Total:",ones+fours+sevens+eights)

def untangle_wires(digit_dictionary):
    words_dictionary = {'0': '','1': digit_dictionary['1'][0], '2': '','3': '','4': digit_dictionary['4'][0],'5': '','6': '','7': digit_dictionary['7'][0],'8': digit_dictionary['8'][0],'9': ''}
    wires_dictionary = {'a': '','b': '', 'c': '','d': '','e': '','f': '','g': ''}

    wires_dictionary['a'] = compare_digits(words_dictionary['1'],words_dictionary['7'])[0]
    b_d = compare_digits(words_dictionary['1'],words_dictionary['4'])
    b_d_e_g = compare_digits(words_dictionary['7'],words_dictionary['8'])

    for digit in digit_dictionary['069']:
        counter_0 = 0
        counter_1 = 0
        counter_6 = 0
        for letter in digit:
            if letter == b_d[0]:
                counter_0 += 1
            if letter == b_d[1]:
                counter_1 += 1
            if letter == words_dictionary['1'][0] or letter == words_dictionary['1'][1]:
                counter_6 += 1
        if (counter_0 == 1 and counter_1== 0) or (counter_0 == 0 and counter_1 == 1):
            wires_dictionary['d'] = b_d[0] if counter_0 == 0 else b_d[1]
            wires_dictionary['b'] = b_d[0] if counter_0 == 1 else b_d[1]
            words_dictionary['0'] = digit
        elif counter_6 == 1:
            words_dictionary['6'] = digit
        else:
            words_dictionary['9'] = digit

    for digit in digit_dictionary['235']:    
        comparison_1 = 0
        comparison_6 = compare_digits(words_dictionary['6'],digit)
        for letter in digit:
            if letter == words_dictionary['1'][0] or letter == words_dictionary['1'][1]:
                comparison_1 += 1
        if len(comparison_6) == 1:
            words_dictionary['5'] = digit
        elif comparison_1 == 2:
            words_dictionary['3'] = digit
        else:
            words_dictionary['2'] = digit
    
    return words_dictionary



def compare_digits(string_A,string_B):
    counter = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    distincts = []
    for A in string_A:
        counter[A]+=1
    for B in string_B:
        if counter[B]==1:
            counter[B] = -1
        else:
            counter[B] += 1
    for key,value in counter.items():
        if value == 1:
            distincts.append(key)
    return distincts


def data_analyser(dataset):
    result = 0
    for inputs,outputs in zip(dataset[0],dataset[1]):
        pre_built_number = []
        words_dictionary = untangle_wires(inputs)
        for number in outputs:
            analysis_number = sorted(number)
            result_number = "".join(analysis_number)
            for key,value in words_dictionary.items():
                analysis_value = sorted(value)
                result_value = "".join(analysis_value)
                if result_number == result_value:
                    pre_built_number.append(key)
        built_number = int("".join(pre_built_number))
        result += built_number
    print("Added outputs:",result)
                    
def main():
    dataset = read_file()
    count_entries(dataset[1])
    data_analyser(dataset)

if __name__ == "__main__":
    main()