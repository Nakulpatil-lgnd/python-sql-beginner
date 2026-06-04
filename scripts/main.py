import sqlite3
import os

def run_project():
    print("--- Starting Python + SQL Project ---")
    
    # 1. Connect to an in-memory SQLite database (it disappears when the script ends)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # 2. Find and read our schema.sql file
    schema_path = os.path.join(os.path.dirname(__file__), '../sql/schema.sql')
    with open(schema_path, 'r') as f:
        sql_schema = f.read()
    
    # 3. Execute the SQL code to create the table
    cursor.executescript(sql_schema)
    print("Success: Database table 'users' created from schema.sql!")
    
    # 4. Insert a sample user into our new database table
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice Smith", "alice@example.com"))
    conn.commit()
    print("Success: Inserted sample user 'Alice Smith' into the table!")
    
    # 5. Fetch and print the data to prove it worked
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    
    print("\n--- Database Output ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")
    print("-----------------------")
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    run_project()
