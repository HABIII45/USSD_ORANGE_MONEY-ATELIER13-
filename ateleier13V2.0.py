import re
liste=[]
dictionnaire={'solde':20000,'code_secret':123} 
liste.append(dictionnaire)
def code_om():
     
    nbre_tentative=0
    while nbre_tentative < 3:
      
       code_secret_saisi=int(input("saisir votre code secret :"))
     
       nbre_tentative+=1
       if code_secret_saisi==dictionnaire['code_secret']:
         print()
      
         break
      
       else:
          print("saisir un code valide")
def naviguation():
    while True:
     print("9.precedent")
     print("0.quitter")
     choice=input("voulez vous quitter ou retourner sur le menu principal?")
     if choice=="9":
       menu_principal()
     
     elif choice=="0":
       print("merci et a bientot")
     break 
def debiter_compte(montant):
    if montant <= dictionnaire['solde']:
        dictionnaire['solde'] -= montant
        return True
    else:
        print("Solde insuffisant")
        return False
def annuler_transfert(montant_transfert):
   
   print("faire votre choix 1 ou 2")
   print("1.annuler le transfert")
   print("2.QUITTER")
   choix_menu=input("choisir 1 ou 2: ")
   if choix_menu=="2":
      menu_principal()
   elif choix_menu=="1":
      code_om()
   dictionnaire['solde'] +=montant_transfert
   print("transfert annuler voici le solde de votre compte omoney: ",liste[0]["solde"])

 
  
  
              
        
        
def consulter_solde():
  
    print("consultation du solde de votre compte O_Money")
    code_om()
    print(f"voici le montant de votre compte", liste[0]['solde'],"cfa") 
    return
    
 
   

def achat_credit():
   while True:
    print("Veuillez choisir une option")
    print("1.acheter du credit sur mon numero")
    print("2.acheter du credit sur un autre numero")
    choix_credit=input("choisir 1 ou 2: ")
    if choix_credit=="1":
       code_om()
       while True:
        montant_credit=input("Veuillez saisir le montant: ")
        if montant_credit.isnumeric() :
          montant_credit=int(montant_credit)
          break
        else:
          print("veuillez saisir que des chiffres ")
       if debiter_compte(montant_credit):
         dict_achat={"choix_credit":choix_credit,"montant_credit":montant_credit}
         liste.append(dict_achat)  
         print(f"Rechargement reussi pour le montant de: " ,liste[1]['montant_credit'], "cfa sur  votre numero")
        
         print("Opération réussie")
         break
       else:
         print("Opération annulée")
         
        
       
       
   
       
       
           
    elif choix_credit=="2":
         code_om()
         while True:
          num_credit=input("Veuillez saisir le numero destinataire: ")
          if re.fullmatch(r'(77|78)[0-9]{7}', num_credit):
             num_credit=int(num_credit)
             break
          else:
            print("veuillez saisir que des chiffres")
         while True:
          montant_credit=input("saisir le montant à tranférer")
         
          if montant_credit.isnumeric() :
             montant_credit=int(montant_credit)
             
             if debiter_compte(montant_credit):
              dict_achat={"choix_credit":choix_credit,"num_credit":num_credit,"montant_credit":montant_credit}
              liste.append(dict_achat)  
              print(f"Rechargement reussi pour un montant de : " ,liste[1]['montant_credit'], " cfa sur le ",liste[1]['num_credit'])
        
             print("Opération réussie")
             break
          else:
           print("Opération annulée")
          break
    else:
        print("choix indisponible")
   
   return liste
 
  
#achat_credit()
def transfert():
  while True:
    print("Veuillez choisir une option")
    print("1.national")
    print("2.international")
    
   
    choix_tranfert=input("choisir 1 ou 2 ")
    if choix_tranfert=="1":
       code_om()
       while True:
        num_transfert=input("Veuillez saisir un numero avec un indicatif du senegal(+221): ")
        if re.fullmatch(r'(77|78)[0-9]{7}', num_transfert):
          num_transfert=int(num_transfert)
          
          break
        else:
          print("veuillez saisir que des chiffres et un numero de telephone valide")
       while True:
          montant_transfert=int(input("saisir le montant à tranférer"))
        
         
        
       
          if debiter_compte(montant_transfert):
             dict_transfert={"choix_transfert":choix_tranfert,"montant_transfert":montant_transfert,"num_transfert":num_transfert}
             liste.append(dict_transfert)  
             print(f"Transfert sur le  ",liste[1]["num_transfert"],"pour le montant de: ",liste[1]["montant_transfert"],"nouveau motant: ",liste[0]["solde"])
        
        
          print("Opération réussie")
          
      
      
            
      
            
        
      
         
          if annuler_transfert(montant_transfert):
           dict_transfert={"choix_transfert":choix_tranfert,"montant_transfert":montant_transfert,"num_transfert":num_transfert}
           liste.append(dict_transfert)  
           print(f"Transfert sur le  ",liste[1]["num_transfert"]," annulé pour le montant de: ",liste[1]["montant_transfert"],"nouveau solde: ",liste[0]["solde"])
        
          break
    elif choix_tranfert=="2":
         code_om()
         while True:
          num_transfert=input("Veuillez saisir un numero avec un indicatif du mali(+223),du niger(): ")
          if re.fullmatch(r'(+223|+227)', num_transfert):
             num_transfert=int(num_transfert)
             break
          else:
           print("veuillez saisir que des chiffres")
           if debiter_compte(montant_transfert):
              dict_transfert={"choix_transfert":choix_tranfert,"montant_credit":montant_transfert}
              liste.append(dict_transfert)  
              print(f"Transfert sur le  ",liste[1]["num_transfert"],"pour le montant de: ",liste[1]["montant_transfert"])
        
        
              print("Opération réussie")
           
              
              break
              
           else:
            print("Opération annulée")
           break
        
         while True:
          montant_transfert=int(input("saisir le montant à tranférer"))
          if debiter_compte(montant_transfert):
              dict_transfert={"choix_transfert":choix_tranfert,"montant_transfert":montant_transfert}
              liste.append(dict_transfert)  
              print(f"Transfert sur le  ",liste[1]["num_transfert"],"pour le montant de: ",liste[1]["montant_transfert"])
        
              print("Opération réussie")
              break
          else:
            print("Opération annulée")
        
          
   
      
         if annuler_transfert(montant_transfert):
             dict_transfert={"choix_transfert":choix_tranfert,"montant_transfert":montant_transfert,"num_transfert":num_transfert}
             liste.append(dict_transfert)  
             print(f"Transfert sur le  ",liste[1]["num_transfert"]," annulé pour le montant de: ",liste[1]["montant_transfert"],"nouveau solde: ",liste[0]["solde"])
             break
    elif choix_tranfert=="3":
       print("aucun montant envoyer,une annulation ne peut etre effectuer")  
         
         
       
    break
    
  return liste
         
 
    
  
   
   #return liste

def achat_forfait():
  
  while True:
    print("faire un choix de forfait")
    print("1.Pass 100 Mo – 500 F")
    print("2.Pass 500 Mo – 1 000 F")
    print("3.Pass 1 Go – 2 000 F")
    choix_forfait=input("choisir votre forfait: ")
    if choix_forfait=="1":
      
       code_om()
       montant_forfait=500
       if debiter_compte(montant_forfait):
              dict_forfait={"choix_forfait":choix_forfait,"montant_forfait":montant_forfait}
              liste.append(dict_forfait)  
              print(liste)
        
              print("Opération réussie")
              break
       else:
            print("Opération annulée")
    if choix_forfait=="2":
         code_om()
      
         montant_forfait=1000
         if debiter_compte(montant_forfait):
              dict_forfait={"choix_forfait":choix_forfait,"montant_forfait":montant_forfait}
              liste.append(dict_forfait)  
              print(liste)
        
              print("Opération réussie")
              break
         else:
            print("Opération annulée")
    if choix_forfait=="3":
         code_om()
      
         montant_forfait=2000
         if debiter_compte(montant_forfait):
              dict_forfait={"choix_forfait":choix_forfait,"montant_forfait":montant_forfait}
              liste.append(dict_forfait)  
              print(liste)
        
              print("Opération réussie")
              break
         else:
            print("Opération annulée")
    break
  return liste
     
def menu_principal():
    print("Bienvenue sur le service Orange Money")
    print("1. Consulter votre solde")
    print("2. Acheter du crédit")
    print("3. Effectuer un transfert")
    print("4. Annuler un transfert")
    choix_fait = input("Saisir votre choix : ")

    if choix_fait == "1":
        consulter_solde()
        naviguation()
    elif choix_fait == "2":
        achat_credit()
        naviguation()
    elif choix_fait == "3":
        transfert()
        naviguation()
    elif choix_fait=="4":
       annuler_transfert(liste[1]["montant_transfert"])
    else:
        print("Choix indisponible")
         
   
def main():
    print("=*=*=*=* USSD ORANGE MONEY =*=*=*=*=")
    print("Composer #144# pour accéder au service")

    while True:
        option = input("")

        if option == "#144#":
            menu_principal()
            break
        else:
            print("Code USSD invalide")

main()

