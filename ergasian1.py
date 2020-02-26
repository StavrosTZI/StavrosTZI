eis=input("Δηλώστε το όνομα ή την διαδρομή του αρχείου: " )#το προγραμμα δουλευει για κειμενα στα Αγγλικα
fo=open(eis,"r", encoding="utf8",)
keim=fo.read().rstrip("\n")
spkeim=keim.split()
lmax1=lmax2=lmax3=lmax4=lmax5=0#lmax:μηκος μεγιστων
max1=max2=max3=max4=max5="bl"#μεγιστες
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
limax=[max1,max2,max3,max4,max5]#limax:λιστα μεγιστων

for epa in range(5):
  temp=limax[epa]#temp:λεξη
  templi=list(temp)#templi:λιστα με τα γραμματα της λεξης
  tlen=len(temp)#tlen:μεγεθος λεξης
  
  a=e=i=o=u=y=0
  for epa2 in range(tlen):#καθε φωνηεν εχει και μια μεταβλητη int με τον αριθμο που εμφανιζεται 
    x=templi[epa2]#βρισκω ποσες φορες επαναλαμβανεται το καθε φωνηεν 
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
  if a != 0:#αφερω το καθε φωνηεν ξεχωριστα
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
fo.close
  
 
