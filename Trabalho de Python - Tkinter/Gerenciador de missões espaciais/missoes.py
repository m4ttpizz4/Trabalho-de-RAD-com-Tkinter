class Missao:
    def __init__(self, id, nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status):
        self.id = id
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
    def get_missao_by_id(conn, id):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM missao WHERE id = ?', (id,))
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
                    WHERE id = ?''',
                       (missao.nome, missao.data_lancamento, missao.destino, missao.estado, missao.tripulacao, missao.carga_util, missao.duracao, missao.custo, missao.status, missao.id))
        conn.commit()

    @staticmethod
    def delete_missao(conn, id):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM missao WHERE id = ?', (id,))
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
                  WHERE id = ?'''
        cursor.execute(sql, (missao.nome,  missao.data_lancamento, missao.destino, missao.estado, missao.tripulacao, missao.carga_util, missao.duracao, missao.custo, missao.status, missao.id))
        conn.commit()