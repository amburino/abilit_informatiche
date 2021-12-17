import time


l=[]
print(l)
m=[1,3, "bella", "ciao"]
print(m)
print(m[2],m[3])
###
a=range(4)
b=range(1,30,2)
#for n in a:
 # print(n)
#for n in b:
 # print(n)
#############
l=[1,2]
l2=['a','b']
l3=[4,5]
f=[(e1,e2,e3) for e1 in l for e2 in l2 for e3 in l3]
#print(f)
############
q=list(range(1000000))
s=list(range(1000))
t1=time.process_time()
r=q+s
t2=time.process_time()
print("tempo di esecuzione:", t2-t1)
t3=time.process_time()
q.extend(s)
t4=time.process_time()
print("extend execution time:",t4-t3)
#####
a1=list(range(20))
b1=list(range(12))
a1.extend(b1)
print(a1)
