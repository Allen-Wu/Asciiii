import unittest
from .main import run

class TestBasics(unittest.TestCase):
    def test_static(self):
        config = {'file': 'data/1.jpg', 'line': 800, 'e': 0.15, 'light': False}
        result = run(config)
        self.assertNotEqual(result, '')
    def test_light(self):
        config = {'file': 'data/2.jpg', 'line': 800, 'e': 0.15, 'light': True}
        result = run(config)
        self.assertNotEqual(result, '')
    def test_all(self):
        config = {'line': 800, 'e': 0.15, 'light': False}
        result = run(config)
        self.assertNotEqual(result, '')
