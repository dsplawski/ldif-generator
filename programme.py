# -*- coding:Utf-8 -*-
"""A generator of LDIF contact files for Mozilla Thunderbird"""
__author__ = "David SPLAWSKI <splawski.david@gmail.com>"
__version__ = "0.2"

import sys
from contact import Contact
from BaseMySQL import BaseMySQL, GestionBD, Sauvegarde


def main():
# Création de l'objet-interface avec la base de données
    bd = GestionBD(BaseMySQL.dbName, BaseMySQL.user, 
                    BaseMySQL.passwd, BaseMySQL.host)
    if bd.echec:
        sys.exit()
    while 1:
        print "\nQue voulez-vous faire :\n"\
          "1) Créer les tables de la base de données\n"\
          "2) Supprimer les tables de la base de données ?\n"\
          "3) Entrer des employés\n"\
          "4) Lister des employés\n"\
          "5) Exécuter une requête SQL quelconque\n"\
          "6) Enregister sous format ldif\n"\
          "7) Terminer ?                         Votre choix :",
        ch = int(raw_input())
        if ch == 1:
            # création de toutes les tables décrites dans le dictionnaire
            bd.creerTables(BaseMySQL.dicoT)
        elif ch == 2:
            # suppression de toutes les tables décrites dans le dic.
            bd.supprimerTables(BaseMySQL.dicoT)
        elif ch == 3:
        # création d'un <enregistreur> d'employés
            table = {3: 'employes'}[ch]
            enreg = Sauvegarde(bd, table)
            while 1:
                if enreg.save():
                    break
        elif ch == 4:
            # liste de tous les employés
            table = {4: 'employes'}[ch]
            if bd.executerReq("SELECT * FROM %s" % table):
                # analyser le résultat de la requête ci-dessus :
                records = bd.resultatReq()      # ce sera un tuple de tuples
                for rec in records:             # => chaque enregistrement
                    for item in rec:            # => chaque champ dans l'enreg.
                        print item,
                    print
        elif ch == 5:
            req = raw_input("Entrez la requête SQL : ")
            if bd.executerReq(req):
                print bd.resultatReq()          # ce sera un tuple de tuples
        elif ch == 6:
            fic = raw_input('Enter filename to process: ')
            ofi = open(fic, "w")
            contact = Contact()
            table = {6: 'employes'}[ch]
            if bd.executerReq("SELECT * FROM %s" % table):
                # analyser le résultat de la requête ci-dessus :
                records = bd.resultatReq()      # ce sera un tuple de tuples
                for rec in records:             # => chaque enregistrement
                    contact = Contact(*rec[1:])
                    ofi.write(contact.get-contact_ldif())
                ofi.close()
        else:
            bd.commit()
            bd.close()
            break

if __name__ == '__main__':
    main()
