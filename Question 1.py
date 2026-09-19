import sqlite3

DB_FILE = "example.db"

def main():

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL
        )
    """)

    cursor.execute("DELETE FROM employees")


    employees = [ ("Alice Moyo", "Engineering", 850),
                  ("Brian Walker", "Marketing", 620),
                  ("Chipo Ndebele", "Engineering", 910),
                  ("David Sithole", "Finance", 700),]

    cursor.executemany(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        employees,
    )
    conn.commit()


    print("All employees:")
    cursor.execute("SELECT id, name, department, salary FROM employees")
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]:<18} {row[2]:<12} ${row[3]:,.2f}")

    print("\nEngineering employees:")
    cursor.execute("SELECT name, salary FROM employees WHERE department = ?",
        ("Engineering",),)

    for name, salary in cursor.fetchall():
        print(f"  {name}: ${salary:,.2f}")

    cursor.execute("SELECT AVG(salary) FROM employees")
    print(f"\nAverage salary: ${cursor.fetchone()[0]:,.2f}")

    conn.close()


if __name__ == "__main__":
    main()