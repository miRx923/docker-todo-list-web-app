""" Module defining basic database operations """

from flask import redirect, url_for, jsonify
import psycopg2
import os


def get_db_params():
    """ Getter for getting database connection parameters """

    # Use environment variables to get database connection parameters
    db_params = {
        "db_host": None,
        "db_name": None,
        "db_user": None,
        "db_password": None
    }

    # Check if the environment variables exists before assigning
    if "DB_HOST" in os.environ and os.environ["DB_HOST"] is not None:
        db_params["db_host"] = os.environ["DB_HOST"]
    else:
        db_params["db_host"] = "database"

    if "POSTGRES_DB" in os.environ and os.environ["POSTGRES_DB"] is not None:
        db_params["db_name"] = os.environ["POSTGRES_DB"]
    else:
        db_params["db_name"] = "todo_db"

    if "POSTGRES_USER" in os.environ and os.environ["POSTGRES_USER"] is not None:
        db_params["db_user"] = os.environ["POSTGRES_USER"]
    else:
        db_params["db_user"] = "todo_user"

    if "POSTGRES_PASSWORD" in os.environ and os.environ["POSTGRES_PASSWORD"] is not None:
        db_params["db_password"] = os.environ["POSTGRES_PASSWORD"]
    else:
        db_params["db_password"] = "pass"

    return db_params


def get_conn():
    """ Getter for database psycopg2 connect() """

    db_params = get_db_params()

    # Initialize connection
    conn = psycopg2.connect(
            host=db_params["db_host"],
            database=db_params["db_name"],
            user=db_params["db_user"],
            password=db_params["db_password"])
    
    return conn


def db_init():
    """ Function for initializing database """

    conn = get_conn()
    cur = conn.cursor() # Create a cursor object to execute SQL queries

    # Check if the todo table exists
    cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'todo')")
    table_exists = cur.fetchone()[0]

    # If todo table does not exist, create one
    if not table_exists:
        # Define the SQL query to create the todo table
        create_table = "CREATE TABLE todo (id SERIAL PRIMARY KEY, task VARCHAR(500) NOT NULL, completed BOOLEAN NOT NULL)"
        cur.execute(create_table) # Execute the create table query
        conn.commit() # Commit the transaction to save the changes

    # Close the cursor and connection
    cur.close()
    conn.close()


def db_fetch():
    """ Function for fetching database contents """

    conn = get_conn()
    cur = conn.cursor() # Create a cursor object to execute SQL queries

    cur.execute("SELECT task, completed FROM todo") # Execute the SQL query to fetch data from the Todo table
    rows = cur.fetchall() # Fetch all rows from the result set

    # Close the cursor and connection
    cur.close()
    conn.close()

    return rows


def add_task(task):
    """ Function for adding task to the todo table """

    # Check if the task is empty or contains only whitespace
    if not task.strip():  
        return jsonify({'error': 'Task cannot be empty'}), 400  # Return error response
    
    # If the task is not empty add it to the database todo table
    else:
        conn = get_conn()
        cur = conn.cursor() # Create a cursor object to execute SQL queries

        cur.execute("INSERT INTO todo (task, completed) VALUES (%s, %s)", (task, False)) # Execute the query
        conn.commit() # Commit the transaction to save the changes

        # Close the cursor and connection
        cur.close()
        conn.close()


def delete_task(task):
    """ Function for deleting task from the todo table """

    conn = get_conn()
    cur = conn.cursor() # Create a cursor object to execute SQL queries

    cur.execute("DELETE FROM todo WHERE task = %s", (task,)) # Execute the query
    conn.commit() # Commit the transaction to save the changes

    # Close the cursor and connection
    cur.close()
    conn.close()


def toggle_completion(task):
    """ Function for toggling task completion in the todo table """

    conn = get_conn()
    cur = conn.cursor() # Create a cursor object to execute SQL queries

    cur.execute("UPDATE todo SET completed = NOT completed WHERE task = %s", (task,)) # Execute the query
    conn.commit() # Commit the transaction to save the changes

    # Close the cursor and connection
    cur.close()
    conn.close()
