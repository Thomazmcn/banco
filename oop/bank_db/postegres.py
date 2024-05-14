import psycopg2

hostname = "127.0.0.1"
database = "bank_db"
username = "postgres"
pwd = "12345"
port_id = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=hostname, dbname=database, user=username, password=pwd, port=port_id
    )
    cur = conn.cursor()

    create_script = """ CREATE TABLE IF NOT EXISTS custumer (
                            id      int PRIMARY KEY,
                            ag      int,
                            ac      int,
                            hash    varchar(64),
                            salt    varchar(90),
                            balance float,
                            credit  JSONB,
                            debt    JSONB,
                            origin  INTEGER[],
                            destiny INTEGER[]


    )"""
    cur.execute(create_script)

    conn.commit()

except Exception as error:
    print(error)


finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
