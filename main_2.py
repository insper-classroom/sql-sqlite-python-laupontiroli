from db.db_utils import *
import sqlite3

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Estudantes")
conn.commit()

nome_tabela='Estudantes'

tupla_colunas=[
    ("Nome", "TEXT NOT NULL"),
    ("Curso","TEXT NOT NULL"),
    ("Ano_de_Ingresso","INTEGER")
]

criar_tabela(cursor,nome_tabela,tupla_colunas)
conn.commit()

mostrar_tabela(cursor,nome_tabela)

colunas_tupla=obter_colunas_da_tabela(cursor,nome_tabela)

estudantes = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022)
]

inserir_conteudo(cursor,nome_tabela,colunas_tupla,estudantes)
conn.commit()

mostrar_tabela(cursor,nome_tabela)

filtro="WHERE 2019==Ano_de_Ingresso OR Ano_de_Ingresso==2020"

mostrar_tabela(cursor,nome_tabela,filtro_conteudo=filtro)

coluna="ID"
condicao="4"
deletar_linhas(cursor,nome_tabela,coluna,condicao)
conn.commit()

mostrar_tabela(cursor,nome_tabela)

cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = ? WHERE Curso = ?", (2018, "Computação"))

coluna_mudar="Ano_de_Ingresso"
filtro='Curso'
mudar=2018
curso='Computação'
update_linhas(cursor,nome_tabela,coluna_mudar,mudar,filtro,curso)

mostrar_tabela(cursor,nome_tabela)