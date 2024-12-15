
import sqlite3

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    # CREATE: Add a new article to the database
    @classmethod
    def create_article(cls, title, content, author_id, magazine_id):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        """, (title, content, author_id, magazine_id))
        connection.commit()
        article_id = cursor.lastrowid
        connection.close()
        return cls(article_id, title, content, author_id, magazine_id)

    # READ: Retrieve an article by ID
    @classmethod
    def get_article(cls, article_id):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM articles WHERE id=?", (article_id,))
        article_data = cursor.fetchone()
        connection.close()
        if article_data:
            return cls(*article_data)  # Unpack the tuple into Article attributes
        return None

    # UPDATE: Update an article's details
    @classmethod
    def update_article(cls, article_id, new_title, new_content):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE articles
            SET title=?, content=?
            WHERE id=?
        """, (new_title, new_content, article_id))
        connection.commit()
        connection.close()

    # DELETE: Delete an article by ID
    @classmethod
    def delete_article(cls, article_id):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM articles WHERE id=?", (article_id,))
        connection.commit()
        connection.close()
