from peewee import *

db = SqliteDatabase('my_database.db')

class TabelaA(Model):
    campo1 = CharField()
    id_b = IntegerField()

    class Meta:
        database = db

class TabelaB(Model):
    campo2 = CharField()
    id_c = IntegerField()

    class Meta:
        database = db

class TabelaC(Model):
    campo3 = CharField()
    id_d = IntegerField()

    class Meta:
        database = db

class TabelaD(Model):
    campo4 = CharField()
    id_e = IntegerField()

    class Meta:
        database = db

class TabelaE(Model):
    campo5 = CharField()

    class Meta:
        database = db

# Define as condições de junção
join1 = TabelaA.id_b == TabelaB.id
join2 = TabelaB.id_c == TabelaC.id
join3 = TabelaC.id_d == TabelaD.id
join4 = TabelaD.id_e == TabelaE.id

# Faz o join entre as tabelas usando as condições definidas
query = (TabelaA.select()
          .join(TabelaB, on=join1)
          .join(TabelaC, on=join2)
          .join(TabelaD, on=join3)
          .join(TabelaE, on=join4))

# Executa a query e imprime os resultados
for registro in query:
    print(registro.campo1, registro.tabelab.campo2, registro.tabelab.tabelac.campo3,
          registro.tabelab.tabelac.tabelad.campo4, registro.tabelab.tabelac.tabelad.tabelae.campo5)
