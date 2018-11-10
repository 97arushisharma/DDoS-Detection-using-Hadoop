#!/usr/bin/python3
"""reducer.py"""

import sys, ast
import math
from operator import itemgetter

count=0
S=0
entropy=0


'''
# input comes from STDIN
for line in sys.stdin:
    
    line = line.strip()
    line = line.split()
    a.append(line[2])
   
   
#print()

for word in a:
	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1'''
for map_op in sys.stdin:
    #x = ast.literal_eval(wordcount)
    '''
    for k,v in x.items():
        count= count+1
        S=S+v
    for k,v in x.items():
        entropy= entropy+ ((v/S)* (math.log(v/S,2)))
    '''
    '''
    entropy = float(map_op)
    entropy= (-1)*entropy
    Normalized_entropy= (entropy/(math.log(count,2)))
    print(entropy, " ", Normalized_entropy)
    '''
    print(map_op)


    


    
    

                
           
        	
        	 



     
            



    



