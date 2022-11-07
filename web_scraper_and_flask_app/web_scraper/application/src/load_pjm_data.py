from utils.database.postgres import PostgresOperations


def insert_to_postgres(host:str, port:int, user:str, password:str, database:str, table_name:str, dataframe) -> None:
    """
    1. Instantiates PostgresOperations class
    2. Calls execute_many to upload the given dataframe to the given table


    Args:
        host (str): database host
        port (int): database port
        user (str): database username
        password (str): database password
        database (str): name of the desired database
        table_name (str): table to load data
        dataframe (): Dataframe to load to postgres
    """    
    postgres = PostgresOperations(host, port, user, password, database)
    postgres.execute_many_insert(dataframe,table_name)
