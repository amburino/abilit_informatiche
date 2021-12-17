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
########
stack=[1,2,3,4]
print("stack iniziale:",stack)
for i in list(range(5,7)):
  stack.append(i)
print("append:",stack)
stack.pop()
print("pop:",stack)
######
queue=["a","b","c","d"]
print("initial queue:", queue)
queue.append("e")
queue.append("f")
print("append:",queue)
queue.pop(0)
print("pop:",queue)
#######
tup1=()
tup2=(35,)
print(tup1,tup2)
print(type(tup1),type(tup2))
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
tup3=(1,2,3,4,5,6,123)
print(type(tup3))
print(len(tup3),max(tup3))
########
a={}
d={1:"Hello",2:"world"}
print(type(d))
print(d[2])
e={'name':"john",1:[2,4,3]}
print(e["name"])
d={"age":28, "name":"Jack"}
print(d["age"])
d["age"]=30
print(d["age"])
f={'name':"john",1:[2,4,3]}
print(f.pop(1))
print(f)
f.clear()
print(f)
#########