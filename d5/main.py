def read_file():
    line_listing = []
    row = []
    f = open("lines.txt", "r")
    content=f.readlines()
    tmp = {}
    maximum = 0
    for line in content:
        packet = ",".join(line.split(" -> "))
        points = packet.split(",")
        maximum = maximum if maximum > int(points[0]) else int(points[0])
        maximum = maximum if maximum > int(points[1]) else int(points[1])
        maximum = maximum if maximum > int(points[2]) else int(points[2])
        maximum = maximum if maximum > int(points[3]) else int(points[3])

        if int(points[1]) == int(points[3]):
            pointA = {"x":int(points[0]),"y":int(points[1]),"type":0}   #row
            pointB = {"x":int(points[2]),"y":int(points[3]),"type":0}
            if int(points[0]) > int(points[2]):
                pointA , pointB = pointB, pointA
        elif int(points[0]) == int(points[2]):
            pointA = {"x":int(points[0]),"y":int(points[1]),"type":1}   #column
            pointB = {"x":int(points[2]),"y":int(points[3]),"type":1}
            if int(points[1]) > int(points[3]):
                pointA , pointB = pointB, pointA
        else:
            pointA = {"x":int(points[0]),"y":int(points[1]),"type":2}   #diagonal
            pointB = {"x":int(points[2]),"y":int(points[3]),"type":2}

        row.append(pointA)
        row.append(pointB)
        line_listing.append(row)
        row = []
    return [line_listing,maximum]

def print_row_list(list):
    rows = len(list)
    columns = 2
    for i in range(rows):
        for j in range(columns):
            if list[i][j]["type"]==0:
                print(str(list[i][j]["x"]) + " -> " + str(list[i][j]["y"]) + " r| ",end="")
            elif list[i][j]["type"]==1:
                print(str(list[i][j]["x"]) + " -> " + str(list[i][j]["y"]) + " c| ",end="")
            else:
                print(str(list[i][j]["x"]) + " -> " + str(list[i][j]["y"]) + " d| ",end="")
        print("\n")

def print_matrix(matrix):
    rows = 10
    columns = 10
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j]==0:
                print(". |",end="")
            else:
                print(str(matrix[i][j]) + " |",end="")
        print("\n")

def sorting_parameter(input):
    return input[0]["type"]

def rc_diagram(input,maximum):
    matrix = [ [ 0 for i in range(maximum+1) ] for j in range(maximum+1) ]
    rows = len(input)
    counter = 0
    for i in range(rows):
        if input[i][0]["type"]==0:
            for k in range(input[i][0]["x"],(input[i][1]["x"])+1):
                matrix[input[i][0]["y"]][k] += 1
        if input[i][0]["type"]==1:
            for k in range(input[i][0]["y"],(input[i][1]["y"])+1):
                matrix[k][input[i][0]["x"]] += 1
        if input[i][0]["type"]==2:
            #print("Diagonal is",input[i])
            y_movement = 1 if input[i][0]["y"]-(input[i][1]["y"]) < 0 else -1
            x_movement = 1 if input[i][0]["x"]-(input[i][1]["x"]) < 0 else -1
            #print("Y:",y_movement,"X:",x_movement,"Needs steps:")
            #print(range(input[i][0]["y"],(input[i][1]["y"])+1))
            y_step = input[i][0]["y"]
            x_step = input[i][0]["x"]
            steps = abs(input[i][0]["y"]-input[i][1]["y"])
            for i in range(steps+1):
                #print("y step:",y_step)
                #print("x step:",x_step)
                matrix[y_step][x_step] += 1
                y_step += y_movement
                x_step += x_movement
    for i in range(maximum + 1):
        for j in range(maximum + 1):
            if matrix[i][j] > 1:
                counter += 1
    #print_matrix(matrix)
    print("The answer is",end=" ")
    print(counter)

def main():
    results = read_file()
    inputs = results[0]
    maximum = results[1]
    inputs.sort(key=sorting_parameter)
    rc_diagram(inputs,maximum)
    #print_row_list(inputs)

if __name__ == "__main__":
    main()