from database.DB_connect import DBConnect
from model.edge import Edge
from model.node import Node


class DAO():

    @staticmethod
    def getAllEdges(... , idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
                
                """
        cursor.execute(query)

        for row in cursor:
            result.append(Edge(idMap[row['...']], idMap[row['...']], row['peso']))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """ 
                
                """
        cursor.execute(query)

        for row in cursor:
            result.append(Node(**row))

        cursor.close()
        conn.close()

        return result