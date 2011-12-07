# -*- coding:Utf-8 -*-
# Project Contacts.ldif


# Imports
import time


# Function getTimestamp
def getTimestamp():
    "Return timestamp"
    debut = time.time()
    temps = time.localtime(debut)
    timestamp = time.mktime(temps)
    tstamp = int(timestamp)
    return str(tstamp)


# Function showContact
def showContact(nom, prenom, email):
    "Show contact's informations"
    print "Nom et prenom du contact : ", prenom, nom, "Email :", email


# Function showContactLDIF
def showContactLDIF(nom, prenom, email, timestamp):
    "Show contact's informations (format LDIF)"
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
    print "modifytimestamp:", timestamp


# Function getData
def getData():
    "Return the informations entered"
    nom = raw_input("Nom : ")
    prenom = raw_input("Prénom : ")
    email = raw_input("Email : ")
    return [nom, prenom, email]


# Function writeInFile
def writeInFile():
    "Write in a file"
    of = open(nomF, 'a')
    while 1:
        nom, prenom, email = getData()
        timestamp = getTimestamp()
        if nom == '':
            break
        else:
            of.write("dn: cn=%s %s,mail=%s" % (prenom, nom, email) + '\n')
            of.write("objectclass: top" + '\n')
            of.write("objectclass: person" + '\n')
            of.write("objectclass: organizationalPerson" + '\n')
            of.write("objectclass: inetOrgPerson" + '\n')
            of.write("objectclass: mozillaAbPersonAlpha" + '\n')
            of.write("givenName:" + prenom + '\n')
            of.write("sn:" + nom + '\n')
            of.write("cn:" + prenom + " " + nom + '\n')
            of.write("mail:" + email + '\n')
            of.write("modifytimestamp: " + timestamp + '\n\n')
    of.close()


# Function readInFile
def readInFile():
    "Read in a file"
    of = open(nomF, 'r')
    while 1:
        ligne = of.readline()
        if ligne == "":
            break
        print ligne
    of.close()


# Function main()

nomF = raw_input('Nom du fichier à traiter : ')
choix = raw_input('Entrez "e" pour écrire, "c" pour consulter les données : ')

if choix == 'e':
    writeInFile()
else:
    readInFile()
