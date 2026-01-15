import re
import json
liste=[]
achats_credit = []
achats_forfait = []
transferts = []
dernier_transfert =None

import json

dictionnaire = {}




    
def charger_donnees():
    global dictionnaire
    try:
        with open("dictionnaire.json", "r") as f:
            dictionnaire = json.load(f)
    except FileNotFoundError:
        dictionnaire = {'solde': 20000, 'code_secret': 123}
        mise_a_jour()



   
         
       

def mise_a_jour():
    with open("dictionnaire.json", "w") as f:
        json.dump(dictionnaire, f, indent=4)


   
liste.append(dictionnaire)


def dernier_montant_transfert():
    try:
        with open("dictionnaire_transfert.json", "r") as f:
            transferts = json.load(f)
            return transferts[-1]['montant']
    except (FileNotFoundError, IndexError):
        return 0

def mise_a_jour_transfert():
    with open("dictionnaire_transfert.json", "w") as f:
        json.dump(transferts, f, indent=4)

try:
 with open("dictionnaire_transfert.json","r") as f:
   transferts=json.load(f)
except FileNotFoundError:
   mise_a_jour_transfert()  
     
def mise_a_jour_credit():
   with open("dictionnaire_achat_credit.json","w") as f:
    json.dump(achats_credit,f,indent=4)
    
try:
 with open("dictionnaire_achat_credit.json","r") as f:
   achats_credit=json.load(f)
except FileNotFoundError:
   mise_a_jour_credit()
       
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
    global dictionnaire
    if montant <= dictionnaire['solde']:
        dictionnaire['solde'] -= montant
        mise_a_jour()
        return True
    else:
        print("Solde insuffisant")
        return False
    
   
def annuler_transfert():
    global dictionnaire, transferts

    if not transferts:
        print("Aucun transfert à annuler")
        return

    dernier = transferts[-1]   

    if dernier['statut'] == "ANNULE":
        print("Ce transfert est déjà annulé")
        return

    code_om()

    dernier['statut'] = "ANNULE"
    dictionnaire['solde'] += dernier['montant']

    mise_a_jour()
    mise_a_jour_transfert()

    print("Transfert annulé")
    print("Nouveau solde :", dictionnaire['solde'])

              
        
        
def consulter_solde():
  
    print("consultation du solde de votre compte O_Money")
    code_om()
    print("Solde :", dictionnaire['solde'], "CFA")

    return
    
 
    

   
   

   

def achat_credit():
   global achats_credit
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
             achat = {
            "type": "credit",
            "destinataire": "774663451",
            "montant": montant_credit
            }
       achats_credit.append(achat)  
       mise_a_jour_credit()

          
       print(achats_credit)
       

       print("Rechargement réussi")
       print("Montant :", montant_credit, "CFA")

       break
    
         
        
      
       
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
              achat = {
                "type": "credit",
                "destinataire": num_credit,
                "montant": montant_credit
               }
              
   
              
             achats_credit.append(achat)  
             mise_a_jour_credit()
             print("Rechargement réussi")
             print("Numéro :", num_credit)
             print("Montant :", montant_credit, "CFA")
             print("Opération réussie")
             break
          else:
           print("Opération annulée")
          break
         break
    else:
        print("choix indisponible")
   
   return liste
 
  
#achat_credit()
def transfert():
  global dernier_transfert
 
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
            dernier_transfert = {
                "type": "national",
                "montant": montant_transfert,
                "numero": num_transfert,
                 "statut": "VALIDE"
            }
          transferts.append(dernier_transfert)
            
          mise_a_jour_transfert()
          
         
          print("Opération réussie")
          
      
      
            
      
            
        
      
         
          
           
          break
    elif choix_tranfert=="2":
         code_om()
         while True:
          num_transfert=input("Veuillez saisir un numero avec un indicatif du mali(+223),du niger(): ")
          if num_transfert.isnumeric():
             num_transfert=int(num_transfert)
             
          else:
           print("veuillez saisir que des chiffres")
           
         
        
         
          montant_transfert=int(input("saisir le montant à tranférer"))
          if debiter_compte(montant_transfert):
            dernier_transfert = {
                "type": "international",
                "montant": montant_transfert,
                "numero": num_transfert,
                 "statut": "VALIDE"
                
               }
            transferts.append(dernier_transfert)
            
            mise_a_jour_transfert()
            mise_a_jour()
            
            break
          else:
            print("Opération annulée")
        
          
   
      
         
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
             forfait = {
            "type": "forfait-500",
            "destinataire": "774663451",
            "montant": montant_forfait
            }
             achats_forfait.append(forfait)
       
        
       print("Opération réussie")
       break
    else:
            print("Opération annulée")
    if choix_forfait=="2":
         code_om()
      
         montant_forfait=1000
         if debiter_compte(montant_forfait):
             forfait = {
            "type": "forfait-1000",
            "destinataire": "774663451",
            "montant": montant_forfait
            }
             achats_forfait.append(forfait)
       
        
         print("Opération réussie")
         break
    else:
            print("Opération annulée")
    if choix_forfait=="3":
         code_om()
      
         montant_forfait=2000
         if debiter_compte(montant_forfait):
             forfait = {
            "type": "forfait-500",
            "destinataire": "774663451",
            "montant": montant_forfait
            }
             achats_forfait.append(forfait)
       
         print("Opération réussie")
         break
    else:
            print("Opération annulée")
    break
  return liste
charger_donnees()    
def menu_principal():
    print("Bienvenue sur le service Orange Money")
    print("1. Consulter votre solde")
    print("2. Acheter du crédit")
    print("3. Effectuer un transfert")
    print("4. Annuler un transfert")
    print("5.afficher l historique des transactions")
    print("6.quitter")
    choix_fait = input("Saisir votre choix : ")

    if choix_fait == "1":
        consulter_solde()
        
        naviguation()
    elif choix_fait == "2":
        mise_a_jour_credit()
        achat_credit()
        mise_a_jour()
        
        naviguation()
       
    elif choix_fait == "3":
        transfert()
       
        naviguation()
        
    elif choix_fait=="4":
       
       annuler_transfert()
      
       mise_a_jour_transfert()
      
    elif choix_fait=="5":
       for i in transferts:
          print("type de transaction:",i['type'],",montant de la transaction:",i['montant'],",numero tel:",i['numero'])
    elif choix_fait=="6":
       print("merci!a bientot")   
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

