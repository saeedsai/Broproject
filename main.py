#This is my comments
"""This is 
more comments"""
x=5
y=[11,4,3,22,5,0]
c1= ["keshmesh","saeed"]
import random

print("start of program")
#print(y)
c1[1] = "amir"
c1.insert(2,"saeed")
c1.append("jigar")
c1.extend(["saeed","saeed"])
c1.remove("saeed")
c1.pop(4)
del c1[2]
c1.sort(reverse = True)


def sortingfun(n):
    return abs(n*n - 50)

def myfun():
    if (x>2 and c1[0] and ("saeed" in c1)):
       
        global z 
        z="ZZZ"
        print("length: "+str(len(c1))+" | "+" | random = "+ str(random.randrange(1, 10))+" "+c1[1])
        y.sort(key = sortingfun)
        print(y)
        #print(bin(x))
        #print(bin(x<<2))
        #print(type(bin(x<<2)))
        return True
    else:
        return False

#myfun()
"""
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
    """

"""quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1} \xaa."
print(myorder.format(quantity, itemno, price))"""
#txt = "\x48\x65\x6c\x6c\x6f \f"
print(c1)
print(myfun()) 
m =list(y)
print(m)
y.sort() 
print(m)
print("program ends here")

