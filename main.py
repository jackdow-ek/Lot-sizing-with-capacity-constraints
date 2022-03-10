def calculateCost(setupCost, holdingCost, listLength, solutionList, demandList, capacityList):
    #calculating total costs for solution
    totalSetupCost=setupCost*float(listLength-solutionList.count(0))
    totalHoldCost=0.0
    previousValue=0.0
    print("total setup cost =",totalSetupCost)
    #r' compare to r 
    for i in range(0,listLength-1):
        totalHoldCost = totalHoldCost + float(solutionList[i] - demandList[i])
        previousValue=previousValue+totalHoldCost
    totalHoldCost = previousValue*holdingCost
    print("total holding cost =",totalHoldCost)
    totalCost=totalSetupCost+totalHoldCost
    print("total COST =",totalCost,"\n")

# creating an empty lists
demandList = []
capacityList = []
gap = "----------------------------------------------"
# number of elements as input
listLength = int(input(gap+"\nEnter size of Demand/Capacity : "))

#empty list for storing data
solutionList = [None] * listLength

#user enters demand values
print(gap+"\nEnter elements for Demand")

# iterating till the range
tmp = 1
for i in range(0, listLength):
    print("element.",tmp,"= ",end ="")
    element = int(input())
    tmp = tmp + 1
    demandList.append(element) # adding the element

#user enters capacity values
print(gap+"\nEnter elements for Capacity")
tmp = 1
for i in range(0, listLength):
    print("element.",tmp,"= ",end ="")
    element = int(input())
    tmp = tmp + 1
    capacityList.append(element) # adding the element

print(gap+"\ndemand =",demandList)
print("capacity =",capacityList)


#checkin feasibilty
print(gap+"\nChecking Feasibilty\n")
totalDemand = demandList[0]
totalCapacity = capacityList[0]
feasible = False

if(totalDemand<=totalCapacity):#checking first elemnts
    print(totalDemand,"<",totalCapacity)
    feasible = True

if(feasible==True):#if first elements are suitable works
    for i in range(1, listLength):
        #recalculating total values of demand&capacity for next step of loop
        totalDemand = totalDemand + demandList[i]
        totalCapacity = totalCapacity + capacityList[i]
        
        if (totalDemand<totalCapacity):
            print(totalDemand,"<",totalCapacity)
        else:
            print(totalDemand,"!",totalCapacity,"NOT FEASIBLE")
            feasible = False
            break#if input values are not feasible loop ends
else:#if first elements are not suitable works
    print(totalDemand,"!",totalCapacity,"NOT FEASIBLE")
    feasible = False

#calculating solution
if(feasible==True):#checking value of feasible(variable)
    print("FEASIBLE.\n"+gap)
    
    exceed = 0
    for i in range(0, listLength):
        if(demandList[i]>capacityList[i]):
            solutionList[i]=0#full capacity
            exceed=demandList[i]-capacityList[i]#the amount exceeding the capacity is calculated
            for tmp in range(i-1,-1,-1):#surplus is carried over to previous periods
                if(exceed>solutionList[tmp]):
                    exceed = exceed-solutionList[tmp]
                    solutionList[tmp]=0#full capacity
                elif(exceed<solutionList[tmp]):
                    solutionList[tmp]=solutionList[tmp]-exceed
                    exceed = 0#end
        elif(demandList[i]<capacityList[i]):
            solutionList[i]=capacityList[i]-demandList[i]#Calculates free space in capacity
    for i in range(0, listLength):
        solutionList[i]=capacityList[i]-solutionList[i]
    print("solution =",solutionList)
    
    #optimizing the solution
    excess_capacity = [None] * listLength#empty list for storing data
    
    #calculating excess capacity
    for i in range(0,listLength):
        excess_capacity[i]=capacityList[i]-solutionList[i]
        if(excess_capacity[i]<0):
            excess_capacity[i]=0
    
    setupCost = float(input(gap+"\nEnter setup cost   : "))
    holdingCost = float(input("Enter holding cost : "))
    print(gap+"\ncapacity =",capacityList,"\n")
    print("solution =",solutionList)
    calculateCost(setupCost, holdingCost, listLength, solutionList, demandList, capacityList)
    
    
    for i in range(listLength-1,-1,-1):
        for j in range(i-1,-1,-1):
            if(solutionList[i]<excess_capacity[j] and setupCost>(holdingCost*float(solutionList[i])*float(i-j))):
                solutionList[j]=solutionList[i]+solutionList[j]#shifting lot
                excess_capacity[j]=excess_capacity[j]-solutionList[i]#recalculate excess capacity
                solutionList[i]=0
    
    print("optimized solution =",solutionList)
    calculateCost(setupCost, holdingCost, listLength, solutionList, demandList, capacityList)