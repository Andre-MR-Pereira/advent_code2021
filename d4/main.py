def read_file():
    bingo_boards = []
    bingo_order = []
    bingo_board = []
    buffer_line = []
    f = open("boards.txt", "r")
    content=f.readlines()
    bingo_shout = True
    for line in content:
        packet = line.split() if not bingo_shout else line.split(",")
        if len(packet) > 0:
            for x in packet:
                buffer_line.append({"value":int(x),"marked":0}) if not bingo_shout else bingo_order.append(int(x))
            if not bingo_shout:
                bingo_board.append(buffer_line)    
                buffer_line = []
        else:
            if len(bingo_board) > 0:
                bingo_boards.append(bingo_board)
                bingo_board = []
        bingo_shout = False
    bingo_boards.append(bingo_board)
    return [bingo_order,bingo_boards]

def print_row_matrix(matrix):
    amount_boards = len(matrix)
    rows = len(matrix[0])
    columns = len(matrix[0][0])
    for k in range(amount_boards):
        print("=========" + str(k) + "==========")
        for i in range(rows):
            for j in range(columns):
                if matrix[k][i][j]["marked"]==0:
                    print(str(matrix[k][i][j]["value"]) + " | ",end="")
                else:
                    print("("+str(matrix[k][i][j]["value"]) + ") | ",end="")
            print("\n")

def bingo(bingo_order,bingo_boards):
    amount_boards = len(bingo_boards)
    rows = len(bingo_boards[0])
    columns = len(bingo_boards[0][0])
    partial_sums = [0] * amount_boards
    print(amount_boards,rows,columns)
    for shouted_number in bingo_order:
        for k in range(amount_boards):
            stop_flag_columns = [True] * columns
            for i in range(rows):
                stop_flag_row = True
                for j in range(columns):
                    if shouted_number == bingo_boards[k][i][j]["value"]:
                        bingo_boards[k][i][j]["marked"]=1
                    if bingo_boards[k][i][j]["marked"]==0:
                        stop_flag_row = False
                        stop_flag_columns[j] = False
                        partial_sums[k] += bingo_boards[k][i][j]["value"]
                if stop_flag_row==True:
                    print("Final:")
                    print_row_matrix(bingo_boards)
                    print("\n")
                    sum = partial_sums[k]
                    for r in range(i+1,rows):
                        for c in range(columns):
                            if bingo_boards[k][r][c]["marked"]==0:
                                sum += bingo_boards[k][r][c]["value"]
                    return [sum,int(shouted_number)]
            for final_row in range(columns):
                if stop_flag_columns[final_row]==True:
                    print("Final:")
                    print_row_matrix(bingo_boards)
                    print("\n")
                    sum = partial_sums[k]
                    return [sum,int(shouted_number)]
            partial_sums[k] = 0
                
    return [-1,-1]

def bingo_loss(bingo_order,bingo_boards):
    amount_boards = len(bingo_boards)
    rows = len(bingo_boards[0])
    columns = len(bingo_boards[0][0])
    partial_sums = [0] * amount_boards
    finished_boards = [False] * amount_boards
    done_counter = 0
    print(amount_boards,rows,columns)
    for shouted_number in bingo_order:
        for k in range(amount_boards):
            if finished_boards[k] == False:
                done_flag_columns = [True] * columns
                for i in range(rows):
                    done_flag_row = True
                    for j in range(columns):
                        if shouted_number == bingo_boards[k][i][j]["value"]:
                            bingo_boards[k][i][j]["marked"]=1
                        if bingo_boards[k][i][j]["marked"]==0:
                            done_flag_row = False
                            done_flag_columns[j] = False
                            partial_sums[k] += bingo_boards[k][i][j]["value"]
                    if done_flag_row==True:
                        finished_boards[k] = True
                for final_row in range(columns):
                    if done_flag_columns[final_row]==True:
                        finished_boards[k] = True
        finished = amount_boards
        for k in range(amount_boards):
            if finished_boards[k] == True:
                finished -= 1
            else :
                board2finish = k
        if finished == 0:
            print("Final:")
            print_row_matrix(bingo_boards)
            print("\n")
            sum = partial_sums[board2finish]
            return [sum,int(shouted_number)]
        partial_sums = [0] * amount_boards
                
    return [-1,-1]
        

def P1():
    inputs = read_file()
    bingo_order = inputs[0]
    bingo_boards = inputs[1]
    #print_row_matrix(bingo_boards)
    result = bingo(bingo_order,bingo_boards)
    print(result)
    print(result[0]*result[1])

def P2():
    inputs = read_file()
    bingo_order = inputs[0]
    bingo_boards = inputs[1]
    #print_row_matrix(bingo_boards)
    result = bingo_loss(bingo_order,bingo_boards)
    print(result)
    print(result[0]*result[1])


if __name__ == "__main__":
    #P1()
    P2()