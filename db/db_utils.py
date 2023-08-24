

def criar_tabela(cursor,nome_tabela,tuplas_colunas):
    '''
    Função que cria uma tabela se não existe uma ainda com o mesmo nome na base de dados

    ------------
    argumentos:
    cursor: 
        cursor da conexão feita com a base de dados
    nome_tabela: str 
        nome da tabela 
    tupla_colunas: list de tupla de strings do tipo (nome_coluna,tipo de conteudo)
        uma lista com tuplas dos nomes das colunas com o tipo de conteudo nelas (INTEGER,TEXT, etc)
    '''

    colunas_sql = ", ".join([f"{coluna} {tipo}" for coluna, tipo in tuplas_colunas])

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome_tabela}(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    {colunas_sql}
    );
    """)


def mostrar_tabela(cursor,tabela,filtro_conteudo='',filtro_colunas="*"):
    '''
    Função que mostra a tabela inteira em seu estado atual

    ------------
    argumentos:
    cursor: 
        ursor da conexão feita com a base de dados
    tabela: str 
        nome da tabela 
    filtro_conteudo: str
    default do filtro_conteudo=''
        filtro passado pelo usuario para mostrar oq quer das colunas
    '''
    cursor.execute(f"SELECT {filtro_colunas} FROM {tabela} {filtro_conteudo} ")

    print(f"""{cursor.fetchall()}
    ------------------------------------------------------------
    """)


def inserir_conteudo(cursor,tabela,colunas,conteudo):
    '''
    Função que inseri conteudo das colunas de uma tabela

    --------
    argumentos:
    cursor: 
        ursor da conexão feita com a base de dados
    tabela: str 
        nome da tabela 
    colunas: tupla 
    tupla com o nome de todas as colunas
    '''
    cursor.executemany(f"""
    INSERT INTO {tabela} {tuple(colunas)}
    VALUES (?, ?, ?)
    """,conteudo)
    

def obter_colunas_da_tabela(cursor, nome_tabela):
    '''
    Função que retorna uma lista com todas as colunas da tabela
    
    ---------
    argumentos:
    cursor: 
        cursor da conexão feita com a base de dados
    nome_tabela: str 
        nome da tabela 
    '''
    cursor.execute(f"PRAGMA table_info({nome_tabela})")
    colunas_info = cursor.fetchall()
    colunas = [coluna[1] for coluna in colunas_info]# O índice 1 contém o nome da coluna
    colunas=colunas[1:] #Tirando o ID
    return colunas

def deletar_linhas(cursor,tabela,coluna_da_cond,condicao):

    cursor.execute(f"DELETE FROM {tabela} WHERE {coluna_da_cond} = ?", (condicao,))


def update_linhas(cursor,tabela,coluna_mudar,mudar_para,coluna_filtro='',condicao=''):
    filtro=f"WHERE {coluna_filtro} = ?"
    if coluna_filtro=='':
        filtro=coluna_filtro
    cursor.execute(f"UPDATE {tabela} SET {coluna_mudar} = ? {filtro} ", (mudar_para,condicao))
