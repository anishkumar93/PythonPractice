#python print

"""
Print # in the below format
n=4
wher width = height = n

    #
   ##
  ###
 ####

"""

import sys

n = 4


for a in range(1,n+1):
	print (n-a)*" "+a*"#"

print ("---------------------------------------------------\n\n")
"""stdout.write prints without leading or trailing space"""
for i in range(1,n+1):
    for j in range(i,n):
        sys.stdout.write(" "),
    for k in range(1,i+1):
        sys.stdout.write("#"),
    sys.stdout.write("\n")


print ("---------------------------------------------------\n\n")
"""Print() leaves additional space"""
for i in range(1,n+1):
    for j in range(i,n):
        print(" "),
    for k in range(1,i+1):
        print("#"),
    print("\n")
