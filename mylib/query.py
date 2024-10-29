"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "python_query_log.md"


# def log_query(query):
#     """adds to a query markdown file"""
#     with open(LOG_FILE, "a") as file:
#         file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("candy_data_DB.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # log_query(f"{query}")


def create_record(
    competitorname,
    chocolate,
    fruity,
    caramel,
    peanutyalmondy,
    nougat,
    crispedricewafer,
    hard,
    bar,
    pluribus,
    sugarpercent,
    pricepercent,
    winpercent,
):
    """create example query"""
    conn = sqlite3.connect("candy_data_DB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO candy_data_DB
        (competitorname,
        chocolate,
        fruity,
        caramel,
        peanutyalmondy,
        nougat,
        crispedricewafer,
        hard,
        bar,
        pluribus,
        sugarpercent,
        pricepercent,
        winpercent)
        VALUES (?,?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?)
        """,
        (
            competitorname,
            chocolate,
            fruity,
            caramel,
            peanutyalmondy,
            nougat,
            crispedricewafer,
            hard,
            bar,
            pluribus,
            sugarpercent,
            pricepercent,
            winpercent,
        ),
    )
    conn.commit()
    conn.close()


def update_record(
    competitorname,
    chocolate,
    fruity,
    caramel,
    peanutyalmondy,
    nougat,
    crispedricewafer,
    hard,
    bar,
    pluribus,
    record_id,
    sugarpercent,
    pricepercent,
    winpercent,
):
    """update example query"""
    conn = sqlite3.connect("candy_data_DB.db")
    c = conn.cursor()
    print(
        (
            competitorname,
            chocolate,
            fruity,
            caramel,
            peanutyalmondy,
            nougat,
            crispedricewafer,
            hard,
            bar,
            pluribus,
            record_id,
            sugarpercent,
            pricepercent,
            winpercent,
        )
    )
    c.execute(
        """
        UPDATE candy_data_DB 
        SET competitorname=?,
        chocolate=?, 
        fruity=?, 
        caramel=?, 
        peanutyalmondy=?, 
        nougat=?, 
        crispedricewafer=?, 
        hard=?, 
        bar=?,
        pluribus=?,
        sugarpercent=?,
        pricepercent=?,
        winpercent=?
        WHERE id=?;
        """,
        (
            competitorname,
            chocolate,
            fruity,
            caramel,
            peanutyalmondy,
            nougat,
            crispedricewafer,
            hard,
            bar,
            pluribus,
            sugarpercent,
            pricepercent,
            winpercent,
            record_id,
        ),
    )

    conn.commit()
    conn.close()


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("candy_data_DB.db")
    c = conn.cursor()
    c.execute("DELETE FROM candy_data_DB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()


def read_data():
    """read data"""
    conn = sqlite3.connect("candy_data_DB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM candy_data_DB")
    data = c.fetchall()
    return data
