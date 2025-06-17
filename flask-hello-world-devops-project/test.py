import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_root(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, World", response.data)

if __name__ == '__main__':
    unittest.main()
