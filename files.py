with open("file.txt",'w') as f:
    f.write("iam")
    f.close()
    
with open("file.txt",'r') as f:
    print(f.read())
    f.close()

with open("file.txt",'a') as f:
    f.write('''charan''')
    f.close()

with open("file.txt",'r') as f:
    s=f.read()
    print(s)
    f.close()

s=s.replace("Bellary","BITM")
with open("file.txt",'a') as f:
    f.write(s)
    f.close()

with open("file.txt",'a') as f:
    print(f.tell())
    f.close()

with open("file.txt",'w') as f:
    print(f.tell())
    
    f.seek(10)
    f.write("#")
    f.close()
