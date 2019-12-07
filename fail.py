f = open('inputFile.txt','r')
p = open('passfile', 'w')
q = open('fail-list','w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        p.write(line)
    else: 
        q.write(line)
f.close()
p.close()
q.close()
