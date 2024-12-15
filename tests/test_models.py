
import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "Gilbert Kibet")
        self.assertEqual(author.name, "Gilbert Kibet")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")  # Corrected: providing the category argument
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

if __name__ == "__main__":
    unittest.main()
