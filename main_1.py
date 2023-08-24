import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# drop pra poder fazer rodar mais vezes sem ficr criando uma tabela duplicada
cursor.execute("DROP TABLE IF EXISTS Estudantes")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_Ingresso INTEGER
);
""")
               
estudantes = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022)
]



cursor.executemany("""
  INSERT INTO Estudantes(Nome, Curso, Ano_de_Ingresso)
  VALUES (?, ?, ?)
""",estudantes)


conn.commit()

cursor.execute("SELECT * FROM Estudantes ")

print(f"""{cursor.fetchall()}
------------------------------------------------------------
""")

cursor.execute("SELECT * FROM Estudantes WHERE 2019==Ano_de_Ingresso OR Ano_de_Ingresso==2020")

print(f"""{cursor.fetchall()}
------------------------------------------------------------
""")



cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = ? WHERE Nome = ?", (2018, "Pedro Mendes"))

conn.commit()

cursor.execute("SELECT * FROM Estudantes ")

print(f"""{cursor.fetchall()}
------------------------------------------------------------
""")

cursor.execute("DELETE FROM Estudantes WHERE ID = ?", ("4",))
conn.commit()

cursor.execute("SELECT * FROM Estudantes ")
print(f"""{cursor.fetchall()}
------------------------------------------------------------
""")

cursor.execute("SELECT * FROM Estudantes WHERE Curso='Computação'")
print(f"""{cursor.fetchall()}
------------------------------------------------------------
""")

cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = ? WHERE Curso = ?", (2018, "Computação"))
conn.commit()

cursor.execute("SELECT * FROM Estudantes ")
print(f"""{cursor.fetchall()}
------------------------------------------------------------
""")

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

