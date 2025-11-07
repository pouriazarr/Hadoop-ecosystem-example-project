from pyhive import hive

with hive.connect(
        host="hive-server", port=10000,
        username="hive", password="hive", auth="CUSTOM"
) as conn:
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS loans")
    cur.execute("USE loans")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            id INT, fullname STRING, code STRING,
            amount DOUBLE, year INT
        )
        COMMENT 'Table of loans'
        ROW FORMAT DELIMITED
            FIELDS TERMINATED BY '\t'
            LINES TERMINATED BY '\n'
        STORED AS TEXTFILE
    """)

    cur.execute("""
        INSERT INTO loans (id, fullname, code, amount, year) VALUES
        (1, 'pouria zpr', '3412323', 100000.0, NULL),
        (2, 'ali karimi', '52132132', 30000.0, NULL),
        (3, 'vahid vahidi', '4123213245', 510000000.0, NULL)
    """)

    cur.execute("SELECT * FROM loans")
    cur.execute("SELECT * FROM loans WHERE amount > 3000")
    for i in cur.fetchall():
        print(i)
    print(cur.fetchall())

