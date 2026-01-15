USSD Orange Money - Simulation Python
Description

Ce projet est une simulation d’Orange Money en ligne de commande.
Il permet de gérer un compte, effectuer des transferts, acheter du crédit ou des forfaits, et annuler le dernier transfert.
Toutes les données sont sauvegardées dans des fichiers JSON pour conserver l’historique entre les sessions.

Fonctionnalités

Consulter le solde du compte (protégé par code secret, 3 tentatives maximum)

Acheter du crédit pour son propre numéro ou pour un autre numéro

Acheter des forfaits Internet (100 Mo, 500 Mo, 1 Go)

Effectuer un transfert national ou international

Chaque transfert a un statut : VALIDE ou ANNULE

Annuler uniquement le dernier transfert effectué

Consulter l’historique des transactions
quitter le programme

Fichiers utilisés

dictionnaire.json : informations du compte (solde, code secret)

dictionnaire_transfert.json : historique des transferts



Utilisation

Installer Python 3.x

Lancer le script :

python3 main.py


Composer le code USSD #144# pour accéder au menu principal.

Suivre les options du menu : consulter le solde, acheter du crédit ou forfait, effectuer ou annuler un transfert, afficher l’historique.

Saisir le code secret lorsque demandé pour valider les opérations.

Remarques

Seul le dernier transfert peut être annulé.

Les transferts annulés restent dans l’historique avec le statut ANNULE.

Chaque opération modifiant le solde est automatiquement sauvegardée dans les fichiers JSON.