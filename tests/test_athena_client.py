import unittest
import sys
sys.path.append('..')

from athena_client import HelloAPI, SquareAPI, TodoAPI


class SquareApiTestSuite(unittest.TestCase):
    def setUp(self):
        self.client = SquareAPI()

    def test_get_square(self):
        num = 7
        response = self.client.get_square(num)
        self.assertEqual(response.text.strip(), '49')


class TodoApiTestSuite(unittest.TestCase):
    def setUp(self):
        self.client = TodoAPI()

    def test_1_put_task(self):
        response = self.client.put_task('task_1', 'remember the milk')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'task_1': 'remember the milk'})

    def test_2_get_task(self):
        response = self.client.get_task('task_1')
        self.assertEqual(response.json(), {'task_1': 'remember the milk'})

    def test_3_delete_task(self):
        response = self.client.delete_task('task_1')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

