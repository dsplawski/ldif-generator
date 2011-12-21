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

    def __repr__(self):
        "Show contact's informations"
        return "%s %s <%s>" % (self.first_name, self.last_name, self.email)

    def get_timestamp(self):
        "Return timestamp"
        timestamp = int(time.time())
        return "%d" % timestamp

    def get_contact_ldif(self):
        "Return contact'si informations (format LDIF)"
        info = "\ndn: cn=%s %s,mail=%s\n"\
        % (self.first_name, self.last_name, self.email)
        info += "objectclass: top\n"
        info += "objectclass: person\n"
        info += "objectclass: organizationalPerson\n"
        info += "objectclass: inetOrgPerson\n"
        info += "objectclass: mozillaAbPersonAlpha\n"
        info += "givenName: %s\n" % self.first_name
        info += "sn: %s\n" % self.last_name
        info += "cn: %s %s\n" % (self.first_name, self.last_name)
        info += "mail: %s\n" % self.email
        info += "modifytimestamp: %s\n" % self.get_timestamp()
        return info
