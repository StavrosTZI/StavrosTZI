eis=input("Δηλώστε το όνομα ή την διαδρομή του αρχείου: " )
with open(eis,"r+") as keim:
  spakeim=keim.split()#spasmeno keimeno
for epan in range(len(spakeim)):#epanalipsi
  leks=spakeim[epan]
  spaleks=list(leks)#leksi  spasmenh leksh
  badl=["f","c","k","r"] 
  goodl=["b","d","g","h","j","l","m","n","p","q","s","t","v","w","x","z"]
  bad=0
  good=0
  ss=False
  for epan2 in range(len(spaleks)):
    for epan3 in badl:
      if spaleks[epan2]==epan3:
        bad=bad + 1
        ss=True
    if ss==False:
      for epan3 in goodl:
        if spaleks[epan2]==epan3:
          good=good + 1
  spakeim[epan]=""
  for epan2 in spaleks:
    spakeim[epan] += epan2
  if bad>good:
    symp="Καλή"#symperasma
  else:
    symp="Κακή"
  print (spakeim[epan]+":"+symp)
