eis=input("Δηλώστε το όνομα ή την διαδρομή του αρχείου: " )
fo=open(eis,"r", encoding="utf8",)
keim=fo.read().rstrip("\n")
lista=keim.split()#lista: το κειμενο χωρισμενο σε μορφη λιστας
for ep in range(len(lista)):#μια επαναληψη για καθε καμματι της λιστας
  if len(lista[ep])>3:
    temp1=lista[ep]#temp1:λεξη
    temp2=temp1[0]#temp2:πρωτο γραμμα της λεξης
    sl=len(temp1)
    temp1=temp1[1:sl]#Χρησιμοποιω slicing για να "κοψω" τον πρωτο χαρακτηρα της λεξης
    temp1=temp1 + temp2 + "ay"
    print(temp1)
fo.close
