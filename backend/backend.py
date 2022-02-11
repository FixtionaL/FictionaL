import mysql.connector
from decouple import config

class storage:
    def __init__(self,cog_name):
        
        self.cog_name=cog_name
        self.db=mysql.connector.connect(host=config('mysqldb_host'),user=config('mysqldb_user'),passwd=config('mysqldb_password'),port=config('mysqldb_port'),database=config('mysqldb_database'))
        # print("backend connected to mysql database!")
        self.cursor=self.db.cursor()

        self.cursor.execute("show tables");
        self.tables=[i[0]for i in self.cursor.fetchall()]
        
        
    def register_guild(self,default:dict):
        pass

    def get_cog_list(self,):
        RES={}
        if 'main_cog_list' not in self.tables:
            self.cursor.execute("create table main_cog_list(name varchar(20) primary key,path varchar(100),loaded boolean)")
            self.cursor.execute("show tables");
            self.tables=[i[0]for i in self.cursor.fetchall()]
            # self.cursor.execute("insert into main_cog_list values('cog_handeler','cogs.cog_handeler',1)")
            self.db.commit()
        self.cursor.execute("select * from main_cog_list")
        result=self.cursor.fetchall()
        for i in result:
            RES[i[0]]=i[1:]
        return RES
        
    def add_cog_to_list(self,cog_name:str):
        self.cursor.execute(f"insert into main_cog_list values('{cog_name}')")
        self.db.commit()

    def remove_cog_from_list(self,cog_name:str):
        self.cursor.execute(f"delete from main_cog_list where name='{cog_name}'")
        self.db.commit()        
    def update_cog_list(self,cog_name:str,loaded:bool):
        self.cursor.execute(f"update main_cog_list set loaded={loaded} where name='{cog_name}'")
        self.db.commit()

    def get_prefix(self,client,ctx)->str:
        if(self.cog_name!="main"):
            raise Exception("This function is only for main cog")
        self.db.commit()
        default_prefix='--'
        if 'main_prefix' in self.tables:
            if(ctx.guild is None):
                self.cursor.execute("select * from main_prefix where guild_id='no_guild'")
                RES=self.cursor.fetchone()
                if(RES is None):
                    self.cursor.execute("insert into main_prefix (guild_id,prefix) values ('no_guild','{}')".format(default_prefix))
                    self.db.commit()
                    return default_prefix
                return RES[1]
            self.cursor.execute("select * from main_prefix where guild_id='{}'".format(ctx.guild.id))
            r=self.cursor.fetchone()
            if r is not None:
                return r[1]
            self.cursor.execute(f"insert into main_prefix values('{ctx.guild.id}','{default_prefix}')")
        else:
            self.cursor.execute("create table main_prefix(guild_id varchar(20) primary key,prefix varchar(5))")
            self.cursor.execute(f"insert into main_prefix values('{ctx.guild.id}','{default_prefix}')")
            self.cursor.execute("show tables");
            self.tables=[i[0]for i in self.cursor.fetchall()]
        self.db.commit()
        return default_prefix
    def set_prefix(self,guild,prefix:str):
        self.cursor.execute(f"update main_prefix set prefix='{prefix}' where guild_id='{guild}'")
        self.db.commit()
    


# b=backend(None,"main")
# b.set_prefix('--')
# print('prefix:',b.get_prefix())


        