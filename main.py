#This is my comments
"""This is 
more comments"""
x=5
y=" Sadegh Kalamat Sade "
c1= 2-1j
import random

print("start of program")
print(y)
def myfun():
    if (x>2):
        y="complex ="
        global z 
        z="ZZZ"
        print("length: "+str(len(y))+" | "+str(c1+x-1j-4.2)+" | random = "+ str(random.randrange(1, 10)))

myfun()

#print(y.strip())
y2= y.split("gh")
#print(y.replace("Sade","Pichide").strip())
print(y2[0][1:3])
print(y2[1])
j = 0
for i in str(y[-4:].upper()):
    j=j+1
    print(i+str(j))

if "Y" in z:
    print("Y is found")
else:
    print("Y is not found")

print("program ends here")
