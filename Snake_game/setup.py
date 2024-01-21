import mysql.connector as connector

config = {
    "user": "root",
    "host": "localhost"
}
db_name = "Score_Board"
table_name = "player"

class DBplayer:    
    def __init__(self):
        self.con = connector.connect(**config)

        #create database
        query = f'create database if not exists {db_name}'
        self.cur = self.con.cursor()
        self.cur.execute(query)
        #use database
        query = f'use {db_name}'
        self.cur.execute(query)
        #create table
        query = f'create table if not exists {table_name} (user_id int not null auto_increment, user_name varchar(50) not null, high_score int)'
        self.cur.execute(query)
        print(f'Database {db_name} created, Table {table_name} created')
    
    def insert_user(self,user_id, user_name,high_score):
        self.query = f"insert into {table_name}(user_id,user_name,high_score) values ({user_id},'{user_name}',{high_score})"
        print(self.query)
        self.cur.execute(self.query)
        self.con.commit()
        # print("Player saved to db...")

    def fetch(self):
        query = f"select highScore from {table_name}"
        self.cur.execute(query)
        highscore = self.cur.fetchone()
        return highscore
    
    def update(self):
        query = f"select * from {table_name}"
        self.cur.execute(query)




# player_a.insert_user(1,"Raju",100)