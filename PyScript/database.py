import psycopg2         # PostgreSQL

class MyPostgreSQLData:
    def __init__(self):
        # 2. Parametry ve slovníku
        pgData = {
            'host': '127.0.0.1',  # 192.168.56.101 -  adresa virtual boxu
            'user': 'postgres',
            'password': '1234',
            'database': 'postgres',
            'port': 5432  # Není nutné, default pro daný typ databáze
        }

        self.connpg = psycopg2.connect(**pgData)
        self.cur1 = self.connpg.cursor()

    def __str__(self):
        print(f'''
            Server version:  {self.connpg.get_parameter_status("server_version")}
            Server codepage: {self.connpg.get_parameter_status("server_encoding")}
            Client codepage: {self.connpg.get_parameter_status("client_encoding")}
            Connected as superuser: {self.connpg.get_parameter_status("is_superuser")}
            DateStyles: {self.connpg.get_parameter_status("DateStyle")}
            Timezone: {self.connpg.get_parameter_status("TimeZone")}
        ''')

        print(f'''
            Server host: {self.connpg.info.host}
            Server port: {self.connpg.info.port}
            Server PID:  {self.connpg.info.backend_pid}
        ''')

    def get_all(self):
        # Přímo zadaný SQL dotaz
        self.cur1.execute('SELECT * FROM public.uzivatel')
        a = []
        for line in self.cur1.fetchall():
            # print('line:', line)
            a.append(line)

        return a


    def insert_row(self, name, surrname):

        order = f'INSERT INTO uzivatel (jmeno, prijmeni, datum_narozeni, pocet_clanku) VALUES (\'{name}\',  \'{surrname}\',  \'1995-12-03\', 36);'

        self.cur1.execute(order)





MyData = MyPostgreSQLData()
r = MyData.get_all()
print(r[3])
print(r[3][1])





