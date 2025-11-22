#
# import psycopg2
#
# class PostgresConnectorContextManager:
#     def __init__(self, db_host: str, db_name: str, ...):
#         # init
#
#     def __enter__(self):
#         # create conn
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         # close conn
#
#     def get_data_sql(self, sql):
#         # exec query, result = pandas df

import psycopg2
import pandas as pd

class PostgresConnectorContextManager:
    def __init__(self, db_host: str, db_port: int, db_name: str, db_user: str, db_password: str):
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=self.db_host,
            port=self.db_port,
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.connection:
            self.connection.close()

    def get_data_sql(self, sql):
        return pd.read_sql(sql, self.connection)

