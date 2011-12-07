# -*- coding:Utf-8 -*-
# Project Contacts.ldif


# Function showContact
def showContact(nom, prenom, email):
    print "Nom et prenom du contact : ", prenom, nom, "Email :", email


# Function showContactLDIF
def showContactLDIF(nom, prenom, email):
    "Show contact's informations"
    print "dn: cn=%s %s,mail=%s" % (prenom, nom, email)
    print "objectclass: top"
    print "objectclass: person"
    print "objectclass: organizationalPerson"
    print "objectclass: inetOrgPerson"
    print "objectclass: mozillaAbPersonAlpha"
    print "givenName:", prenom
    print "sn:", nom
    print "cn:", prenom, nom
    print "mail:", email
    print "modifytimestamp: 1323186656"


# Function getData
def getData():
    "Return the informations entered"
    nom = raw_input("Nom : ")
    prenom = raw_input("Prénom : ")
    email = raw_input("Email : ")
    return [nom, prenom, email]


# Function main()

nom, prenom, email = getData()
showContactLDIF(nom, prenom, email)
