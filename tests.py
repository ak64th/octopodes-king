import unittest

from octopodes.app import greet


class TestGreeting(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(greet(), "Hello, world.")

if __name__ == '__main__':
    unittest.main()