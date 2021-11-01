import sqlite3


conn = sqlite3.connect('Industria.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM Pecas; """)
for linhas in cursor.fetchall():
    
    print(linhas)        

cursor.execute("""
SELECT * FROM Deposito""")
for linhas in cursor.fetchall():
    print(linhas)
    

cursor.execute("""
SELECT * FROM Fornecedor""")
for linhas in cursor.fetchall():
    print(linhas)
    

cursor.execute("""
SELECT * FROM Projeto""")
for linhas in cursor.fetchall():
    print(linhas)
    

cursor.execute("""
SELECT * FROM Departamento""")

for linhas in cursor.fetchall():    
    print(linhas)

cursor.execute("""
SELECT * FROM Funcionarios""")
for linhas in cursor.fetchall():    
    print(linhas)

conn.close()

