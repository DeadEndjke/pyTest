
import sqlite3 as sq

class SettingsDAO:
    def __init__(self, dbname:str):
        self.__con = sq.connect(dbname)
        self.__cur = self.__con.cursor()

        self.__cur.execute("""create table if not exists settings(
            id integer primary key,
            BASE_URL text not null default 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/',
            API_KEY text,
            LANGUAGE text not null default 'ru' check(LANGUAGE = 'ru' or LANGUAGE = 'en')
        )""")
        if len(self.get_settings()) == 0:
            with self.__con:
                self.__cur.execute("insert into settings (API_KEY) values('')")
        
    
    def get_settings(self) -> list:
        return self.__cur.execute("select * from settings").fetchall()

    # def add_user(self, user:User):
    #     if isinstance(user, User):
    #         with self.__con:
    #             self.__cur.execute("insert into user (API_KEY, LANGUAGE) values(?, ?)", (user.key, user.lang))

    # def get_id(self, user:User) -> str:
    #     if isinstance(user, User):
    #         return self.__cur.execute("select id from user where API_KEY=? and LANGUAGE=?",(user.key, user.lang)).fetchone[0]

    def get_key(self) -> str:
        return self.__cur.execute("select API_KEY from settings where id=1").fetchone()[0]
    
    def get_url(self) -> str:
        return self.__cur.execute("select BASE_URL from settings where id=1").fetchone()[0]
        
    def get_lang(self) -> str:
        return self.__cur.execute("select LANGUAGE from settings where id=1").fetchone()[0]
    
    def set_key(self, key):
        with self.__con:
            self.__cur.execute("update settings set API_KEY=? where id=1", [key])

    def set_lang(self, lang):
        with self.__con:
            self.__cur.execute("update settings set LANGUAGE=? where id=1", [lang])
            

        

    
    
