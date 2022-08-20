class MyQueries():
    def __init__(self):
        pass
    def insert_to_user_list(self,user_account):
        query = f"INSERT INTO user_list (user_account, created_on, is_activated) VALUES ('{user_account}',CURRENT_TIMESTAMP,true)"
        return query
    def insert_to_instagram_account(self,instagram_account):
        query = f"INSERT INTO instagram_account (instagram_account,created_on,is_activated) VALUES ('{instagram_account}',CURRENT_TIMESTAMP, true)"
        return query
    def insert_to_related_pages(self, user_id, instagram_id):
        query = f"INSERT INTO related_page (user_id,instagram_id,created_on,is_activated) VALUES ('{user_id}','{instagram_id}',CURRENT_TIMESTAMP,true)"
        return query
    def select_user_id(self, user_account):
        query = f"SELECT user_id FROM user_list WHERE user_account='{user_account}'"
        return query
    def select_instagram_id(self, instagram_account):
        query = f"SELECT instagram_id FROM instagram_account WHERE instagram_account='{instagram_account}'"
        return query