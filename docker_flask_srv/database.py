import psycopg2         # PostgreSQL

class MyPostgreSQLData:
    def __init__(self):
        # 2. Parametry ve slovníku
        pgData = {
            'host': 'database_server',  # 192.168.56.101 -  adresa virtual boxu
            'user': 'postgres',
            'password': '1234',
            'database': 'postgres',
            'port': 5432  # Není nutné, default pro daný typ databáze
        }

        self.connpg = psycopg2.connect(**pgData)
        self.cur1 = self.connpg.cursor()
    def __del__(self):
        self.connpg.commit()
        self.connpg.close()

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
        cur1 = self.connpg.cursor()
        cur1.execute('SELECT * FROM "reality"')
        a = []
        for line in cur1.fetchall():
            # print('line:', line)
            a.append(line)

        cur1.close()
        return a

    def delete_all(self):
        cur1 = self.connpg.cursor()
        cur1.execute('DELETE FROM public.reality')

        cur1.close()


    def insert_row(self, name, link):
        cur1 = self.connpg.cursor()
        order = f'INSERT INTO public.reality (name, image_link) VALUES (\'{name}\',  \'{link}\');'
        print(order)

        cur1.execute(order)
        self.connpg.commit()

        cur1.close()





# MyData = MyPostgreSQLData()

# MyData.insert_row('pppp','op')

# r = MyData.get_all()
# print(r)






