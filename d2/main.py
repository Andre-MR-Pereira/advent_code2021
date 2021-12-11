def read_file():
    inputs = {
        "aim" : 0,
        "depth" : 0,
        "horizontal" : 0
    }
    f = open("commands.txt", "r")
    content=f.readlines()
    for line in content:
        command = line.split()
        if command[0] == "forward":
            inputs["horizontal"] += int(command[1])
            inputs["depth"] += inputs["aim"] * int(command[1])
        elif command[0] == "down":
            inputs["aim"] += int(command[1])
        else:
            inputs["aim"] -= int(command[1])
    return inputs

def main():
    inputs = read_file()
    print(inputs,inputs["depth"]*inputs["horizontal"])

if __name__ == "__main__":
    main()