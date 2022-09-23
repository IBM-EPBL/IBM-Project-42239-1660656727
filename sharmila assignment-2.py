import random
a=random.sample(range(30,80),1)
print (a)
b=random.sample(range(30,50),1)
print (b)
if( a >= [50] ):
    print("The temperature is high")
else:
    print("normal")
if( b >= [45] ):
    print("The humidity is high")
else:
    print("normal")
