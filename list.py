'''v = []
for i in range(6):
    i = input("Enter:")
    v.append(i)
print(v)
m_c=max(v.count(x) for x in set(v))
print(m_c)
m_e=[x for x in set(v) if v.count(x)]
print(m_e)'''

p = int(input("No of parties:"))
v = []
for i in range(0,7):
    print("1.q")
    print("2.w")
    print("3.e")
    print("4.r")
    print("5.t")
    print("6.y")
    e = input("Enter the vote for whom do u want:")
    v.append(e)
    print(v)
max_count = max(v.count(x) for x in set(v))
print(max_count)
max_val = [x for x in set(v) if v.count(x) == max_count]
print(max_val)