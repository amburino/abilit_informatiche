import sys

while(True):
  print("inserire un numero intero da 1 a 10")
  par1=input()
  if int(par1) in range(11):
    while(True):
      print("Inserisci una lettera ora fra queste: a,b,c")
      par2=input()
      if par2 in ['a','b','c']:
        print("i due parametri forniti sono: ",par1,par2)
      sys.exit()
  else: print("riprova")
else: print("riprova")  