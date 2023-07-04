import psycopg2

def connect():
    conn = None
    try:
        # read connection parameters
        params = {
            "database": "my_database",
            "user": "my_user",
            "password": "my_password",
            "host": "localhost",
            "port": "5432"
        }

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
       
        # create a cursor
        cur = conn.cursor()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()