trainees=3
rounds=3
oxygen=[[0]*trainees for _ in range(rounds)]
print("Enter oxygen values(Range 0-100):")
for i in range(rounds):
    print(f"Round {i+1}:")
    for j in range(trainees):
        value=int(input(f"oxygen value of trainee {j+1}:"))
        if value<0 or value>100:
            print("Invalid input")
            exit()
        oxygen[i][j]=value
average=[]
for j in range(trainees):
    sum=0
    for i in range(rounds):
        sum+=oxygen[i][j]
    avg=sum/rounds
    average.append(avg)
max_avg=max(average)
if max_avg<70:
    print("All trainees are unfit")
else:
    print("\nOutput values:")
    for j in range(trainees):
        if average[j]==max_avg:
            print("Trainee Number:",j+1)
    print("\nHighest avg oxygen level:",max_avg)