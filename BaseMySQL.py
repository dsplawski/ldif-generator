# -*- coding:Utf-8 -*-
"""A generator of LDIF contact files for Mozilla Thunderbird"""
__author__ = "David SPLAWSKI <splawski.david@gmail.com>"
__version__ = "0.2"

import MySQLdb


class BaseMySQL:
    "Variables of BaseMySQL"
    dbName = "david_db1"      # database
    user = "david"              # user
    passwd = "david"            # password
    host = "192.168.0.207"      # IP server

    # Thesaurus of tables & fields
    dicoT = {"employes": [('id_emp', "k", "clé primaire"),
                            ('nom', 25, "nom"),
                            ('prenom', 25, "prénom"),
                            ('email', 50, "email")]}


class GestionBD:
    "Database's management"
    def __init__(self, dbName, user, passwd, host, port=3306):
        "Database's Connection"
        try:
            self.baseDonn = MySQLdb.connect(db=dbName,
            user=user, passwd=passwd, host=host, port=port)
        except Exception, err:
            print 'The database connection failed: :\n'\
                    'Error detected :\n%s' % err
            self.echec = 1
        else:
            self.cursor = self.baseDonn.cursor()
            self.echec = 0

    def creerTables(self, dicTables):
        "Create tables"
        for table in dicTables:
            req = "CREATE TABLE %s (" % table
            pk = ''
            for descr in dicTables[table]:
                nomChamp = descr[0]
                tch = descr[1]
                if tch == 'i':
                    typeChamp = 'INTEGER'
                elif tch == 'f':
                    typeChamp = 'FLOAT'
                elif tch == 'k':
                    # field 'primary key'
                    typeChamp = 'INTEGER AUTO_INCREMENT'
                    pk = nomChamp
                else:
                    typeChamp = 'VARCHAR(%s)' % tch
                req = req + "%s %s, " % (nomChamp, typeChamp)
            if pk == '':
                req = req[:-2] + ")"
            else:
                req = req + "CONSTRAINT %s_pk PRIMARY KEY(%s))" % (pk, pk)
            self.executerReq(req)

    def supprimerTables(self, dicTables):
        "Drop tables"
        for table in dicTables.keys():
            req = "DROP TABLE %s" % table
            self.executerReq(req)
        self.commit()

    def executerReq(self, req):
        "Execute query"
        try:
            self.cursor.execute(req)
        except Exception, err:
            print " incorrect SQL query :\n%s\nError detected :\n%s"\
                % (req, err)
            return 0
        else:
            return 1

    def resultatReq(self):
        "Result of the query"
        return self.cursor.fetchall()

    def commit(self):
        if self.baseDonn:
            self.baseDonn.commit()

    def close(self):
        if self.baseDonn:
            self.baseDonn.close()


class Sauvegarde:
    "Backup"
    def __init__(self, bd, table):
        self.bd = bd
        self.table = table
        self.descriptif = BaseMySQL.dicoT[table]

    def save(self):
        "Save"
        champs = "("
        valeurs = "("
        for cha, type, nom in self.descriptif:
            if type == "k":
                continue
            champs = champs + cha + ","
            val = raw_input("Enter the field %s :" % nom)
            if type == "i" or type == 'f':
                valeurs = valeurs + val + ","
            else:
                valeurs = valeurs + "'%s'," % (val)

        champs = champs[:-1] + ")"
        valeurs = valeurs[:-1] + ")"
        req = "INSERT INTO %s %s VALUES %s" % (self.table, champs, valeurs)
        self.bd.executerReq(req)

        ch = raw_input("Continue (Y/N) ? ")
        if ch.upper() == "O":
            return 0
        else:
            return 1
