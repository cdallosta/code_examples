import logging

import psycopg2

logger=logging.getLogger(__name__)

class PostgresOperations:
    def __init__(self, host, port, user, password, database,):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def _connection(
        self,
    ) ->psycopg2:
        """Creates database connection object

        Raises:
            error: connection errors

        Returns:
            {psycopg2}: connection object
        """        
        conn = None
        try:
            # connect to the PostgreSQL server
            logger.debug("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
            )
        except (Exception, psycopg2.DatabaseError) as error:
            raise error
        return conn

    def test_connect(self)->bool:
        """Test the connection with the database

        Returns:
            (bool): the result of the connection test
        """
        with self._connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT VERSION()")
                results = cursor.fetchone()
                if results:
                    logger.info("Connection established")
                    return True
                else:
                    logger.error("Unable to connect to the database")
                    return False 

    def execute_many(self, dataframe,table_name:str)->None:
        """
        Inserts and commits the given dataframe to the given table.
        Rollsback insert if error

        Args:
            dataframe (): the dataframe to upload
            table_name (str): the tame of the table

        """
        tuples = [tuple(x) for x in dataframe.to_numpy()]

        cols = ",".join(list(dataframe.columns))

        value_statement = str(tuple(["%%s" for x in list(dataframe.columns)])).replace("'", "")

        with self._connection() as conn:
            with conn.cursor() as cursor:
                query = f"INSERT INTO %s(%s) VALUES{value_statement}" % (
                    table_name,
                    cols,
                )

                cursor = conn.cursor()
                try:
                    cursor.executemany(query, tuples)
                    conn.commit()
                    logger.info("Upload Succesful")
                except (Exception, psycopg2.DatabaseError) as error:
                    conn.rollback()
                    logger.error(error)
                    return 1

