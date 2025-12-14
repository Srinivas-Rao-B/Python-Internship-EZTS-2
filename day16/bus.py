import math

stops=["th","ga","ic","ha","te","lu","ni","ca"]
path=[800,600,750,900,1400,1200,1100,1500]
cost_per_m=5/1000
def getFare(source,dest):
    starts=stops.index(source)
    end=stops.index(dest)
    if starts==end:
        return "invalid input"
    total_dist=0
    i=starts
    while i!=end:
        if i>=len(stops):
            i=0
        total_dist+=path[i]
        i+=1
    cost=math.ceil(total_dist*cost_per_m)
    return cost
source=input("enter the source stop :").lower()
dest = input("enter the destination stop :").lower()
fare = getFare(source, dest)
print("Fare:", fare)