eis=input("Δηλώστε το όνομα ή την διαδρομή του αρχείου: " )
with open(eis,"r+") as keim:
  lista=keim.split()#lista: το κειμενο χωρισμενο σε μορφη λιστας
  for ep in range(len(lista)):#μια επαναληψη για καθε καμματι της λιστας
    if len(lista[ep])>3:
      temp1=lista[ep]
      temp2=temp1[0]
      sl=len(temp1)
      temp1=temp1[1:sl]#Χρησιμοποιω slicing για να "κοψω" τον πρωτο χαρακτηρα της λεξης
      temp1=temp1 + temp2 + "ay"
      print(temp1)
