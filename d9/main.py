def read_file():
    f = open("cave.txt", "r")
    content=f.readlines()
    cave = []
    visit = []
    for line in content:
        row = []
        visited_line = []
        for number in line:
            if number != '\n':
                row.append(int(number))
                visited_line.append(False)
        cave.append(row)
        visit.append(visited_line)
    return [cave,visit]

def choose_points(i,j,matrix):
    no_up = False
    no_down = False
    no_left = False
    no_right = False

    if i==0:
        no_up = True
    elif i==len(matrix)-1:
        no_down = True

    if j==0:
        no_left = True
    elif j==len(matrix[i])-1:
        no_right = True

    return [no_up,no_down,no_left,no_right]

def lowPoints(cave):
    low_points = []
    low_points_locations = []
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            not_low = False
            
            no_up,no_down,no_left,no_right = choose_points(i,j,cave)
            targets = pinpointPoints(no_up,no_down,no_left,no_right,i,j)

            for x,y in list(targets):
                if cave[i][j] >= cave[x][y]:
                    not_low = True

            if(not not_low):
                low_points.append(cave[i][j] + 1)
                low_points_locations.append((i,j))
    return [low_points,low_points_locations]

def pinpointPoints(no_up,no_down,no_left,no_right,i,j):
    x = [i-1,'l','r',i+1]
    y = ['u',j-1,j+1,'d']

    if no_up:
        x.remove(i-1)
        y.remove('u')
        change = True
    if no_down:
        x.remove(i+1)
        y.remove('d')
        change = True
    if no_left:
        x.remove('l')
        y.remove(j-1)
        change = True
    if no_right:
        x.remove('r')
        y.remove(j+1)
        change = True

    for entry in range(len(x)):
        if x[entry] == 'l' or x[entry] == 'r':
            x[entry] = i
    for entry in range(len(y)):
        if y[entry] == 'u' or y[entry] == 'd':
            y[entry] = j

    return zip(x,y)

def basins(cave,visit,low_points_locations):
    basins = [0,0,0]
    result = 1

    for x,y in low_points_locations:
        basin_size = DFS(cave,visit,x,y)
        basins.append(basin_size)
        basins.sort(reverse=True)
        basins.pop()
    for x in basins:
        result *= x
    print("The size of the 3 basins is:",result)

def DFS(cave,visit,x,y):
    visited_count = 0
    stack = []

    stack.append((x,y))
    while len(stack) > 0:
        i,j = stack.pop()
        if not visit[i][j]:
            visited_count += 1
            visit[i][j] = True
            no_up,no_down,no_left,no_right = choose_points(i,j,cave)
            targets = pinpointPoints(no_up,no_down,no_left,no_right,i,j)

            for position_x,position_y in list(targets):
                if cave[position_x][position_y] != 9 and not visit[position_x][position_y]:
                    stack.append((position_x,position_y))

    return visited_count

def print_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
                print(str(matrix[i][j]) + " |",end="")
        print("\n")

def main():
    cave,visit = read_file()
    low_points,low_points_locations = lowPoints(cave)
    basins(cave,visit,low_points_locations)
    print("The risk level is:",sum(low_points))

if __name__ == "__main__":
    main()