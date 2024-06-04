class Missao:
    def __init__(self, missao_id, nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status):
        self.missao_id = missao_id
        self.nome = nome
        self.data_lancamento = data_lancamento
        self.destino = destino
        self.estado = estado
        self.tripulacao = tripulacao
        self.carga_util = carga_util
        self.duracao = duracao
        self.custo = custo
        self.status = status

    @staticmethod
    def criar_missao(conn, missao):
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO missao (
                       nome, 
                       data_lancamento, 
                       destino, 
                       estado, 
                       tripulacao, 
                       carga_util, 
                       duracao, 
                       custo, 
                       status)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (missao.nome, missao.data_lancamento, missao.destino, missao.estado, missao.tripulacao, missao.carga_util, missao.duracao, missao.custo, missao.status))
        conn.commit()

    @staticmethod
    def ler_missao(conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM missao ORDER BY data_lancamento DESC')
        return cursor.fetchall()

    @staticmethod
    def get_missao_by_id(conn, missao_id):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM missao WHERE missao_id = ?', (missao_id,))
        return cursor.fetchone()

    @staticmethod
    def atualizar_missao(conn, missao):
        cursor = conn.cursor()
        cursor.execute('''UPDATE missao 
                       SET nome = ?,  
                       data_lancamento = ?, 
                       destino = ?, 
                       estado = ?, 
                       tripulacao = ?, 
                       carga_util = ?, 
                       duracao = ?, 
                       custo = ?, 
                       status = ?
                    WHERE missao_id = ?''',
                       (missao.nome, missao.data_lancamento, missao.destino, missao.estado, missao.tripulacao, missao.carga_util, missao.duracao, missao.custo, missao.status, missao.missao_id))
        conn.commit()

    @staticmethod
    def delete_missao(conn, missao_id):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM missao WHERE missao_id = ?', (missao_id,))
        conn.commit()

    @staticmethod
    def atualizar_missao(conn, missao):
        cursor = conn.cursor()
        sql = ''' UPDATE missao
                  SET nome = ?,
                      data_lancamento = ?,
                      destino = ?,
                      estado = ?,
                      tripulacao = ?,
                      carga_util = ?,
                      duracao = ?,
                      custo = ?,
                      status = ?
                  WHERE missao_id = ?'''
        cursor.execute(sql, (missao.nome,  missao.data_lancamento, missao.destino, missao.estado, missao.tripulacao, missao.carga_util, missao.duracao, missao.custo, missao.status, missao.missao_id))
        conn.commit()

    @staticmethod
    def pesquisar_missao_por_data(conn, data_de_inicio, data_do_fim):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM missao WHERE data_lancamento BETWEEN ? AND ? ORDER BY data_lancamento DESC", (data_de_inicio, data_do_fim))
        return cursor.fetchall()