def read_file():
    f = open("crabs.txt", "r")
    content=f.readlines()
    for line in content:
        crabs = [int(x) for x in line.split(",")]
    return crabs

def optimal_radius_P1(crabs):
    crabs.sort()
    horizontal_position = []
    horizontal_position.append(crabs[int(len(crabs)/2)]) if len(crabs)%2 == 1 else horizontal_position.extend([crabs[int((len(crabs)-1)/2)],crabs[int((len(crabs)-1)/2)+1]]) 
    return horizontal_position

def compute_fuel_used_P1(crabs,horizontal_position):
    total_fuel = []
    for k in range(len(horizontal_position)):
        k_total_fuel = 0
        for i in range(len(crabs)):
            k_total_fuel += abs(crabs[i] - horizontal_position[k])
        total_fuel.append(k_total_fuel)
    total_fuel.sort()
    print("Fuel needed is",total_fuel[0])

def optimal_radius_P2(crabs):
    import math

    crabs.sort()
    horizontal_position = [math.floor(sum(crabs)/len(crabs)),math.ceil(sum(crabs)/len(crabs))]
    
    return horizontal_position

def compute_fuel_used_P2(crabs,horizontal_position):
    total_fuel = []
    for k in range(len(horizontal_position)):
        k_total_fuel = 0
        for i in range(len(crabs)):
            k_total_fuel += triangular_sequence(abs(crabs[i] - horizontal_position[k]))
        total_fuel.append(k_total_fuel)
    total_fuel.sort()
    print("Fuel needed is",total_fuel[0])

def triangular_sequence(interval):
    return int((interval*(interval+1))/2)

def P1():
    crabs = read_file()
    horizontal_position = optimal_radius_P1(crabs)
    compute_fuel_used_P1(crabs,horizontal_position)

def P2():
    crabs = read_file()
    horizontal_position = optimal_radius_P2(crabs)
    compute_fuel_used_P2(crabs,horizontal_position)
    print(crabs)
    print(len(horizontal_position))
    print(horizontal_position)

if __name__ == "__main__":
    #P1()
    P2()