var=input() #ex rah23ul output:2 (count of digits in strings)
count=0
for i in var:
    if i>='0' and  i<='9':
        count+=1
print(count)