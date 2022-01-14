import math

infile="mydata.dat"
outfile="myout.dat"

def f(y):
  if y >= 0.0:
    return y**5*math.exp(-y)
  else:
    return 0.0

indata=open(infile, "r")
linee=indata.readlines()
indata.close()
letti=[]
x=[]
for n in linee:
  valori= n.split()
  x.append(float(valori[0]));
  y= float(valori[1])
  letti.append(f(y))

outdata= open(outfile, "w")
i=0
for n in letti:
  outdata.write('%g %12.5e\n' %(x[i],n))
  i+=1
outdata.close()