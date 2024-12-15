import pytest
import sqlite3

@pytest.fixture(scope="function")
def setup_database():
    # Set up the database schema and test data before each test
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Create tables and insert test data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            author_id INTEGER,
            magazine_id INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT
        )
    ''')
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Weekly', 'Technology')")
    cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES ('The Rise of AI', 'Content about AI', 1, 1)")

    conn.commit()

    yield conn  # Provide the connection to the tests

    # Clean up the database after the test
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()
