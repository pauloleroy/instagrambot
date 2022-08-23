import psycopg2 as pg2

class DBConnection():
    def __init__(self, queries):
        self.conn = pg2.connect(database='bottest', user='postgres',password='3720')
        self.queries = queries
            
    def insert_user(self):
        pass

    def insert_login_track(self):
        pass

    def insert_instagram_account(self, instagram_account):

        pass

    def insert_following(self):
        pass

    def drop_following(self):
        pass

    def insert_follower(self):
        pass

    def drop_follower(self):
        pass

    def insert_bot_action(self):
        pass
    
    def insert_like_track(self):
        pass

    def insert_related_page(self, user_id, instagram_id):
        cur = self.conn.cursor()
        query = self.queries.select_user_id(user_id)
        cur.execute(query)
        my_user_id = cur.fetchall()[0][0]
        #Insert instagram id if not exist otherwise get instagram id
        query = self.queries.select_instagram_id(instagram_id)
        cur.execute(query)
        my_instagram_id = cur.fetchall()[0][0]
        #cur.commit()
        pass

    def drop_related_page(self):
        pass

    def select_related_page(self):
        pass

    def select_follower_vs_bot(self):
        pass
