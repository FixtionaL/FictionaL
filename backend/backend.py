
import mysql.connector
from decouple import config

class storage:
    def __init__(self,cog_name):
        
        self.cog_name=cog_name
        self.db=mysql.connector.connect(host=config('mysqldb_host'),user=config('mysqldb_user'),passwd=config('mysqldb_password'),port=config('mysqldb_port'),database=config('mysqldb_database'))
        print("backend connected to mysql database!")
        self.cursor=self.db.cursor()
        
        
    def register_guild(self,default:dict):
        pass

    def get_cog_list(self,):
        
        pass
    
    def get_prefix(self,client,ctx)->str:
        if(self.cog_name!="main"):
            raise Exception("This function is only for main cog")
        default_prefix='--'
        self.cursor.execute("show tables");
        result=[i[0]for i in self.cursor.fetchall()]
        if 'main_prefix' in result:
            self.cursor.execute("select * from main_prefix")
            r=self.cursor.fetchall()
            for i in range(len(r)):
                if str(ctx.guild.id)==r[i][0]:
                    return r[i][1]
            self.cursor.execute(f"insert into main_prefix values('{ctx.guild.id}','{default_prefix}')")
        else:
            self.cursor.execute("create table main_prefix(guild_id varchar(20) primary key,prefix varchar(5))")
            self.cursor.execute(f"insert into main_prefix values('{ctx.guild.id}','{default_prefix}')")
        self.db.commit()
        return default_prefix
    def set_prefix(self,guild,prefix:str):
        self.cursor.execute(f"update main_prefix set prefix='{prefix}' where guild_id='{guild}'")
        self.db.commit()
    




# b=backend(None,"main")
# b.set_prefix('--')
# print('prefix:',b.get_prefix())


        