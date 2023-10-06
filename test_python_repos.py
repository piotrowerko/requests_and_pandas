import unittest

from python_repos import get_status

class TestPythonRepos(unittest.TestCase):
    
    def test_status_code(self):
        """Test case of api response status code"""
        status = get_status()
        self.assertEqual(status, 200)


if __name__ == '__main__':
    unittest.main()