import psycopg2

# class to control R/W to PostgreSQL database
class MyPostgreSQLData:
    def __init__(self):
        # database parameters
        pgData = {
            'host': 'database_server',
            'user': 'postgres',
            'password': '1234',
            'database': 'postgres',
            'port': 5432
        }

        # enable database connection
        self.connpg = psycopg2.connect(**pgData)
        self.cur1 = self.connpg.cursor()

    def __del__(self):
        self.connpg.commit()
        self.connpg.close()


    def get_all(self):
        # return all elements from database table
        cur1 = self.connpg.cursor()
        cur1.execute('SELECT * FROM "reality"')
        element = []
        for line in cur1.fetchall():
            element.append(line)

        cur1.close()
        return element

    def delete_all(self):
        # delete all elements from database table
        cur1 = self.connpg.cursor()
        cur1.execute('DELETE FROM "reality"')

        cur1.close()


    def insert_row(self, name, link):
        # insert new element into table
        cur1 = self.connpg.cursor()
        order = f'INSERT INTO "reality" (name, image_link) VALUES (\'{name}\',  \'{link}\');'

        cur1.execute(order)
        self.connpg.commit()

        cur1.close()

    def create_table(self):
        cur1 = self.connpg.cursor()
        order = 'CREATE TABLE reality (ID int, name varchar(100), image_link varchar(255));'

        try:
            cur1.execute(order)
            self.connpg.commit()
        except:
            print('Table exist')

        cur1.close()