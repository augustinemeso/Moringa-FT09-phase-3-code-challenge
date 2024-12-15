import sqlite3

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'

    # CREATE: Add a new magazine to the database
    @classmethod
    def create_magazine(cls, name, category):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        connection.commit()
        magazine_id = cursor.lastrowid
        connection.close()
        return cls(magazine_id, name, category)

    # READ: Retrieve a magazine by ID
    @classmethod
    def get_magazine(cls, magazine_id):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id=?", (magazine_id,))
        magazine_data = cursor.fetchone()
        connection.close()
        if magazine_data:
            return cls(*magazine_data)  # Unpack the tuple into Magazine attributes
        return None

    # UPDATE: Update a magazine's details
    @classmethod
    def update_magazine(cls, magazine_id, new_name, new_category):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute(""" 
            UPDATE magazines
            SET name=?, category=?
            WHERE id=?
        """, (new_name, new_category, magazine_id))
        connection.commit()
        connection.close()

    # DELETE: Delete a magazine by ID
    @classmethod
    def delete_magazine(cls, magazine_id):
        connection = sqlite3.connect('database/magazine.db')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM magazines WHERE id=?", (magazine_id,))
        connection.commit()
        connection.close()