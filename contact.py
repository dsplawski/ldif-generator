# -*- coding:Utf-8 -*-
"""A generator of LDIF contact files for Mozilla Thunderbird"""
__author__ = "David SPLAWSKI <splawski.david@gmail.com>"
__version__ = "0.2"

import time


def getTimestamp():
    "Return timestamp"
    timestamp = int(time.time())
    return "%d" % timestamp


def showContact(last_name, first_name, email):
    "Show contact's informations"
    print "First name and last name:", first_name, last_name, "E-mail:", email


def showContactLDIF(last_name, first_name, email, timestamp):
    "Show contact's informations (format LDIF)"
    print "dn: cn=%s %s,mail=%s" % (first_name, last_name, email)
    print "objectclass: top"
    print "objectclass: person"
    print "objectclass: organizationalPerson"
    print "objectclass: inetOrgPerson"
    print "objectclass: mozillaAbPersonAlpha"
    print "givenName:", first_name
    print "sn:", last_name
    print "cn:", first_name, last_name
    print "mail:", email
    print "modifytimestamp:", timestamp


def getData():
    "Return the informations entered"
    last_name = raw_input("Last name : ")
    first_name = raw_input("First name : ")
    email = raw_input("E-mail : ")
    return [last_name, first_name, email]


def writeInFile():
    "Write in a file"
    of = open(filename, 'a')
    while 1:
        last_name, first_name, email = getData()
        timestamp = getTimestamp()
        if last_name == '':
            break
        else:
            of.write("dn: cn=%s %s,mail=%s\n" % (first_name, last_name, email))
            of.write("objectclass: top\n")
            of.write("objectclass: person\n")
            of.write("objectclass: organizationalPerson\n")
            of.write("objectclass: inetOrgPerson\n")
            of.write("objectclass: mozillaAbPersonAlpha\n")
            of.write("givenName:%s\n" % first_name)
            of.write("sn:%s\n" % last_name)
            of.write("cn:%s %s\n" % (first_name, last_name))
            of.write("mail:%s\n" % email)
            of.write("modifytimestamp: %s\n\n" % timestamp)
    of.close()


def readInFile():
    "Read in a file"
    of = open(filename, 'r')
    while 1:
        line = of.readline()
        if line == "":
            break
        print line
    of.close()


filename = raw_input('Enter filename to process: ')
option = raw_input('Type "a" to add contacts or "s" to show contact list: ')

if option == 'a':
    writeInFile()
else:
    readInFile()
