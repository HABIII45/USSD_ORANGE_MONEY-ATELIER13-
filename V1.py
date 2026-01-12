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
     print("9.accueil")
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
      
       while True:
        montant_credit=input("Veuillez saisir le montant: ")
        code_om()
        if montant_credit.isnumeric() :
          montant_credit=int(montant_credit)
          break
        else:
          print("veuillez saisir que des chiffres ")
       if debiter_compte(montant_credit):
         dict_achat={"choix_credit":choix_credit,"montant_credit":montant_credit}
         liste.append(dict_achat)  
         print(f"Rechargement reussi pour le montant de: " ,liste[1]['montant_credit'], "cfa sur  votre numero")
        
        
         break
       else:
         print("Opération annulée")
        
        
       
       
   
       
       
           
    elif choix_credit=="2":
         
         while True:
          num_credit=input("Veuillez saisir le numero destinataire: ")
          if re.fullmatch(r'(77|78)[0-9]{7}', num_credit):
             num_credit=int(num_credit)
             break
          else:
            print("veuillez saisir que des chiffres")
         while True:
          montant_credit=input("saisir le montant")
          code_om()
          if montant_credit.isnumeric() :
             montant_credit=int(montant_credit)
             
             if debiter_compte(montant_credit):
              dict_achat={"choix_credit":choix_credit,"num_credit":num_credit,"montant_credit":montant_credit}
              liste.append(dict_achat)  
              print(f"Rechargement reussi pour un montant de : " ,liste[1]['montant_credit'], " cfa sur le ",liste[1]['num_credit'])
        
             
             break
          else:
           print("Opération annulée")
   
          break
    else:
        print("choix indisponible")
   
   #return liste
 
  
#achat_credit()
def transfert():
  while True:
    print("Veuillez choisir une option")
    print("1.national")
    print("2.international")
    choix_tranfert=input("choisir 1 ou 2: ")
    if choix_tranfert=="1":
       code_om()
       while True:
        num_transfert=input("Veuillez saisir un numero avec  du senegal: ")
        if re.fullmatch(r'(77|78)[0-9]{7}', num_transfert):
            num_transfert = int(num_transfert)
            print("Numero valide")
            break
        else:
          print("veuillez saisir que des chiffres et un numero de telephone valide")
       while True:
          montant_transfert=int(input("saisir le montant à tranférer"))
        
         
        
       
          if debiter_compte(montant_transfert):
             dict_transfert={"choix_credit":choix_tranfert,"montant_transfert":montant_transfert,"num_transfert":num_transfert}
             liste.append(dict_transfert)  
             print(f"Transfert sur le  ",liste[1]["num_transfert"],"pour le montant de: ",liste[1]["montant_transfert"])
        
          print("Opération réussie")
    
      
            
      
            
        
      
       break     
    elif choix_tranfert=="2":
         code_om()
         while True:
          num_transfert=input("Veuillez saisir le numero du beneficiaire avec un indicatif du mali(+223),du niger(+227): ")
          if re.fullmatch(r'(+223|+227)', num_transfert):
            num_transfert = int(num_transfert)
            print("Numero valide")
            break
          else:
           print("veuillez saisir que des chiffres")
           if debiter_compte(montant_transfert):
              dict_transfert={"choix_credit":choix_tranfert,"montant_credit":montant_transfert}
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
              dict_achat={"choix_credit":choix_tranfert,"montant_credit":montant_transfert}
              liste.append(dict_achat)  
              print(f"Transfert sur le  ",liste[1]["num_transfert"],"pour le montant de: ",liste[1]["montant_transfert"])
        
              print("Opération réussie")
              break
          else:
            print("Opération annulée")
            break
         
     
    
   #return liste
   
def menu_principal():
    print("Bienvenue sur le service Orange Money")
    print("1. Consulter votre solde")
    print("2. Acheter du crédit")
    print("3. Effectuer un transfert")

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
    else:
        print("Choix indisponible")
         
   
def main():
    print("=*=*=*=* USSD ORANGE MONEY =*=*=*=*=")
    print("Composer #144# pour accéder au service")

    while True:
        option = input("Faire votre choix : ")

        if option == "#144#":
            menu_principal()
            break
        else:
            print("Code USSD invalide")

main()

