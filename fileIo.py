f = open('inputFile.txt','r')
p = open('passfile', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)
        p.write(line)
        
        
f.close()
p.close()
