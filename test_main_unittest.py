import unittest
from main import Greeter


class MainTestCase(unittest.TestCase):

    def test_hello_world(self):
        g = Greeter()
        result = g.greet()
        self.assertEqual("Hello world!", result)

    def test_hello_name(self):
        g = Greeter()
        result = g.greet(who="John")
        self.assertEqual("Hello John!", result)
