# -*- coding:Utf-8 -*-
"""A generator of LDIF contact files for Mozilla Thunderbird"""
__author__ = "David SPLAWSKI <splawski.david@gmail.com>"
__version__ = "0.2"

import time


class Contact:
    def __init__(self, first_name="", last_name="", email=""):
        "Contact's constructor"
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_timestamp(timestamp):
        "Return timestamp"
        timestamp = int(time.time())
        return "%d" % timestamp

    def show_contact(self, last_name, first_name, email):
        "Show contact's informations"
        print "First name and last name:", self.first_name, self.last_name,
        "E-mail:", self.email

    def get_contact_ldif(self, first_name, last_name, email):
        "Return contact'si informations (format LDIF)"
        info = "\ndn: cn=%s %s,mail=%s\n" % (first_name, last_name, email)
        info += "objectclass: top\n"
        info += "objectclass: person\n"
        info += "objectclass: organizationalPerson\n"
        info += "objectclass: inetOrgPerson\n"
        info += "objectclass: mozillaAbPersonAlpha\n"
        info += "givenName: %s\n" % first_name
        info += "sn: %s\n" % last_name
        info += "cn: %s %s\n" % (first_name, last_name)
        info += "mail: %s\n" % email
        info += "modifytimestamp: %s\n" % self.get_timestamp()
        return info

    def get_data(self):
        "Return the informations entered"
        first_name = raw_input("First name : ")
        last_name = raw_input("last name : ")
        email = raw_input("E-mail : ")
        return [first_name, last_name, email]

    def write_in_file(self, filename):
        "Write in a file"
        of = open(filename, 'a')
        while 1:
            first_name, last_name, email = self.get_data()
            if first_name == '':
                break
            else:
                info = self.get_contact_ldif(first_name, last_name, email)
                of.write(info)
        of.close()

    def read_in_file(self, filename):
        "Read in a file"
        of = open(filename, 'r')
        while 1:
            line = of.readline()
            if line == "":
                break
            print line
        of.close()


if __name__ == '__main__':
    filename = raw_input('Enter filename to process: ')
    option = raw_input('Type "a" to add contacts or "s" to show contact list:')
    contact = Contact()
    if option == 'a':
        contact.write_in_file(filename)
    else:
        contact.read_in_file(filename)
