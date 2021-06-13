"""
Exercise 1
----------
Create a database in your Postgres server (using `createdb`)
In psycopg2 create a table and insert some records using methods for SQL string composition. Make sure to establish
a connection and close it at the end of interacting with your database. Inspect your table schema and data in psql.
(hint: use `SELECT *` `\\dt` and `\\d`)
"""
from utils.constants import get_conn

TABLE_NAME = "vehicles"


def main():
    """
    Creates a vehicles table, inserts some values, then queries and prints the results
    :return: None
    """
    create_table = f"""
    DROP TABLE IF EXISTS {TABLE_NAME};
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        year int,
        make varchar,
        model varchar,
        mileage float
    )
    """

    insert_values = f"""
    INSERT INTO {TABLE_NAME} VALUES 
    (1994, 'Ford', 'Pinto', 18),
    (1997, 'Chevy', 'Malibu', 23),
    (1990, 'Nissan', '300ZX', 16),
    (2019, 'Nissan', 'Altima', 23)
    """

    select_all = f"SELECT * FROM {TABLE_NAME}"

    # Retriever cursor from the helper
    conn, cur = get_conn()

    # Create table and insert values
    cur.execute(create_table)
    cur.execute(insert_values)

    # Select and display results, then close the cursor
    cur.execute(select_all)
    for row in cur.fetchall():
        print(row)
    cur.close()


if __name__ == "__main__":
    main()
