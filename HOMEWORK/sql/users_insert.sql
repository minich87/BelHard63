import psycopg2


conn = psycopg2.connect('postgresql://minich:12345@localhost:5432/bh63')
with conn:
    with conn.cursor() as cur:
        cur.executemany('''
            INSERT INTO users(name, email) VALUES(?, ?);
            ''', (('Alex', 'a.ivanov@mail.com'),
                  ('Ann', 'ann87@gmail.com'),
                  ('Nick', 'Nixs@tut.by'),
                  ('Maksim', 'Max_lite@gmail.com'),
                  ('Vasya', 'v.smirnoff@gmail.com')))
        conn.commit()
conn.close()
