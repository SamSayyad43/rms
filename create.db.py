import sqlite3

def create_db():
    try:
        # Connect to database (creates 'rms.db' if not exists)
        con = sqlite3.connect("rms.db")
        cur = con.cursor()

        # ------------------------- COURSE TABLE -------------------------
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course (
                cid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                duration TEXT,
                charges TEXT,
                description TEXT
            )
        """)

        # ------------------------- STUDENT TABLE -------------------------
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Student (
                roll INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                Email TEXT,
                Gender TEXT,
                state TEXT,
                Address TEXT,
                DOB TEXT,
                Contact TEXT,
                City TEXT,
                Course TEXT,
                AdmissionDate TEXT
            )
        """)

        # ------------------------- RESULT TABLE -------------------------
        cur.execute("""
            CREATE TABLE IF NOT EXISTS result (
                Rid INTEGER PRIMARY KEY AUTOINCREMENT,
                Roll TEXT,
                Name TEXT,
                Course TEXT,
                Marks_ob TEXT,
                FullMarks TEXT,
                per TEXT
            )
        """)

        # ------------------------- REGISTER TABLE -------------------------
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Register (
                Rid INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                LName TEXT,
                Contact TEXT,
                Email TEXT UNIQUE,
                Password TEXT,
                CPassword TEXT
            )
        """)

        # ------------------------- LOGIN TABLE -------------------------
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Login (
                Lid INTEGER PRIMARY KEY AUTOINCREMENT,
                Email TEXT UNIQUE,
                Password TEXT
            )
        """)

        # ------------------------- ADMIN TABLE -------------------------
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Admin (
                Aid INTEGER PRIMARY KEY AUTOINCREMENT,
                AdminName TEXT,
                APassword TEXT
            )
        """)

        con.commit()
        print("✅ Database and all tables created successfully!")

    except Exception as ex:
        print("❌ Error creating database:", ex)

    finally:
        con.close()

# Run automatically when executed
if __name__ == "__main__":
    create_db()
