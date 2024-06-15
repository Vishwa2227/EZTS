S=input()
dic={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in S:
    if i=='a' or i=='A':
        dic['a']+=1
    elif i=='e' or i=='E':
        dic['e']+=1
    elif i=='i' or i=='I':
        dic['i']+=1
    elif i=='o' or i=='O':
        dic['o']+=1
    elif i=='u' or i=='U':
        dic['u']+=1    
x=max(dic.values())
print(dic.items())