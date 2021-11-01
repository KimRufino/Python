#Elaborar um diagrama de entidades e relacionamento, e em seguida implementar em pyrhon as seguinte tabelas referentes
#um industria.
#Peças, Depositos, Fornecedor, Projeto, Funcionario, departamento.

import sqlite3

conn = sqlite3.connect('Industria.db')


print ('Banco de dados aberto com sucesso!!!')

#definindo um cursor

cursor = conn.cursor()

#TABELA PEÇAS
cursor.execute("""
CREATE TABLE Pecas(
    Nome           TEXT NOT NULL,
    Peso           INTEGER,
    Cor            TEXT
);
""")

#TABELA DEPOSITO
cursor.execute("""CREATE TABLE Deposito(
    Nome           TEXT NOT NULL,
    Endereço       TEXT NOT NULL
);
""")

#TABELA FORNECEDOR
cursor.execute("""CREATE TABLE Fornecedor(
    Nome           TEXT NOT NULL,
    Numero         VARCHAR(4) NOT NULL
);
""") 

#TABELA PROJETO
cursor.execute("""CREATE TABLE Projeto(
    Numero           VARCHAR(6) NOT NULL,
    Orcamento        TEXT NOT NULL
);
""") 

#TABELA DEPARTAMENYO
cursor.execute("""CREATE TABLE Departamento(
    Numero           VARCHAR(4) NOT NULL,
    Setor            TEXT NOT NULL       
);
""")

#TABELA FUNCIONARIOS 
cursor.execute("""CREATE TABLE Funcionarios(
    Nome           VARCHAR (60) NOT NULL,
    Telefone       VARCHAR(11) NOT NULL,
    Salario        DECIMAL(10) NOT NULL
    );
""")

print('TABELA CRIADA COM SUCESSO!')

#desconectando....
conn.close()