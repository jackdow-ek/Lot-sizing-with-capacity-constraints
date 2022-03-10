def calculate_cost(setupcost, holdingcost, listlength, solutionlist, demandlist):
    # calculating total costs for solution
    total_setup_cost = setupcost * float(listlength - solutionlist.count(0))
    total_hold_cost = 0.0
    previous_value = 0.0
    print("total setup cost =", total_setup_cost)
    #  r' compare to r
    for i in range(0, listlength - 1):
        total_hold_cost = total_hold_cost + float(solutionlist[i] - demandlist[i])
        previous_value = previous_value + total_hold_cost
    total_hold_cost = previous_value * holdingcost
    print("total holding cost =", total_hold_cost)
    total_cost = total_setup_cost + total_hold_cost
    print("total COST =", total_cost, "\n")

gap = "----------------------------------------------"
# number of elements as input
list_length = int(input(gap + "\nEnter size of Demand/Capacity : "))
demand_list = [0] * list_length
capacity_list = [0] * list_length
# empty list for storing data
solution_list = [0] * list_length

# user enters demand values
print(gap + "\nEnter elements for Demand")

# iterating till the range
for i in range(list_length):
    print("element.", i + 1, "= ", end="")
    demand_list[i] = int(input())  # adding the element

# user enters capacity values
print(gap + "\nEnter elements for Capacity")

for i in range(0, list_length):
    print("element.", i + 1, "= ", end="")
    capacity_list[i] = int(input())  # adding the element

print(gap + "\ndemand =", demand_list)
print("capacity =", capacity_list)

#  checking feasibility
print(gap + "\nChecking Feasibility\n")
total_demand = demand_list[0]
total_capacity = capacity_list[0]
feasible = False

if total_demand <= total_capacity:  # checking for first elements
    print(total_demand, "<", total_capacity)
    feasible = True

if feasible:  # if first elements are suitable then it works
    for i in range(1, list_length):
        # recalculating total values of demand&capacity for next step of loop
        total_demand = total_demand + demand_list[i]
        total_capacity = total_capacity + capacity_list[i]

        if total_demand <= total_capacity:
            print(total_demand, "<", total_capacity)
        else:
            print(total_demand, "!", total_capacity, "NOT FEASIBLE")
            feasible = False
            break  # if input values are not feasible then loop ends
else:  # if first elements are not suitable then it works
    print(total_demand, "!", total_capacity, "NOT FEASIBLE")
    feasible = False

# calculating the solution
if feasible:  # checking value of feasible(variable)
    print("FEASIBLE.\n" + gap)

    exceed = 0
    for i in range(0, list_length):
        if demand_list[i] > capacity_list[i]:
            solution_list[i] = 0  # full capacity
            exceed = demand_list[i] - capacity_list[i]  # the amount that exceeding the capacity is calculated
            for tmp in range(i - 1, -1, -1):  # surplus is carried over to previous periods
                if exceed > solution_list[tmp]:
                    exceed = exceed - solution_list[tmp]
                    solution_list[tmp] = 0  # full capacity
                elif exceed < solution_list[tmp]:
                    solution_list[tmp] = solution_list[tmp] - exceed
                    exceed = 0  # end
        elif demand_list[i] < capacity_list[i]:
            solution_list[i] = capacity_list[i] - demand_list[i]  # it calculates free space in capacity
    for i in range(0, list_length):
        solution_list[i] = capacity_list[i] - solution_list[i]
    print("solution =", solution_list)

    # optimizing the solution
    excess_capacity = [0] * list_length  # empty list for storing data

    # calculating excess capacity
    for i in range(0, list_length):
        excess_capacity[i] = capacity_list[i] - solution_list[i]
        if excess_capacity[i] < 0:
            excess_capacity[i] = 0

    setup_cost = float(input(gap + "\nEnter setup cost   : "))
    holding_cost = float(input("Enter holding cost : "))
    print(gap + "\ncapacity =", capacity_list, "\n")
    print("solution =", solution_list)
    calculate_cost(setup_cost, holding_cost, list_length, solution_list, demand_list)

    for i in range(list_length - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if solution_list[i] < excess_capacity[j] and setup_cost > (
                    holding_cost * float(solution_list[i]) * float(i - j)):
                solution_list[j] = solution_list[i] + solution_list[j]  # shifting a lot
                excess_capacity[j] = excess_capacity[j] - solution_list[i]  # recalculate excess capacity
                solution_list[i] = 0

    print("optimized solution =", solution_list)
    calculate_cost(setup_cost, holding_cost, list_length, solution_list, demand_list)
