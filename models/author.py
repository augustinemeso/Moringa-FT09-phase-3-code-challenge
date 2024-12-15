import sqlite3

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'

    # CREATE: Add a new author to the database
    @classmethod
    def create_author(cls, name):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        connection.commit()
        author_id = cursor.lastrowid
        connection.close()
        return cls(author_id, name)

    # READ: Retrieve an author by ID
    @classmethod
    def get_author(cls, author_id):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM authors WHERE id=?", (author_id,))
        author_data = cursor.fetchone()
        connection.close()
        if author_data:
            return cls(*author_data)  # Unpack the tuple into Author attributes
        return None

    # UPDATE: Update an author's name
    @classmethod
    def update_author(cls, author_id, new_name):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE authors SET name=? WHERE id=?", (new_name, author_id))
        connection.commit()
        connection.close()

    # DELETE: Delete an author by ID
    @classmethod
    def delete_author(cls, author_id):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM authors WHERE id=?", (author_id,))
        connection.commit()
        connection.close()