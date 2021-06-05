import unittest
import sys
sys.path.append('..')

from athena_client import GreetAPI, HelloAPI, SquareAPI, TodoAPI


class GreetApiTestSuite(unittest.TestCase):
    def setUp(self):
        self.client = GreetAPI()

    def test_get_request(self):
        name = 'Abhi'
        response = self.client.get_request(name)
        self.assertEqual(response.text, "Hi %s!!!" % name)


if __name__ == '__main__':
    unittest.main()

