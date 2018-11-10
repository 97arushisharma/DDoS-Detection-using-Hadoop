#!/usr/bin/python3
import sys,ast,math

a=[]
wordcount={}
count=0
S=0
entropy = 0
sd = 0
sd1 = 0

for line in sys.stdin:
    line = line.strip()
    words = line.split("\n")
	
    for ips in words:
        ips = ips.split()
        a.append(ips[2])

for word in a:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    count= count+1
    S=S+v

mean = S/count


for k,v in wordcount.items():
    sd = sd + (v-mean)*(v-mean)


sd1 = math.sqrt(sd/count)    

for k,v in wordcount.items():
    entropy= entropy+ ((v/S)* (math.log(v/S,2)))
print(str(entropy)+"	"+str(sd1))



