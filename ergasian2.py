eis=input("Δηλώστε το όνομα ή την διαδρομή του αρχείου: " )
fo=open(eis,"r", encoding="utf8",)
keim=fo.read().rstrip("\n")
spakeim=keim.split()
for epan in range(len(spakeim)):#epan:epanalipsi
  leks=spakeim[epan]
  spaleks=list(leks)#leks:leksh  spaleks:spasmenh leksh
  badl=["f","c","k","r"] 
  goodl=["b","d","g","h","j","l","m","n","p","q","s","t","v","w","x","z"]
  bad=0
  good=0
  ss=False
  for epan2 in range(len(spaleks)):
    for epan3 in badl:
      if spaleks[epan2]==epan3:#Μετρηση κακων γραμματων
        bad=bad + 1
    for epan3 in goodl:
      if spaleks[epan2]==epan3:#Μετρηση καλων γραμματων
        good=good + 1
  spakeim[epan]=""
  for epan2 in spaleks:
    spakeim[epan] += epan2
  if bad>good:
    symp="Κακή"#symp:symperasma
  else:
    symp="Καλή"
  print (spakeim[epan]+":"+symp)
  fo.close
  
