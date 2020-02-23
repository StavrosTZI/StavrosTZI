eis=input("Δηλώστε το όνομα ή την διαδρομή του αρχείου: " )
with open(eis,"r+") as keim:
  spkeim=keim.split()
  lmax1=lmax2=lmax3=lmax4=lmax5=0
  max1=max2=max3=max4=max5="bl"
for epa in range(len(spkeim)):
  if len(spkeim[epa])>lmax1:
    max1=(spkeim[epa])
    lmax1=len(spkeim[epa])
  elif len(spkeim[epa])>lmax2:
    max2=(spkeim[epa])
    lmax2=len(spkeim[epa])
  elif len(spkeim[epa])>lmax3:
    max3=(spkeim[epa])
    lmax3=len(spkeim[epa])
  elif len(spkeim[epa])>lmax4:
    max4=(spkeim[epa])
    lmax4=len(spkeim[epa])
  elif len(spkeim[epa])>lmax5:
    max5=(spkeim[epa])
    lmax5=len(spkeim[epa])
limax=[max1,max2,max3,max4,max5]#limax:listmax

for epa in range(5):
  temp=limax[epa]
  templi=list(temp)
  tlen=len(temp)
  
  a=e=i=o=u=y=0
  for epa2 in range(tlen):#καθε φωνηεν εχει και μια μεταβλητη int με τον αριθμο που εμφανιζεται 
    x=templi[epa2]
    if x=="a":
      a=1+a
    if x=="e":
      e=1+e
    if x=="i":
      i=1+i
    if x=="o":
      o=1+0
    if x=="u":
      u=1+u
    if x=="y":
      y=1+y
  if a != 0:
    for epa2 in range(a):
      templi.remove("a")
  if e != 0:
    for epa2 in range(e):
      templi.remove("e")
  if i != 0:
    for epa2 in range(i):
      templi.remove("i")
  if o != 0:
    for epa2 in range(o):
      templi.remove("o")
  if u != 0:
    for epa2 in range(u):
      templi.remove("u")
  if y != 0:
    for epa2 in range(y):
      templi.remove("y")
  templi.reverse()
  limax[epa]=""
  for epa2 in templi:
    limax[epa] += epa2
print(limax)
  
 