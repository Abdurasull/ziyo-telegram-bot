import mysql.connector


class DB:
    def __init__(
        self, 
        user: str,
        password: str, 
        db_name: str, 
        host: str = 'localhost', 
        port: int = 3306
    ) -> None:
        try:
            self.__connection = mysql.connector.connect(
                user=user, password=password,
                host=host, port=port,
            )
            self.__cursor = self.__connection.cursor()
            self.__use_create_db(db_name)
            self.__initial_table()
        except mysql.connector.Error as err:
            print("Something went wrong with MYSQl Connection: {}".format(err))
    
    def __use_create_db(self, db_name: str) -> None:
        self.__cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        self.__cursor.execute(f"USE {db_name}")

    def __initial_table(self) -> None:
        self.__create_user_table()

    def __create_user_table(self) -> None:
        self.__cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT NOT NULL,
                    telegram_id BIGINT NOT NULL,
                    first_name VARCHAR(128) NOT NULL,
                    last_name VARCHAR(128),
                    username VARCHAR(128),
                    PRIMARY KEY (id),
                    UNIQUE (id, telegram_id)
                )
            """
        )

    def add_user(
        self, 
        telegram_id: int, 
        first_name: str, 
        last_name: str = None, 
        username: str = None
    ) -> bool:
        if not self.is_user(telegram_id):
            self.__cursor.execute("""
                    INSERT INTO users (telegram_id, first_name, last_name, username)
                    VALUES (%s, %s, %s, %s)
                """,
                (telegram_id, first_name, last_name, username)
            )
            self.__commmit()
            return True
        else:
            return False
    
    def is_user(self, telegram_id: int) -> bool:
        self.__cursor.execute(f"""
                SELECT * FROM users
                WHERE telegram_id={telegram_id}
            """
        )
        if self.__cursor.fetchall():
            return True
        else:
            return False
        
    def __commmit(self) -> None:
        self.__connection.commit()

    def __close(self) -> None:
        self.__cursor.close()
        self.__connection.close()
    