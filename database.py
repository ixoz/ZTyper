import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ztyper"
        )
        self.cursor = self.conn.cursor()

    def create_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        self.conn.commit()

    def get_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        return self.cursor.fetchone()

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return self.cursor.fetchone()

    def save_score(self, user_id, score):
        self.cursor.execute("INSERT INTO scores (user_id, score) VALUES (%s, %s)", (user_id, score))
        self.conn.commit()

    def get_scores(self, user_id):
        self.cursor.execute("SELECT score, created_at FROM scores WHERE user_id = %s ORDER BY created_at DESC", (user_id,))
        return self.cursor.fetchall()

    def update_user(self, user_id, new_username, new_password):
        self.cursor.execute("UPDATE users SET username = %s, password = %s WHERE id = %s", (new_username, new_password, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.conn.commit()

    def delete_score(self, user_id, score):
        self.cursor.execute("DELETE FROM scores WHERE user_id = %s AND score = %s LIMIT 1", (user_id, score))
        self.conn.commit()
