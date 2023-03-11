from peewee import *

db = SqliteDatabase('my_database.db')

class TabelaE(Model):
    campo5 = CharField()

    class Meta:
        database = db

class TabelaD(Model):
    campo4 = CharField()
    id_e = ForeignKeyField(TabelaE)

    class Meta:
        database = db

class TabelaC(Model):
    campo3 = CharField()
    id_d = ForeignKeyField(TabelaD)

    class Meta:
        database = db

class TabelaB(Model):
    campo2 = CharField()
    id_c = ForeignKeyField(TabelaC)

    class Meta:
        database = db

class TabelaA(Model):
    campo1 = CharField()
    id_b = ForeignKeyField(TabelaB)

    class Meta:
        database = db

# Cria as tabelas no banco de dados
db.create_tables([TabelaE, TabelaD, TabelaC, TabelaB, TabelaA])

# Insere alguns dados de teste
tabela_e1 = TabelaE.create(campo5='valor1')
tabela_e2 = TabelaE.create(campo5='valor2')
tabela_d1 = TabelaD.create(campo4='valor3', id_e=tabela_e1)
tabela_d2 = TabelaD.create(campo4='valor4', id_e=tabela_e2)
tabela_c1 = TabelaC.create(campo3='valor5', id_d=tabela_d1)
tabela_c2 = TabelaC.create(campo3='valor6', id_d=tabela_d2)
tabela_b1 = TabelaB.create(campo2='valor7', id_c=tabela_c1)
tabela_b2 = TabelaB.create(campo2='valor8', id_c=tabela_c2)
tabela_a1 = TabelaA.create(campo1='valor9', id_b=tabela_b1)
tabela_a2 = TabelaA.create(campo1='valor10', id_b=tabela_b2)