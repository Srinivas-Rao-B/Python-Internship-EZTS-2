n = int(input("Enter the number of bulbs: "))
st = []
for i in range(n):
    a = int(input("Enter the state of bulb (0/1): "))
    st.append(a)
l = []
for i in range(n):
    b = int(input("Enter the length: "))
    l.append(b)
total = 0
for i in range(1, n):
    if st[i]==0:
        x = l[i] - l[i - 1]
        total += x
print("The Total length of the cable =", total)