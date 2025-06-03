import unittest
from app.main import app

class TestHome(unittest.TestCase):
    def test_home(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from DevOps", response.data)

if __name__ == '__main__':
    unittest.main()
