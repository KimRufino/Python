import sqlite3

conn = sqlite3.connect('Industria.db')

cursor = conn.cursor()

cursor.execute("""
INSERT INTO Pecas(Peso, Nome, Cor)
VALUES('1', 'Parafuso', 'Cinza'),('1', 'Porca', 'Azul'),('1', 'Arruela', 'Amarelo'),('20', 'Sapata', 'Cinza'),('40', 'Porta', 'Cinza');""")

cursor.execute("""
INSERT INTO Deposito(Nome, Endereço)
VALUES('Martins', 'Av Sao Manoel SN'), ('Rufino', 'Av Pde Joel SN'), ('Aurorense', 'Rua Sao Sebastião SN'), ('DevilmyCry', 'Av Calamidade SN'), ('Pandemic', 'Av Fim do Mundo SN');

""")
#Informação fornecedor
cursor.execute("""
INSERT INTO Fornecedor(Nome, Numero)
VALUES('Rua Moacir Franco', '0001'), ('Rua Raul Franco', '0002'), ('Rua Fael Franco', '0003'), ('Rua Silva Franco', '0004'), ('Rua Pandemonia', '0005');
""")
#Informação Projeto
cursor.execute("""
INSERT INTO Projeto(Numero, Orcamento)
VALUES('0001', '500000'), ('0002', '100000'), ('0003', '200000'), ('0004', '300000'), ('0005', '400000');
""")

cursor.execute("""
INSERT INTO Departamento(Numero, Setor)
VALUES('0001', 'Administracao'), ('0002', 'Almoxarifado'), ('0003', 'Fiscal'), ('0004', 'Segurança'), ('0005', 'TI');
""")

cursor.execute("""
INSERT INTO Funcionarios(nome, Salario, Telefone)
VALUES ('Ana', '10000,00','90000000000'), ('Seya', '8000,00', '99000000000'), ('Goku', '70000,00', '99900000000'), ('Cloud', '5000,00', '99990000000'), ('Sephirot', '5000,00', '99999900000');
""")

conn.commit()

conn.close()