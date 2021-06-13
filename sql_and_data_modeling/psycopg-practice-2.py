"""
Exercise 2
Now modify your script to use string composition throughout. Use both `%s` and `%(named_var)s` methods.
Run the script and then connect to the database using psql to inspect that the records were properly inserted into 
the tables in our database.

Exercise 3
Fetch results from your first created record to create a new record slightly modified.
Fetch all of the rows from the table and print each item line-by-line using a loop.
"""

from utils.constants import get_conn

TABLE_NAME = "vehicles"
COLUMNS = ["year", "make", "model", "mileage"]
TYPES = ["int", "varchar", "varchar", "float"]
VALUES = """
(1994, 'Ford', 'Pinto', 18),
(1997, 'Chevy', 'Malibu', 23),
(1990, 'Nissan', '300ZX', 16),
(2019, 'Nissan', 'Altima', 23)
"""


def main():
    """
    Creates a vehicles table, inserts some VALUES, then queries and prints the results
    :return: None
    """
    create_table = f"""
    DROP TABLE IF EXISTS {TABLE_NAME};
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        {COLUMNS[0]} {TYPES[0]},
        {COLUMNS[1]} {TYPES[1]},
        {COLUMNS[2]} {TYPES[2]},
        {COLUMNS[3]} {TYPES[3]}
    )
    """

    insert_values = f"INSERT INTO {TABLE_NAME} VALUES {VALUES}"

    select_all = f"SELECT * FROM {TABLE_NAME}"

    # Retriever cursor from the helper
    conn, cur = get_conn()

    # Create table and insert VALUES
    cur.execute(create_table)
    cur.execute(insert_values)

    # Select and display results, then close the cursor
    cur.execute(select_all)
    for row in cur.fetchall():
        print(row)
    cur.close()


if __name__ == "__main__":
    main()
