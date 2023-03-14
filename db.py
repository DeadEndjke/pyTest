
import sqlite3 as sq
from user import User

class UserDAO:
    def __init__(self, dbname):
        self.__dbname = dbname
        with sq.connect("db.db") as con:
            cur = con.cursor()
            
            cur.execute("""create table if not exists user(
                id integer primary key,
                BASE_URL text not null default 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/',
                API_KEY text not null,
                LANGUAGE text not null default 'ru' check(LANGUAGE = 'ru' or LANGUAGE = 'en')
            )""")

    def showAll(self):
        with sq.connect(self.__dbname) as con:
            cur = con.cursor()

            res = cur.execute("select * from user")
            for row in res:
                print(row)

    def get_max_id(self):
         with sq.connect(self.__dbname) as con:
            cur = con.cursor()

            cur.execute("select max(id) from user")
            result = cur.fetchone()
            return result[0]


            

    def add_user(self, user):
        if isinstance(user, User):
            self.__user = user
            with sq.connect(self.__dbname) as con:
                cur = con.cursor()
                cur.execute("insert into user (API_KEY, LANGUAGE) values('" + str(user.key)+"','" + str(user.lang)+"')")

    def get_key(self, id):
        with sq.connect(self.__dbname) as con:
            cur = con.cursor()
            cur.execute("select API_KEY from user where id=" + id)
            result = cur.fetchone()
            return result[0]
    
    def get_url(self, id):
        with sq.connect(self.__dbname) as con:
            cur = con.cursor()
            cur.execute("select BASE_URL from user where id=" + id)
            result = cur.fetchone()
            return result[0]
        
    def get_lang(self, id):
        with sq.connect(self.__dbname) as con:
            cur = con.cursor()
            cur.execute("select LANGUAGE from user where id=" + id)
            result = cur.fetchone()
            return result[0]
            
   


if __name__ == "__main__":
    user = UserDAO("db.db")
    user.get_max_id()
        

    
    
